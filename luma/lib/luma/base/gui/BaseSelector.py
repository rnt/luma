###########################################################################
#    Copyright (C) 2003 by Wido Depping                                      
#    <wido.depping@tu-clausthal.de>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from qt import *
from base.gui.BaseSelectorDesign import BaseSelectorDesign


class BaseSelector(BaseSelectorDesign):

    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        BaseSelectorDesign.__init__(self,parent,name,modal,fl)

###############################################################################

    def setList(self, dnList=None):
        if not (dnList==None):
            for x in dnList:
                self.dnBox.insertItem(x)
