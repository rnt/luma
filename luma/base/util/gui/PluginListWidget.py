# -*- coding: utf-8 -*-

from PyQt4.QtCore import QSize
from PyQt4.QtGui import QWidget, QListView
from base.util.gui.PluginListWidgetDesign import Ui_pluginListWidget
from base.util.model.PluginListWidgetModel import PluginListWidgetModel

import sys
import logging

class PluginListWidget(QWidget, Ui_pluginListWidget):
    """
    Used by mainwin to show the list of plugins that can be loaded
    
    Parent is given to the model, because it is going to contain not only
    the QStandardItems but the widget for each item, that requires a parent.
    """
    __logger = logging.getLogger(__name__)
    
    def __init__(self, parent):
        QWidget.__init__(self, None)
        #dont change None to self in parent
        
        self.parent = parent
        self.setupUi(self)
        
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setViewMode(QListView.IconMode)
        self.listView.setModel(PluginListWidgetModel(self.parent))
        
    def pluginDoubleClicked(self, index):
        if self.parent and hasattr(self.parent, "pluginSelected"):
            self.parent.pluginSelected(self.listView.model().itemFromIndex(index))
        else:
            self.__logger.error("Cannot enter a plugin when no parent is given to PluginListWidget")       
    
    def updatePlugins(self):
        """
        Updates the listview with new plugins
        """
        self.listView.reset()
        self.listView.setModel(PluginListWidgetModel(self.parent))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
