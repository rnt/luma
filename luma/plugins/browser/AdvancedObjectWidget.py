# -*- coding: utf-8 -*-
#
# Copyright (c) 2011
#     Per Ove Ringdal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
import ldap
import copy
import logging
import os

from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtCore import QSize, SIGNAL, QString, pyqtSlot
from PyQt4.QtGui import (QTextBrowser, QTextOption, QPixmap, QSizePolicy,
                         QTextOption, QLineEdit, QToolBar, QImage,
                         QMessageBox, QVBoxLayout, QWidget, QToolButton,
                         QIcon, QComboBox, QInputDialog, QDialog, QFileDialog)

from base.backend.SmartDataObject import SmartDataObject
from base.backend.ObjectClassAttributeInfo import ObjectClassAttributeInfo
from base.util.IconTheme import pixmapFromTheme
from base.util.Paths import getLumaRoot

from .model.EntryModel import EntryModel
from .HtmlParser import HtmlParser
from .TemplateFactory import TemplateFactory
from .editors.EditorFactory import getEditorWidget
from .AddAttributeWizard import AddAttributeWizard

class AdvancedObjectWidget(QWidget):

    def __init__(self, index, currentTemplate="classic.html", parent=None, entryTemplate = None):
        QWidget.__init__(self, parent)

        w = 24
        h = 24
        self.entryModel = None

        # Standard pixmaps used by the widget
        self.reloadPixmap = pixmapFromTheme(
            "view-refresh", ":/icons/32/view-refresh", w, h)
        self.savePixmap = pixmapFromTheme(
            "document-save", ":/icons/32/document-save",w, h)
        self.addPixmap = pixmapFromTheme(
            "list-add", ":/icons/32/list-add", w, h)
        self.deleteSmallPixmap = pixmapFromTheme(
            "list-remove", ":/icons/32/list-remove", w, h)

        self.treeIndex = index

        self.setLayout(QVBoxLayout(self))
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # create the widget containing the data
        self.textBrowser = QTextBrowser()
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setWordWrapMode(QTextOption.WrapAnywhere)
        self.layout().addWidget(self.textBrowser)
        self.textBrowser.anchorClicked.connect(self.anchorClicked)

        self.currentDocument = ''
        self.addingToComboBox = False

        # create the combobox containing the different views
        self.comboBox = QComboBox()
        self.currentTemplate = currentTemplate
        self.errorTemplate = "error.html"
        self.usedTemplates = []
        # FIXED: Need a more robust way for locating the path used in
        #        the TemplateFactory for locating the template view
        #        files
        # >>>    with base.util.Paths.getLumaRoot this should work.
        #        Probably needs some validation testing on platforms
        #        other than Linux
        # Another issue occured when running Luma after a installation
        # from a source distribution. Because the site-packages is only
        # intended for pure python modules, the html templates is not
        # installed, resulting in an Exception when trying to view an
        # entry in the Browser plugin. The setup.py script is modified
        # such that the needed html templates is copied into a folder
        # in the path returned by `base.util.Paths.getConfigPrefix`.
        s = QtCore.QSettings()
        configPrefix = s.value('application/config_prefix').toString()
        templatesPath = os.path.join(unicode(configPrefix).encode('utf-8'),
                                     'browser-templates')
        # If we run Luma from a development environment the isntalled
        # templatesPath do most likely not exist. We therefore use the
        # directory in the repository
        if not os.path.isdir(templatesPath):
            templatesPath = unicode(
                os.path.join(
                    getLumaRoot(), 'plugins', 'browser', 'templates')
            )

        self.templateFactory = TemplateFactory(templatesPath)

        self.htmlParser = HtmlParser(self.textBrowser)

        self.str_RELOAD= QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Reload")
        self.str_SAVE = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Save entry")
        self.str_SAVE_CONTINUE = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Do you want to save the entry before continuing?")
        self.str_SAVE_FAILED = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Saving failed, continue anyway?")
        self.str_DELETE = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Delete object")
        self.str_DELETE_CONFIRM = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Do you really want to delete the object?")
        self.str_ADD = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Add attribute")
        self.str_SWITCH_VIEWS = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Switch between views")
        self.str_REASON = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Reason:")
        self.str_EXPORT_BINARY = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Export binary attribute to file")
        self.str_EXPORT_BINARY_EXCEPT = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Could not export binary data to file.")
        self.str_SELECT_ANOTHER_FILE = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Please select another filename.")
        self.str_NO_TEMPLATE = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "No templates available")
        self.str_MISSING_ENTRY = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "Did'nt receive a ldap-object, it might have been deleted")
        self.str_ENTRY_INVALID = QtCore.QCoreApplication.translate("AdvancedObjectWidget",
            "The ldap object is not valid\nClick Yes to view the object anyway\nNo to view the errors \nIgnore to view the object and ignore this message in later attempts.")

        self.buildToolBar()

