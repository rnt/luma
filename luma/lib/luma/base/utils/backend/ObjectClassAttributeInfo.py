# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2003 by Wido Depping                                      
#    <widod@users.sourceforge.net>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

import ldap
import ldap.schema
import re
import string
from sets import Set

from base.backend.ServerList import ServerList
import environment

class UnknownAttribute:
    pass

class ObjectClassAttributeInfo(object):
    """ A class for getting information about objectclasses and attributes 
    from a server.
    """

###############################################################################
    
    def __init__(self, server=None):
        self.OBJECTCLASSES = {}
        self.ATTRIBUTELIST = {}
        self.SERVER = server
        
        # delete oid for userPassword attribute
        #if ldap.schema.NOT_HUMAN_READABLE_LDAP_SYNTAXES.has_key('1.3.6.1.4.1.1466.115.121.1.40'):
        #    del ldap.schema.NOT_HUMAN_READABLE_LDAP_SYNTAXES['1.3.6.1.4.1.1466.115.121.1.40']
        
        if not (server == None):
            self.retrieveInfoFromServer()

###############################################################################

    def retrieveInfoFromServer(self):
        """ Retrieve all information of objectclasses and attributes from the
        server.
        """
        
        tmpObject = ServerList()
        tmpObject.readServerList()
        serverMeta = ""
        serverMeta = tmpObject.get_serverobject(self.SERVER)

        environment.setBusy(1)

        try:
            tmpUrl = "ldap://" + serverMeta.host + ":" + str(serverMeta.port)
            subschemasubentry_dn,schema = ldap.schema.urlfetch(tmpUrl)
            oidList = schema.listall(ldap.schema.ObjectClass)
            
            for x in oidList:
                environment.updateUI()
                y = schema.get_obj(ldap.schema.ObjectClass, x)
                name = y.names[0]
                
                desc = ""
                if not (y.desc == None):
                    desc = y.desc
                    
                must = []
                if not (len(y.must) == 0):
                    must = y.must
                    
                may = []
                if not (len(y.may) == 0):
                    may = y.may
                    
                self.OBJECTCLASSES[name] = {"DESC": desc, "MUST": must, "MAY": may}

            oidList = schema.listall(ldap.schema.AttributeType)
            
            for x in oidList:
                environment.updateUI()
                y = schema.get_obj(ldap.schema.AttributeType, x)
                name = y.names
                desc = ""
                
                if not (y.desc == None):
                    desc = y.desc
                    
                single = y.single_value
                
                for z in name:
                    self.ATTRIBUTELIST[z] = {"DESC": desc, "SINGLE": single, "SYNTAX": y.syntax}
                    
                    
        except ldap.LDAPError, e:
            print "Error during LDAP request"
            print "Reason: " + str(e)
            
        environment.setBusy(0)

###############################################################################

    def setServer(self, server):
        """ Set the server from which we want to get the infos.
        """
        
        self.SERVER = server[:]

###############################################################################

    def update(self):
        """ Re-read all informations.
        """
        
        self.OBJECTCLASSES = {}
        self.ATTRIBUTELIST = []
        self.retrieveInfoFromServer()

###############################################################################

    def getAllAttributes(self, classList = None):
        """ Return two sets of all attributes which the server supports.
        """
        must = Set()
        may = Set()
        
        for x in classList:
            if not (x in self.OBJECTCLASSES):
                continue
            must = must.union(Set(self.OBJECTCLASSES[x]["MUST"]))
            may = may.union(Set(self.OBJECTCLASSES[x]["MAY"]))
           
        return must, may

###############################################################################

    def getAllMusts(self, classList = None):
        """ Returns a set of all attributes which are needed by the 
        objectclasses given by classList.
        """
        
        must = Set()
        
        for x in classList:
            must = must.union(Set(self.OBJECTCLASSES[x]["MUST"]))
            
        return must

###############################################################################

    def getAllMays(self, classList = None):
        """ Returns a set of all attributes which are optional for the 
        objectclasses given by classList.
        """
        
        may = Set()
        
        for x in classList:
            may = may | Set(self.OBJECTCLASSES[x]["MAY"])
            
        return may

###############################################################################
    def getAllObjectclassesForAttr(self,attribute=""):
        """ Returns two sets of objectclasses that either MUST
            or MAY use a given attribute
        """
        must = Set()
        may = Set()
        
        if not attribute in self.ATTRIBUTELIST:
            raise UnknownAttribute, attribute
            
        for (key,value) in self.OBJECTCLASSES.items():
            if attribute in value['MUST']:
                must.add(key)
                
            if attribute in value['MAY']:
                may.add(key)
              
        return must, may

        
###############################################################################

    def isSingle(self, attribute = ""):
        """ Check if a attribute must be single.
        """
        
        if attribute in self.ATTRIBUTELIST:
            return self.ATTRIBUTELIST[attribute]["SINGLE"]
        else:
            return False

###############################################################################

    def isMust(self, attribute="", objectClasses = None):
        """ Check if the given attribute must be set.
        """
        
        if objectClasses == None:
            raise "Missing Arguments to Funktion 'isMust(attribute, objectClasses)"
            
        else:
            for x in objectClasses:
                if attribute in self.OBJECTCLASSES[x]["MUST"]:
                    return True
                    
        return False
        
###############################################################################

    def isBinary(self, attribute=""):
        """ Check if the given attribute has binary values.
        """
        
        retVal = False
    
        if attribute in self.ATTRIBUTELIST:
            syntax = self.ATTRIBUTELIST[attribute]["SYNTAX"]
            if syntax in ldap.schema.NOT_HUMAN_READABLE_LDAP_SYNTAXES : 
                retVal = True
            
        return retVal

###############################################################################

    def hasObjectClass(self, objectClass):
        if objectClass in self.OBJECTCLASSES.keys():
            return True
        else:
            return False









