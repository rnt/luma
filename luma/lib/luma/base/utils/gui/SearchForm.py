###########################################################################
#    Copyright (C) 2003 by Wido Depping
#    <wido.depping@tu-clausthal.de>
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from qt import *
import ldap
import re

from base.utils.gui.SearchFormDesign import SearchFormDesign
from base.utils.gui.FilterWizard import FilterWizard
from base.backend.ServerObject import ServerObject
from base.backend.ServerList import ServerList
from base.backend.DirUtils import DirUtils
from base.backend.LumaConnection import LumaConnection

class SearchForm(SearchFormDesign):

    def __init__(self,parent = None,name = None,fl = 0):
        SearchFormDesign.__init__(self,parent,name,fl)

        tmpFile  = DirUtils().PREFIX + "/share/luma/icons/secure.png"
        securePixmap = QPixmap(tmpFile)

        self.serverListObject = ServerList()
        self.serverListObject.readServerList()
        self.serverList = self.serverListObject.SERVERLIST
        
        if not (self.serverList == None):
            for x in self.serverList:
                if int(x.tls):
                    self.serverBox.insertItem(securePixmap, x.name)
                else:
                    self.serverBox.insertItem(x.name)

        self.init_filter_bookmarks()

        self.searchEdit.installEventFilter(self)

###############################################################################

    def start_search(self):
        parentObject = self
        while  parentObject.parentWidget():
            parentObject = parentObject.parentWidget()
        tmpStatusBar = parentObject.statusBar()

        liste = self.__get_search_criteria()
        server = str(self.serverBox.currentText())
        serverMeta = self.serverListObject.get_serverobject(server)
        

        conObject = LumaConnection(serverMeta)
        searchResult = conObject.search(serverMeta.baseDN, ldap.SCOPE_SUBTREE,
                str(self.searchEdit.currentText()))

        self.emit(PYSIGNAL("ldap_result"), (serverMeta.name, searchResult,liste, ))

###############################################################################

    def start_filter_wizard(self):
        server = str(self.serverBox.currentText())
        if self.serverList == None:
            print "Warning: Please set up some servers to connect to."
            return
            
        serverMeta = self.serverListObject.get_serverobject(server)
            
        dialog = FilterWizard(server)
        dialog.exec_loop()
        self.init_filter_bookmarks()
        self.searchEdit.setCurrentText(dialog.searchFilterEdit.text())


###############################################################################

    def init_filter_bookmarks(self):
        bookmarkFile = DirUtils().USERDIR + "/.luma/filterBookmarks"
        try:
            fileHandler = open(bookmarkFile, 'r')
            text = fileHandler.readlines()
            fileHandler.close()
            self.searchEdit.clear()
            for x in text:
                self.searchEdit.insertItem(x[:-1])
        except:
            print "Bookmark loading failed"

###############################################################################

    def __get_search_criteria(self):
        filterString = str(self.searchEdit.currentText())
        filterPattern = re.compile("\(\w*=")
        tmpList = filterPattern.findall(filterString)
        endList = []
        for x in tmpList:
            endList.append(x[1:-1])
        return endList

###############################################################################

    def eventFilter(self, object, event):
        if (event.type() == QEvent.KeyRelease):
            if (event.key() == Qt.Key_Return):
                self.start_search()
        return 0