###############################################################################

    @staticmethod
    def smartObjectCopy(smartObject):
        return SmartDataObject(copy.deepcopy([smartObject.dn, smartObject.data]), copy.deepcopy(smartObject.serverMeta))

###############################################################################

    def getSmartObject(self):
        return self.entryModel.getSmartObject()

###############################################################################

    def initModel(self, smartObject, create=False, entryTemplate = None):
        """ sets up the model, and connects it to this object
        """
        if not create:
            # use a copy of the smartObject
            smartObject = AdvancedObjectWidget.smartObjectCopy(smartObject)
        self.baseDN = smartObject.getDN()
        self.entryModel = EntryModel(smartObject, self, entryTemplate)
        self.htmlParser.setModel(self.entryModel)
        self.entryModel.modelChangedSignal.connect(self.modelChanged)
        success, exceptionMsg, exceptionObject = self.entryModel.initModel(create)
        if not success:
            errorMsg = "%s<br><br>%s: %s" % (exceptionMsg, self.str_REASON, str(exceptionObject))
            QMessageBox.critical(self,
                                self.trUtf8(""),
                                self.trUtf8(errorMsg))

###############################################################################

    def loadTemplates(self):
        """ Loads all templates that matches with the current objectclasses
        """
        self.usedTemplates = []
        objectClasses = self.getSmartObject().getObjectClasses()
        newIndex = -1
        i = 0
        for objectClass, fileName in self.templateFactory.getTemplateList():
            if objectClass == '' or objectClass in objectClasses:
                if fileName == self.currentTemplate:
                    newIndex = i
                self.usedTemplates.append(fileName)
                i += 1
        if newIndex == -1:
            newIndex = 0
        self.currentTemplate = self.usedTemplates[newIndex]
        #TODO do this properly, signals ignored
        self.addingToComboBox = True
        self.comboBox.clear()
        self.comboBox.addItems(self.usedTemplates)
        self.comboBox.setCurrentIndex(newIndex)
        self.addingToComboBox = False


###############################################################################

    @pyqtSlot(bool)
    def modelChanged(self, reload):
        if reload:
            item = None
            if self.treeIndex and self.treeIndex.isValid():
                row = self.treeIndex.row()
                column = self.treeIndex.column()
                # QPersistenIndex doesn't have internalPointer()
                # so we aquire a QModelIndex which does
                item = self.treeIndex.sibling(row,column).internalPointer()
            if not(self.entryModel.VALID):
                if item == None or not(item.serverParent.ignoreItemErrors):
                    result = QMessageBox.question(self,
                                        self.trUtf8(""),
                                        self.str_ENTRY_INVALID,
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore,
                                        QMessageBox.No)
                    if result == QMessageBox.No:
                        self.currentTemplate = self.errorTemplate
                    elif result == QMessageBox.Ignore:
                        if not(item == None):
                            item.serverParent.ignoreItemErrors = True
        self.displayValues()

