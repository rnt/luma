# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2003, 2004 by Wido Depping                                      
#    <widod@users.sourceforge.net>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from qt import *
from base.gui.BaseSelectorDesign import BaseSelectorDesign


class BaseSelector(BaseSelectorDesign):
    """ A class for selection a DN from a combobox.
    """

    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        BaseSelectorDesign.__init__(self,parent,name,modal,fl)

###############################################################################

    def setList(self, dnList):
        """ Fill the combobox with possible baseDNs specified by dnList.
        """
        
        if not (type(dnList) == list):
            raise TypeError

        map(self.dnBox.insertItem, dnList)
