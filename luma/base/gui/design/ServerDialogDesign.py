# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Skole\it2901\resources\forms\ServerDialogDesign.ui'
#
# Created: Thu May 05 14:02:38 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ServerDialogDesign(object):
    def setupUi(self, ServerDialogDesign):
        ServerDialogDesign.setObjectName(_fromUtf8("ServerDialogDesign"))
        ServerDialogDesign.resize(607, 434)
        ServerDialogDesign.setMinimumSize(QtCore.QSize(550, 350))
        self.vboxlayout = QtGui.QVBoxLayout(ServerDialogDesign)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.splitter = QtGui.QSplitter(ServerDialogDesign)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layout3 = QtGui.QWidget(self.splitter)
        self.layout3.setObjectName(_fromUtf8("layout3"))
        self.serverListGrid = QtGui.QGridLayout(self.layout3)
        self.serverListGrid.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.serverListGrid.setMargin(0)
        self.serverListGrid.setMargin(0)
        self.serverListGrid.setObjectName(_fromUtf8("serverListGrid"))
        self.serverListView = QtGui.QListView(self.layout3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverListView.sizePolicy().hasHeightForWidth())
        self.serverListView.setSizePolicy(sizePolicy)
        self.serverListView.setObjectName(_fromUtf8("serverListView"))
        self.serverListGrid.addWidget(self.serverListView, 0, 0, 1, 2)
        self.addButton = QtGui.QPushButton(self.layout3)
        self.addButton.setAutoDefault(True)
        self.addButton.setDefault(False)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.serverListGrid.addWidget(self.addButton, 1, 0, 1, 1)
        self.deleteButton = QtGui.QPushButton(self.layout3)
        self.deleteButton.setAutoDefault(True)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.serverListGrid.addWidget(self.deleteButton, 1, 1, 1, 1)
        self.testConnectionButton = QtGui.QPushButton(self.layout3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testConnectionButton.sizePolicy().hasHeightForWidth())
        self.testConnectionButton.setSizePolicy(sizePolicy)
        self.testConnectionButton.setObjectName(_fromUtf8("testConnectionButton"))
        self.serverListGrid.addWidget(self.testConnectionButton, 2, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(48, 48))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.networkTab = QtGui.QWidget()
        self.networkTab.setObjectName(_fromUtf8("networkTab"))
        self.gridlayout = QtGui.QGridLayout(self.networkTab)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.networkIcon = QtGui.QLabel(self.networkTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkIcon.sizePolicy().hasHeightForWidth())
        self.networkIcon.setSizePolicy(sizePolicy)
        self.networkIcon.setMinimumSize(QtCore.QSize(48, 48))
        self.networkIcon.setText(_fromUtf8(""))
        self.networkIcon.setObjectName(_fromUtf8("networkIcon"))
        self.gridlayout.addWidget(self.networkIcon, 0, 0, 1, 1)
        self.networkOptGrid = QtGui.QGridLayout()
        self.networkOptGrid.setObjectName(_fromUtf8("networkOptGrid"))
        self.networkGroup = QtGui.QGroupBox(self.networkTab)
        self.networkGroup.setObjectName(_fromUtf8("networkGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.networkGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.networkGrid = QtGui.QGridLayout()
        self.networkGrid.setObjectName(_fromUtf8("networkGrid"))
        self.hostLabel = QtGui.QLabel(self.networkGroup)
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self.networkGrid.addWidget(self.hostLabel, 0, 0, 1, 1)
        self.hostEdit = QtGui.QLineEdit(self.networkGroup)
        self.hostEdit.setObjectName(_fromUtf8("hostEdit"))
        self.networkGrid.addWidget(self.hostEdit, 0, 1, 1, 1)
        self.portLabel = QtGui.QLabel(self.networkGroup)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.networkGrid.addWidget(self.portLabel, 2, 0, 1, 1)
        self.portSpinBox = QtGui.QSpinBox(self.networkGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portSpinBox.sizePolicy().hasHeightForWidth())
        self.portSpinBox.setSizePolicy(sizePolicy)
        self.portSpinBox.setMaximum(99999)
        self.portSpinBox.setProperty(_fromUtf8("value"), 389)
        self.portSpinBox.setObjectName(_fromUtf8("portSpinBox"))
        self.networkGrid.addWidget(self.portSpinBox, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.networkGrid, 0, 0, 1, 1)
        self.networkOptGrid.addWidget(self.networkGroup, 0, 0, 1, 1)
        self.LDAPGroup = QtGui.QGroupBox(self.networkTab)
        self.LDAPGroup.setObjectName(_fromUtf8("LDAPGroup"))
        self.gridLayout_7 = QtGui.QGridLayout(self.LDAPGroup)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.LDAPGrid = QtGui.QGridLayout()
        self.LDAPGrid.setObjectName(_fromUtf8("LDAPGrid"))
        self.aliasBox = QtGui.QCheckBox(self.LDAPGroup)
        self.aliasBox.setEnabled(False)
        self.aliasBox.setObjectName(_fromUtf8("aliasBox"))
        self.LDAPGrid.addWidget(self.aliasBox, 0, 0, 1, 2)
        self.baseDNBox = QtGui.QCheckBox(self.LDAPGroup)
        self.baseDNBox.setObjectName(_fromUtf8("baseDNBox"))
        self.LDAPGrid.addWidget(self.baseDNBox, 1, 0, 1, 2)
        self.baseDNLabel = QtGui.QLabel(self.LDAPGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseDNLabel.sizePolicy().hasHeightForWidth())
        self.baseDNLabel.setSizePolicy(sizePolicy)
        self.baseDNLabel.setObjectName(_fromUtf8("baseDNLabel"))
        self.LDAPGrid.addWidget(self.baseDNLabel, 2, 0, 1, 1)
        self.baseDNEdit = QtGui.QLineEdit(self.LDAPGroup)
        self.baseDNEdit.setObjectName(_fromUtf8("baseDNEdit"))
        self.LDAPGrid.addWidget(self.baseDNEdit, 2, 1, 1, 1)
        self.hLayout = QtGui.QHBoxLayout()
        self.hLayout.setObjectName(_fromUtf8("hLayout"))
        self.addBaseDNButton = QtGui.QPushButton(self.LDAPGroup)
        self.addBaseDNButton.setAutoDefault(False)
        self.addBaseDNButton.setObjectName(_fromUtf8("addBaseDNButton"))
        self.hLayout.addWidget(self.addBaseDNButton)
        self.deleteBaseDNButton = QtGui.QPushButton(self.LDAPGroup)
        self.deleteBaseDNButton.setAutoDefault(False)
        self.deleteBaseDNButton.setObjectName(_fromUtf8("deleteBaseDNButton"))
        self.hLayout.addWidget(self.deleteBaseDNButton)
        self.LDAPGrid.addLayout(self.hLayout, 3, 1, 1, 1)
        self.baseDNListWidget = QtGui.QListWidget(self.LDAPGroup)
        self.baseDNListWidget.setObjectName(_fromUtf8("baseDNListWidget"))
        self.LDAPGrid.addWidget(self.baseDNListWidget, 4, 0, 1, 2)
        self.gridLayout_7.addLayout(self.LDAPGrid, 0, 0, 1, 1)
        self.networkOptGrid.addWidget(self.LDAPGroup, 1, 0, 1, 1)
        self.gridlayout.addLayout(self.networkOptGrid, 0, 1, 2, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.networkTab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bindOptGroup = QtGui.QGroupBox(self.tab)
        self.bindOptGroup.setObjectName(_fromUtf8("bindOptGroup"))
        self.gridLayout_8 = QtGui.QGridLayout(self.bindOptGroup)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.bindOptGrid = QtGui.QGridLayout()
        self.bindOptGrid.setObjectName(_fromUtf8("bindOptGrid"))
        self.bindAnonBox = QtGui.QCheckBox(self.bindOptGroup)
        self.bindAnonBox.setChecked(True)
        self.bindAnonBox.setObjectName(_fromUtf8("bindAnonBox"))
        self.bindOptGrid.addWidget(self.bindAnonBox, 0, 0, 1, 2)
        self.mechanismLabel = QtGui.QLabel(self.bindOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mechanismLabel.sizePolicy().hasHeightForWidth())
        self.mechanismLabel.setSizePolicy(sizePolicy)
        self.mechanismLabel.setObjectName(_fromUtf8("mechanismLabel"))
        self.bindOptGrid.addWidget(self.mechanismLabel, 1, 0, 1, 1)
        self.mechanismBox = QtGui.QComboBox(self.bindOptGroup)
        self.mechanismBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mechanismBox.sizePolicy().hasHeightForWidth())
        self.mechanismBox.setSizePolicy(sizePolicy)
        self.mechanismBox.setObjectName(_fromUtf8("mechanismBox"))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.mechanismBox.addItem(_fromUtf8(""))
        self.bindOptGrid.addWidget(self.mechanismBox, 1, 1, 1, 1)
        self.bindAsLabel = QtGui.QLabel(self.bindOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bindAsLabel.sizePolicy().hasHeightForWidth())
        self.bindAsLabel.setSizePolicy(sizePolicy)
        self.bindAsLabel.setObjectName(_fromUtf8("bindAsLabel"))
        self.bindOptGrid.addWidget(self.bindAsLabel, 2, 0, 1, 1)
        self.bindAsEdit = QtGui.QLineEdit(self.bindOptGroup)
        self.bindAsEdit.setEnabled(False)
        self.bindAsEdit.setObjectName(_fromUtf8("bindAsEdit"))
        self.bindOptGrid.addWidget(self.bindAsEdit, 2, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.bindOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.bindOptGrid.addWidget(self.passwordLabel, 3, 0, 1, 1)
        self.passwordEdit = QtGui.QLineEdit(self.bindOptGroup)
        self.passwordEdit.setEnabled(False)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.bindOptGrid.addWidget(self.passwordEdit, 3, 1, 1, 1)
        self.gridLayout_8.addLayout(self.bindOptGrid, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.bindOptGroup, 5, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.authIcon = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authIcon.sizePolicy().hasHeightForWidth())
        self.authIcon.setSizePolicy(sizePolicy)
        self.authIcon.setMinimumSize(QtCore.QSize(48, 48))
        self.authIcon.setText(_fromUtf8(""))
        self.authIcon.setObjectName(_fromUtf8("authIcon"))
        self.gridLayout_3.addWidget(self.authIcon, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.securityTab = QtGui.QWidget()
        self.securityTab.setObjectName(_fromUtf8("securityTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.securityTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.securityIcon = QtGui.QLabel(self.securityTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.securityIcon.sizePolicy().hasHeightForWidth())
        self.securityIcon.setSizePolicy(sizePolicy)
        self.securityIcon.setMinimumSize(QtCore.QSize(48, 48))
        self.securityIcon.setText(_fromUtf8(""))
        self.securityIcon.setObjectName(_fromUtf8("securityIcon"))
        self.gridLayout_4.addWidget(self.securityIcon, 0, 0, 1, 1)
        self.securityGridLayout = QtGui.QGridLayout()
        self.securityGridLayout.setObjectName(_fromUtf8("securityGridLayout"))
        self.securityOptGroup = QtGui.QGroupBox(self.securityTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.securityOptGroup.sizePolicy().hasHeightForWidth())
        self.securityOptGroup.setSizePolicy(sizePolicy)
        self.securityOptGroup.setObjectName(_fromUtf8("securityOptGroup"))
        self.gridLayout_9 = QtGui.QGridLayout(self.securityOptGroup)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.encryptionBox = QtGui.QComboBox(self.securityOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryptionBox.sizePolicy().hasHeightForWidth())
        self.encryptionBox.setSizePolicy(sizePolicy)
        self.encryptionBox.setMinimumSize(QtCore.QSize(0, 20))
        self.encryptionBox.setObjectName(_fromUtf8("encryptionBox"))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.encryptionBox.addItem(_fromUtf8(""))
        self.gridLayout_9.addWidget(self.encryptionBox, 0, 0, 1, 1)
        self.securityGridLayout.addWidget(self.securityOptGroup, 0, 0, 1, 1)
        self.serverCertGroup = QtGui.QGroupBox(self.securityTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverCertGroup.sizePolicy().hasHeightForWidth())
        self.serverCertGroup.setSizePolicy(sizePolicy)
        self.serverCertGroup.setObjectName(_fromUtf8("serverCertGroup"))
        self.gridLayout_10 = QtGui.QGridLayout(self.serverCertGroup)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.validateBox = QtGui.QComboBox(self.serverCertGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateBox.sizePolicy().hasHeightForWidth())
        self.validateBox.setSizePolicy(sizePolicy)
        self.validateBox.setMinimumSize(QtCore.QSize(0, 20))
        self.validateBox.setObjectName(_fromUtf8("validateBox"))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self.validateBox.addItem(_fromUtf8(""))
        self.gridLayout_10.addWidget(self.validateBox, 0, 0, 1, 1)
        self.securityGridLayout.addWidget(self.serverCertGroup, 1, 0, 1, 1)
        self.clientCertOptGroup = QtGui.QGroupBox(self.securityTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientCertOptGroup.sizePolicy().hasHeightForWidth())
        self.clientCertOptGroup.setSizePolicy(sizePolicy)
        self.clientCertOptGroup.setObjectName(_fromUtf8("clientCertOptGroup"))
        self.gridLayout_11 = QtGui.QGridLayout(self.clientCertOptGroup)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.clentCertForm = QtGui.QGridLayout()
        self.clentCertForm.setObjectName(_fromUtf8("clentCertForm"))
        self.useClientCertBox = QtGui.QCheckBox(self.clientCertOptGroup)
        self.useClientCertBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useClientCertBox.sizePolicy().hasHeightForWidth())
        self.useClientCertBox.setSizePolicy(sizePolicy)
        self.useClientCertBox.setMinimumSize(QtCore.QSize(0, 20))
        self.useClientCertBox.setObjectName(_fromUtf8("useClientCertBox"))
        self.clentCertForm.addWidget(self.useClientCertBox, 0, 0, 1, 3)
        self.certFileLabel = QtGui.QLabel(self.clientCertOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.certFileLabel.sizePolicy().hasHeightForWidth())
        self.certFileLabel.setSizePolicy(sizePolicy)
        self.certFileLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.certFileLabel.setWordWrap(False)
        self.certFileLabel.setObjectName(_fromUtf8("certFileLabel"))
        self.clentCertForm.addWidget(self.certFileLabel, 1, 0, 1, 1)
        self.certFileEdit = QtGui.QLineEdit(self.clientCertOptGroup)
        self.certFileEdit.setEnabled(False)
        self.certFileEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.certFileEdit.setObjectName(_fromUtf8("certFileEdit"))
        self.clentCertForm.addWidget(self.certFileEdit, 1, 1, 1, 1)
        self.certKeyfileEdit = QtGui.QLineEdit(self.clientCertOptGroup)
        self.certKeyfileEdit.setEnabled(False)
        self.certKeyfileEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.certKeyfileEdit.setObjectName(_fromUtf8("certKeyfileEdit"))
        self.clentCertForm.addWidget(self.certKeyfileEdit, 2, 1, 1, 1)
        self.certKeyfileButton = QtGui.QToolButton(self.clientCertOptGroup)
        self.certKeyfileButton.setEnabled(False)
        self.certKeyfileButton.setMinimumSize(QtCore.QSize(0, 20))
        self.certKeyfileButton.setObjectName(_fromUtf8("certKeyfileButton"))
        self.clentCertForm.addWidget(self.certKeyfileButton, 1, 2, 1, 1)
        self.certFileButton = QtGui.QToolButton(self.clientCertOptGroup)
        self.certFileButton.setEnabled(False)
        self.certFileButton.setMinimumSize(QtCore.QSize(0, 20))
        self.certFileButton.setObjectName(_fromUtf8("certFileButton"))
        self.clentCertForm.addWidget(self.certFileButton, 2, 2, 1, 1)
        self.certKeyfileLabel = QtGui.QLabel(self.clientCertOptGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.certKeyfileLabel.sizePolicy().hasHeightForWidth())
        self.certKeyfileLabel.setSizePolicy(sizePolicy)
        self.certKeyfileLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.certKeyfileLabel.setWordWrap(False)
        self.certKeyfileLabel.setObjectName(_fromUtf8("certKeyfileLabel"))
        self.clentCertForm.addWidget(self.certKeyfileLabel, 2, 0, 1, 1)
        self.gridLayout_11.addLayout(self.clentCertForm, 0, 0, 1, 1)
        self.securityGridLayout.addWidget(self.clientCertOptGroup, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.securityGridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.securityGridLayout, 0, 1, 2, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.securityTab, _fromUtf8(""))
        self.vboxlayout.addWidget(self.splitter)
        self.line = QtGui.QFrame(ServerDialogDesign)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vboxlayout.addWidget(self.line)
        self.bottomHBoxLayout = QtGui.QHBoxLayout()
        self.bottomHBoxLayout.setObjectName(_fromUtf8("bottomHBoxLayout"))
        spacerItem5 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottomHBoxLayout.addItem(spacerItem5)
        self.okButton = QtGui.QPushButton(ServerDialogDesign)
        self.okButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.okButton.setAutoDefault(True)
        self.okButton.setDefault(True)
        self.okButton.setFlat(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.bottomHBoxLayout.addWidget(self.okButton)
        self.applyButton = QtGui.QPushButton(ServerDialogDesign)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy)
        self.applyButton.setAutoDefault(False)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.bottomHBoxLayout.addWidget(self.applyButton)
        self.cancelButton = QtGui.QPushButton(ServerDialogDesign)
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.bottomHBoxLayout.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.bottomHBoxLayout)
        self.hostLabel.setBuddy(self.hostEdit)
        self.portLabel.setBuddy(self.portSpinBox)
        self.mechanismLabel.setBuddy(self.mechanismBox)
        self.bindAsLabel.setBuddy(self.bindAsEdit)
        self.passwordLabel.setBuddy(self.passwordEdit)
        self.certFileLabel.setBuddy(self.certFileEdit)
        self.certKeyfileLabel.setBuddy(self.certKeyfileEdit)

        self.retranslateUi(ServerDialogDesign)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addBaseDNButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.addBaseDN)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.addServer)
        QtCore.QObject.connect(self.applyButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.saveServerlist)
        QtCore.QObject.connect(self.baseDNBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.addBaseDNButton.setDisabled)
        QtCore.QObject.connect(self.baseDNBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.deleteBaseDNButton.setDisabled)
        QtCore.QObject.connect(self.baseDNBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.baseDNEdit.setDisabled)
        QtCore.QObject.connect(self.baseDNBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.baseDNListWidget.setDisabled)
        QtCore.QObject.connect(self.bindAsEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), ServerDialogDesign.addBaseDN)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.reject)
        QtCore.QObject.connect(self.certFileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.certFileDialog)
        QtCore.QObject.connect(self.certKeyfileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.certKeyfileDialog)
        QtCore.QObject.connect(self.deleteBaseDNButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.deleteBaseDN)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.deleteServer)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.accept)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certFileEdit.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certKeyfileEdit.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certFileButton.setEnabled)
        QtCore.QObject.connect(self.useClientCertBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.certKeyfileButton.setEnabled)
        QtCore.QObject.connect(self.bindAnonBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.mechanismBox.setDisabled)
        QtCore.QObject.connect(self.bindAnonBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.bindAsEdit.setDisabled)
        QtCore.QObject.connect(self.bindAnonBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.passwordEdit.setDisabled)
        QtCore.QObject.connect(self.testConnectionButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ServerDialogDesign.testConnection)
        QtCore.QMetaObject.connectSlotsByName(ServerDialogDesign)
        ServerDialogDesign.setTabOrder(self.addButton, self.deleteButton)
        ServerDialogDesign.setTabOrder(self.deleteButton, self.serverListView)
        ServerDialogDesign.setTabOrder(self.serverListView, self.tabWidget)
        ServerDialogDesign.setTabOrder(self.tabWidget, self.hostEdit)
        ServerDialogDesign.setTabOrder(self.hostEdit, self.portSpinBox)
        ServerDialogDesign.setTabOrder(self.portSpinBox, self.aliasBox)
        ServerDialogDesign.setTabOrder(self.aliasBox, self.baseDNBox)
        ServerDialogDesign.setTabOrder(self.baseDNBox, self.baseDNEdit)
        ServerDialogDesign.setTabOrder(self.baseDNEdit, self.addBaseDNButton)
        ServerDialogDesign.setTabOrder(self.addBaseDNButton, self.deleteBaseDNButton)
        ServerDialogDesign.setTabOrder(self.deleteBaseDNButton, self.baseDNListWidget)
        ServerDialogDesign.setTabOrder(self.baseDNListWidget, self.bindAnonBox)
        ServerDialogDesign.setTabOrder(self.bindAnonBox, self.mechanismBox)
        ServerDialogDesign.setTabOrder(self.mechanismBox, self.bindAsEdit)
        ServerDialogDesign.setTabOrder(self.bindAsEdit, self.passwordEdit)
        ServerDialogDesign.setTabOrder(self.passwordEdit, self.encryptionBox)
        ServerDialogDesign.setTabOrder(self.encryptionBox, self.validateBox)
        ServerDialogDesign.setTabOrder(self.validateBox, self.useClientCertBox)
        ServerDialogDesign.setTabOrder(self.useClientCertBox, self.certFileEdit)
        ServerDialogDesign.setTabOrder(self.certFileEdit, self.certKeyfileButton)
        ServerDialogDesign.setTabOrder(self.certKeyfileButton, self.certKeyfileEdit)
        ServerDialogDesign.setTabOrder(self.certKeyfileEdit, self.certFileButton)
        ServerDialogDesign.setTabOrder(self.certFileButton, self.okButton)
        ServerDialogDesign.setTabOrder(self.okButton, self.applyButton)
        ServerDialogDesign.setTabOrder(self.applyButton, self.cancelButton)

    def retranslateUi(self, ServerDialogDesign):
        ServerDialogDesign.setWindowTitle(QtGui.QApplication.translate("ServerDialogDesign", "Manage Server List", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.testConnectionButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "Test connection", None, QtGui.QApplication.UnicodeUTF8))
        self.networkGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "Network options", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.LDAPGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "LDAP options", None, QtGui.QApplication.UnicodeUTF8))
        self.aliasBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Follow aliases", None, QtGui.QApplication.UnicodeUTF8))
        self.baseDNBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Use Base DN provided by server", None, QtGui.QApplication.UnicodeUTF8))
        self.baseDNLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Custom:", None, QtGui.QApplication.UnicodeUTF8))
        self.addBaseDNButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBaseDNButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkTab), QtGui.QApplication.translate("ServerDialogDesign", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.bindOptGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "Bind options", None, QtGui.QApplication.UnicodeUTF8))
        self.bindAnonBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Anonymous bind", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Mechanism:", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "SIMPLE", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "SASL CRAM-MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "SASL DIGEST-MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(3, QtGui.QApplication.translate("ServerDialogDesign", "SASL EXTERNAL", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(4, QtGui.QApplication.translate("ServerDialogDesign", "SASL GSSAPI", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(5, QtGui.QApplication.translate("ServerDialogDesign", "SASL Login", None, QtGui.QApplication.UnicodeUTF8))
        self.mechanismBox.setItemText(6, QtGui.QApplication.translate("ServerDialogDesign", "SASL Plain", None, QtGui.QApplication.UnicodeUTF8))
        self.bindAsLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Bind as:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ServerDialogDesign", "Authentification", None, QtGui.QApplication.UnicodeUTF8))
        self.securityOptGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "Security options", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "Unencrypted connection", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "Transport Layer Security (TLS)", None, QtGui.QApplication.UnicodeUTF8))
        self.encryptionBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "Secure Socket Layer (SSL)", None, QtGui.QApplication.UnicodeUTF8))
        self.serverCertGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "Validate server certificate", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(0, QtGui.QApplication.translate("ServerDialogDesign", "Never", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(1, QtGui.QApplication.translate("ServerDialogDesign", "Allow", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(2, QtGui.QApplication.translate("ServerDialogDesign", "Try", None, QtGui.QApplication.UnicodeUTF8))
        self.validateBox.setItemText(3, QtGui.QApplication.translate("ServerDialogDesign", "Demand", None, QtGui.QApplication.UnicodeUTF8))
        self.clientCertOptGroup.setTitle(QtGui.QApplication.translate("ServerDialogDesign", "Client certificate options", None, QtGui.QApplication.UnicodeUTF8))
        self.useClientCertBox.setText(QtGui.QApplication.translate("ServerDialogDesign", "Use client certificates", None, QtGui.QApplication.UnicodeUTF8))
        self.certFileLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Certificate file:", None, QtGui.QApplication.UnicodeUTF8))
        self.certKeyfileButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.certFileButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.certKeyfileLabel.setText(QtGui.QApplication.translate("ServerDialogDesign", "Certificate keyfile:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.securityTab), QtGui.QApplication.translate("ServerDialogDesign", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("ServerDialogDesign", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setShortcut(QtGui.QApplication.translate("ServerDialogDesign", "Alt+C", None, QtGui.QApplication.UnicodeUTF8))