###############################################################################

    def displayValues(self):
        # Something went wrong. We have no data object.
        # This might happen if we want to refresh an item and
        # it might be deleted already.
        if None == self.entryModel.getSmartObject():
            QMessageBox.critical(self, self.str_MISSING_ENTRY)
            self.enableToolButtons(False)
            return

        self.loadTemplates()
        if self.currentTemplate == None:
            selt.textBrowser.setHtml(self.str_NO_TEMPLATE)
            return
        htmlTemplate = self.templateFactory.getTemplateFile(self.currentTemplate)
        self.currentDocument = self.htmlParser.parseHtml(htmlTemplate)
        self.textBrowser.setHtml(self.currentDocument)

        self.enableToolButtons(True)

###############################################################################

    def enableToolButtons(self, enable):
        if None == self.entryModel:
            self.saveButton.setEnabled(False)
            self.deleteObjectButton.setEnabled(False)
            self.reloadButton.setEnabled(True)
            self.addAttributeButton.setEnabled(False)
            return
        if self.entryModel.EDITED and not self.entryModel.CREATE:
            self.saveButton.setEnabled(enable)
        else:
            self.saveButton.setEnabled(False)

        if self.entryModel.ISLEAF:
            self.deleteObjectButton.setEnabled(enable)
        else:
            self.deleteObjectButton.setEnabled(False)

        if self.entryModel.CREATE:
            self.reloadButton.setEnabled(False)
        else:
            self.reloadButton.setEnabled(enable)

        self.addAttributeButton.setEnabled(enable)



###############################################################################

    def buildToolBar(self):
        self.toolBar = QToolBar()
        self.toolBar.layout().setContentsMargins(0, 0, 0, 0)

        # Reload button
        self.reloadButton = QToolButton(self.toolBar)
        self.reloadButton.setIcon(QIcon(self.reloadPixmap))
        self.reloadButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.reloadButton.setAutoRaise(True)
        self.reloadButton.setBackgroundRole(self.backgroundRole())
        self.reloadButton.setToolTip(self.str_RELOAD)
        self.connect(self.reloadButton, SIGNAL("clicked()"), self.refreshView)
        self.toolBar.addWidget(self.reloadButton)


        # Save button
        self.saveButton = QToolButton(self.toolBar)
        self.saveButton.setIcon(QIcon(self.savePixmap))
        self.saveButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.saveButton.setAutoRaise(True)
        self.saveButton.setBackgroundRole(self.backgroundRole())
        self.saveButton.setToolTip(self.str_SAVE)
        self.connect(self.saveButton, SIGNAL("clicked()"), self.saveObject)
        self.toolBar.addWidget(self.saveButton)

        self.toolBar.addSeparator()

        # Add attribute button
        self.addAttributeButton = QToolButton(self.toolBar)
        self.addAttributeButton.setIcon(QIcon(self.addPixmap))
        self.addAttributeButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.addAttributeButton.setAutoRaise(True)
        self.addAttributeButton.setBackgroundRole(self.backgroundRole())
        self.addAttributeButton.setToolTip(self.str_ADD)
        self.connect(self.addAttributeButton, SIGNAL("clicked()"), self.addAttribute)
        self.toolBar.addWidget(self.addAttributeButton)

        # Delete button
        self.deleteObjectButton = QToolButton(self.toolBar)
        self.deleteObjectButton.setIcon(QIcon(self.deleteSmallPixmap))
        self.deleteObjectButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.deleteObjectButton.setAutoRaise(True)
        self.deleteObjectButton.setBackgroundRole(self.backgroundRole())
        self.deleteObjectButton.setToolTip(self.str_DELETE)
        self.connect(self.deleteObjectButton, SIGNAL("clicked()"), self.deleteObject)
        self.toolBar.addWidget(self.deleteObjectButton)

        self.comboBox.setToolTip(self.str_SWITCH_VIEWS)
        self.connect(self.comboBox, SIGNAL("currentIndexChanged(int)"), self.changeView)
        self.toolBar.addWidget(self.comboBox)

        self.enableToolButtons(False)
        self.layout().insertWidget(0, self.toolBar)

###############################################################################

    @pyqtSlot("int")
    def changeView(self, index):
        """
        change between different views
        """
        if index == -1 or self.addingToComboBox:
            return
        self.currentTemplate = self.usedTemplates[index]
        self.displayValues()

