# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinDesign.ui'
#
# Created: Thu Feb 10 14:38:15 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(551, 542)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mainStack = QtGui.QStackedWidget(self.centralwidget)
        self.mainStack.setGeometry(QtCore.QRect(10, 9, 531, 501))
        self.mainStack.setObjectName(_fromUtf8("mainStack"))
        self.page = QtGui.QWidget(self.mainStack)
        self.page.setObjectName(_fromUtf8("page"))
        self.mainStack.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuLanguage = QtGui.QMenu(self.menuEdit)
        self.menuLanguage.setObjectName(_fromUtf8("menuLanguage"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionShowLogger = QtGui.QAction(MainWindow)
        self.actionShowLogger.setObjectName(_fromUtf8("actionShowLogger"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionEditServerList = QtGui.QAction(MainWindow)
        self.actionEditServerList.setObjectName(_fromUtf8("actionEditServerList"))
        self.actionReloadPlugins = QtGui.QAction(MainWindow)
        self.actionReloadPlugins.setObjectName(_fromUtf8("actionReloadPlugins"))
        self.actionConfigurePlugins = QtGui.QAction(MainWindow)
        self.actionConfigurePlugins.setObjectName(_fromUtf8("actionConfigurePlugins"))
        self.actionAboutLuma = QtGui.QAction(MainWindow)
        self.actionAboutLuma.setObjectName(_fromUtf8("actionAboutLuma"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionDeutch = QtGui.QAction(MainWindow)
        self.actionDeutch.setCheckable(True)
        self.actionDeutch.setObjectName(_fromUtf8("actionDeutch"))
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        self.actionEnglish.setObjectName(_fromUtf8("actionEnglish"))
        self.actionNorwegian = QtGui.QAction(MainWindow)
        self.actionNorwegian.setCheckable(True)
        self.actionNorwegian.setObjectName(_fromUtf8("actionNorwegian"))
        self.menuFile.addAction(self.actionShowLogger)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuLanguage.addSeparator()
        self.menuLanguage.addAction(self.actionSettings)
        self.menuEdit.addAction(self.actionEditServerList)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionReloadPlugins)
        self.menuEdit.addAction(self.actionConfigurePlugins)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuLanguage.menuAction())
        self.menuHelp.addAction(self.actionAboutLuma)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.mainStack.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionAboutLuma, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showAboutLuma)
        QtCore.QObject.connect(self.actionConfigurePlugins, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.configurePlugins)
        QtCore.QObject.connect(self.actionReloadPlugins, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.reloadPlugins)
        QtCore.QObject.connect(self.actionShowLogger, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showLoggerWindow)
        QtCore.QObject.connect(self.actionEditServerList, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showServerEditor)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("destroyed()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Luma", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLanguage.setTitle(QtGui.QApplication.translate("MainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowLogger.setText(QtGui.QApplication.translate("MainWindow", "Show Logger", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShowLogger.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditServerList.setText(QtGui.QApplication.translate("MainWindow", "Server List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditServerList.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReloadPlugins.setText(QtGui.QApplication.translate("MainWindow", "Reload Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReloadPlugins.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurePlugins.setText(QtGui.QApplication.translate("MainWindow", "Configure Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutLuma.setText(QtGui.QApplication.translate("MainWindow", "About Luma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutLuma.setShortcut(QtGui.QApplication.translate("MainWindow", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeutch.setText(QtGui.QApplication.translate("MainWindow", "Deutch", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnglish.setText(QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNorwegian.setText(QtGui.QApplication.translate("MainWindow", "Norwegian", None, QtGui.QApplication.UnicodeUTF8))

