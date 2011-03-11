# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/debris/devel/git/luma-playground/resources/forms/LoggerWidgetDesign.ui'
#
# Created: Fri Mar 11 18:09:59 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LoggerWidget(object):
    def setupUi(self, LoggerWidget):
        LoggerWidget.setObjectName("LoggerWidget")
        LoggerWidget.resize(516, 217)
        LoggerWidget.setWindowTitle("")
        self.vboxlayout = QtGui.QVBoxLayout(LoggerWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.messageEdit = QtGui.QTextEdit(LoggerWidget)
        self.messageEdit.setReadOnly(True)
        self.messageEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.messageEdit.setObjectName("messageEdit")
        self.vboxlayout.addWidget(self.messageEdit)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1 = QtGui.QLabel(LoggerWidget)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.hboxlayout.addWidget(self.textLabel1)
        self.errorBox = QtGui.QCheckBox(LoggerWidget)
        self.errorBox.setChecked(True)
        self.errorBox.setObjectName("errorBox")
        self.hboxlayout.addWidget(self.errorBox)
        self.debugBox = QtGui.QCheckBox(LoggerWidget)
        self.debugBox.setChecked(True)
        self.debugBox.setObjectName("debugBox")
        self.hboxlayout.addWidget(self.debugBox)
        self.infoBox = QtGui.QCheckBox(LoggerWidget)
        self.infoBox.setChecked(True)
        self.infoBox.setObjectName("infoBox")
        self.hboxlayout.addWidget(self.infoBox)
        spacerItem = QtGui.QSpacerItem(141, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.clearButton = QtGui.QToolButton(LoggerWidget)
        self.clearButton.setAutoRaise(True)
        self.clearButton.setObjectName("clearButton")
        self.hboxlayout.addWidget(self.clearButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(LoggerWidget)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked()"), LoggerWidget.clearLogger)
        QtCore.QObject.connect(self.debugBox, QtCore.SIGNAL("stateChanged(int)"), LoggerWidget.rebuildLog)
        QtCore.QObject.connect(self.errorBox, QtCore.SIGNAL("stateChanged(int)"), LoggerWidget.rebuildLog)
        QtCore.QObject.connect(self.infoBox, QtCore.SIGNAL("stateChanged(int)"), LoggerWidget.rebuildLog)
        QtCore.QMetaObject.connectSlotsByName(LoggerWidget)

    def retranslateUi(self, LoggerWidget):
        self.textLabel1.setText(QtGui.QApplication.translate("LoggerWidget", "Display message types:", None, QtGui.QApplication.UnicodeUTF8))
        self.errorBox.setText(QtGui.QApplication.translate("LoggerWidget", "Errors", None, QtGui.QApplication.UnicodeUTF8))
        self.debugBox.setText(QtGui.QApplication.translate("LoggerWidget", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.infoBox.setText(QtGui.QApplication.translate("LoggerWidget", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setToolTip(QtGui.QApplication.translate("LoggerWidget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("LoggerWidget", "Clear log", None, QtGui.QApplication.UnicodeUTF8))