###############################################################################

    def aboutToChange(self):
        """
        Asks the user whether changes should be saved
        returns True if changes were saved, or discarded
        """
        if not self.entryModel.EDITED:
            return True

        result = QMessageBox.warning(self,
            self.str_SAVE,
            self.str_SAVE_CONTINUE,
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Cancel)


        # TODO add exception message
        if result == QMessageBox.Save:
            if not self.saveObject():
                # Saving failed
                result = QMessageBox.question(None,
                            self.trUtf8(""),
                            self.str_SAVE_FAILED,
                            QMessageBox.Ok | QMessageBox.Cancel,
                            QMessageBox.Cancel)
        return not(result == QMessageBox.Cancel)

###############################################################################

    # TODO: add logging for each error
    @pyqtSlot()
    def refreshView(self):
        """ Refreshes the LDAP data from server and displays values.
        """
        if self.aboutToChange():
            success, exceptionMsg, exceptionObject = self.entryModel.reloadModel()
            if not success:
                errorMsg = "%s<br><br>%s: %s" % (exceptionMsg, self.str_REASON, str(exceptionObject))
                QMessageBox.critical(self, self.trUtf8(""), self.trUtf8(errorMsg))
            else:
                self.displayValues()

###############################################################################

    # TODO: add logging for each error
    @pyqtSlot()
    def saveObject(self):
        success, exceptionMsg, exceptionObject = self.entryModel.saveModel()
        if not success:
            # Saving failed
            errorMsg = "%s<br><br>%s: %s" % (exceptionMsg, self.str_REASON, str(exceptionObject))

            QMessageBox.critical(self, self.trUtf8(""), self.trUtf8(errorMsg))
            return False
        else:
            # update the smartObject in the tree
            if self.entryModel.CREATE:
                pass
            elif self.treeIndex and self.treeIndex.isValid():
                row = self.treeIndex.row()
                column = self.treeIndex.column()
                # QPersistenIndex doesn't have internalPointer()
                # so we aquire a QModelIndex which does
                index = self.treeIndex.sibling(row,column)
                index.internalPointer().itemData = self.getSmartObject()
            return True

###############################################################################

    @pyqtSlot()
    def addAttribute(self):
        """ Add attributes to the current object.
        """

        dialog = AddAttributeWizard(self)
        dialog.setData(self.smartObjectCopy(self.entryModel.getSmartObject()))

        dialog.exec_()

        if dialog.result() == QDialog.Rejected:
            return

        attribute = str(dialog.attributeBox.currentText())
        showAll = dialog.enableAllBox.isChecked()
        if dialog.binaryBox.isChecked():
            attributeSet = set([attribute + ";binary"])
        else:
            attributeSet = set([attribute])

        if showAll and not(attribute.lower() in dialog.possibleAttributes):
            objectClass = str(dialog.classBox.currentItem().text())
            self.entryModel.addObjectClass(objectClass)

            serverSchema = ObjectClassAttributeInfo(self.entryModel.smartObject.getServerMeta())
            mustAttributes = serverSchema.getAllMusts([objectClass])
            mustAttributes = mustAttributes.difference(set(self.entryModel.smartObject.getAttributeList()))
            attributeSet = mustAttributes.union(set([attribute]))

        for x in attributeSet:
            self.entryModel.addAttributeValue(x, None)

        self.displayValues()


###############################################################################

    # TODO: add logging for each error, remove tab and node from parent
    @pyqtSlot()
    def deleteObject(self):
        buttonClicked = QMessageBox.critical(self,
                            self.str_DELETE,
                            self.str_DELETE_CONFIRM,
                            QMessageBox.Yes,
                            QMessageBox.No)
        if not (buttonClicked == QMessageBox.Yes):
            return
        # If we have an index, use it tell the item to delete itself
        # so that the view is updated
        if self.treeIndex and self.treeIndex.isValid():
            row = self.treeIndex.row()
            column = self.treeIndex.column()
            # QPersistenIndex doesn't have internalPointer()
            # so we aquire a QModelIndex which does
            index = self.treeIndex.sibling(row,column)
            success, message = index.model().deleteItem(index)
            if success:
                self.enableToolButtons(False)
                self.deleteLater()
            else:
                errorMsg = "%s" % (message)
                QMessageBox.critical(self, self.trUtf8(""), self.trUtf8(errorMsg))
        # if not, we just delete it ourselves since there's not view on the object
        else:
            success, message, exceptionObject = self.entryModel.deleteObject()
            if success:
                self.enableToolButtons(False)
                self.deleteLater()
            else:
                errorMsg = "%s<br><br>%s: %s" % (message, self.str_REASON, str(exceptionObject))
                QMessageBox.critical(self, self.trUtf8(""), self.trUtf8(errorMsg))

###############################################################################

    @pyqtSlot("QUrl")
    def anchorClicked(self, url):
        """ Called when an anchor (<a href=".." /> is clicked
        """
        nameString = unicode(url.toString())
        tmpList = nameString.split("__")

        if tmpList[0] in self.entryModel.getSmartObject().getObjectClasses():
            self.entryModel.deleteObjectClass(tmpList[0])
        else:
            if not len(tmpList) == 3:
                return
            attributeName, index, operation = tmpList[0], int(tmpList[1]), tmpList[2]
            if operation == "edit":
                self.editAttribute(attributeName, index)
            elif operation == "delete":
                self.deleteAttribute(attributeName, index)
            elif operation == "export":
                self.exportAttribute(attributeName, index)

###############################################################################

    def editAttribute(self, attributeName, index):
        smartObject = self.entryModel.getSmartObject()
        oldDN = smartObject.getDN()

        addAttribute = False
        if attributeName == 'RDN':
            # TODO correct this, used on creation?
            oldValue = oldDN
            smartObject.setDN(self.baseDN)
        else:
            if smartObject.hasAttribute(attributeName):
                addValue = False
                oldValue = smartObject.getAttributeValue(attributeName, index)
                if oldValue == None:
                    oldValue = ''
            else:
                addValue = True
                oldValue = ''
        dialog = getEditorWidget(self, smartObject, attributeName, index)
        dialog.exec_()

        if dialog.result() == QDialog.Accepted:
            # TODO check attribute types
            newValue = dialog.getValue()
            if not (newValue == None):
                if attributeName == 'RDN':
                    self.entryModel.setDN(newValue)
                    if dialog.addAttributeBox.isChecked():
                        addAttribute = unicode(dialog.attributeBox.currentText())
                        addValue = unicode(dialog.valueEdit.text())
                        self.entryModel.addAttributeValue(addAttribute, [addValue])
                else:
                    if addValue:
                        self.entryModel.addAttributeValue(attributeName, [newValue])
                    else:
                        self.entryModel.editAttribute(attributeName, index, newValue)
        else:
            if attributeName == 'RDN':
                smartObject.setDN(oldDN.decode('utf-8'))

###############################################################################

    def deleteAttribute(self, attributeName, index):
        self.entryModel.deleteAttribute(attributeName, index)

###############################################################################

    def exportAttribute(self, attributeName, index):
        """ Show the dialog for exporting binary attribute data.
        """
        value = self.getSmartObject().getAttributeValue(attributeName, index)


        fileName = unicode(QFileDialog.getSaveFileName(\
                            self,
                            self.str_EXPORT_BINARY,
                            QString(""),
                            "All files (*)",
                            None))

        if unicode(fileName) == "":
            return

        try:
            fileHandler = open(fileName, "w")
            fileHandler.write(value)
            fileHandler.close()
            SAVED = True
        except IOError, e:
            msg = "%s %s:\n\n%s\n\n%s" % (self.str_EXPORT_BINARY_EXCEPT,
                                          self.str_REASON,
                                          str(e),
                                          self.str_SELECT_ANOTHER_FILE)
            result = QMessageBox.warning(\
                    self,
                    self.str_EXPORT_BINARY,
                    msg,
                    QMessageBox.Cancel | QMessageBox.Ok,
                    QMessageBox.Cancel)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
