# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/einar/Desktop/luma-release-tagging/resources/forms/plugins/search/SearchFormDesign.ui'
#
# Created: Fri Apr  1 15:26:56 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(377, 222)
        self.verticalLayout = QtGui.QVBoxLayout(SearchForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionsGrid = QtGui.QGroupBox(SearchForm)
        self.optionsGrid.setObjectName("optionsGrid")
        self.gridLayout_2 = QtGui.QGridLayout(self.optionsGrid)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.serverLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverLabel.sizePolicy().hasHeightForWidth())
        self.serverLabel.setSizePolicy(sizePolicy)
        self.serverLabel.setObjectName("serverLabel")
        self.gridLayout_2.addWidget(self.serverLabel, 2, 0, 1, 1)
        self.baseDNLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseDNLabel.sizePolicy().hasHeightForWidth())
        self.baseDNLabel.setSizePolicy(sizePolicy)
        self.baseDNLabel.setObjectName("baseDNLabel")
        self.gridLayout_2.addWidget(self.baseDNLabel, 3, 0, 1, 1)
        self.baseDNBox = QtGui.QComboBox(self.optionsGrid)
        self.baseDNBox.setEnabled(True)
        self.baseDNBox.setObjectName("baseDNBox")
        self.gridLayout_2.addWidget(self.baseDNBox, 3, 1, 1, 2)
        self.serverBox = QtGui.QComboBox(self.optionsGrid)
        self.serverBox.setEnabled(True)
        self.serverBox.setObjectName("serverBox")
        self.gridLayout_2.addWidget(self.serverBox, 2, 1, 1, 2)
        self.scopeBox = QtGui.QComboBox(self.optionsGrid)
        self.scopeBox.setMaxVisibleItems(3)
        self.scopeBox.setMaxCount(3)
        self.scopeBox.setDuplicatesEnabled(True)
        self.scopeBox.setObjectName("scopeBox")
        self.gridLayout_2.addWidget(self.scopeBox, 4, 1, 1, 2)
        self.sizeLimitSpinBox = QtGui.QSpinBox(self.optionsGrid)
        self.sizeLimitSpinBox.setObjectName("sizeLimitSpinBox")
        self.gridLayout_2.addWidget(self.sizeLimitSpinBox, 5, 1, 1, 2)
        self.sizeLimitLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLimitLabel.sizePolicy().hasHeightForWidth())
        self.sizeLimitLabel.setSizePolicy(sizePolicy)
        self.sizeLimitLabel.setObjectName("sizeLimitLabel")
        self.gridLayout_2.addWidget(self.sizeLimitLabel, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.optionsGrid)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.optionsGrid)
        self.line = QtGui.QFrame(SearchForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.searchHLayout = QtGui.QHBoxLayout()
        self.searchHLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.searchHLayout.setObjectName("searchHLayout")
        self.filterBoxEdit = QtGui.QComboBox(SearchForm)
        self.filterBoxEdit.setEditable(True)
        self.filterBoxEdit.setObjectName("filterBoxEdit")
        self.searchHLayout.addWidget(self.filterBoxEdit)
        self.searchButton = QtGui.QPushButton(SearchForm)
        self.searchButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setObjectName("searchButton")
        self.searchHLayout.addWidget(self.searchButton)
        self.filterBuilderToolButton = QtGui.QToolButton(SearchForm)
        self.filterBuilderToolButton.setEnabled(True)
        self.filterBuilderToolButton.setObjectName("filterBuilderToolButton")
        self.searchHLayout.addWidget(self.filterBuilderToolButton)
        self.verticalLayout.addLayout(self.searchHLayout)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.serverLabel.setBuddy(self.serverBox)
        self.baseDNLabel.setBuddy(self.baseDNBox)
        self.sizeLimitLabel.setBuddy(self.sizeLimitSpinBox)
        self.label.setBuddy(self.scopeBox)

        self.retranslateUi(SearchForm)
        self.scopeBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)
        SearchForm.setTabOrder(self.filterBoxEdit, self.searchButton)
        SearchForm.setTabOrder(self.searchButton, self.filterBuilderToolButton)
        SearchForm.setTabOrder(self.filterBuilderToolButton, self.serverBox)
        SearchForm.setTabOrder(self.serverBox, self.baseDNBox)
        SearchForm.setTabOrder(self.baseDNBox, self.scopeBox)
        SearchForm.setTabOrder(self.scopeBox, self.sizeLimitSpinBox)

    def retranslateUi(self, SearchForm):
        SearchForm.setWindowTitle(QtGui.QApplication.translate("SearchForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.optionsGrid.setTitle(QtGui.QApplication.translate("SearchForm", "Search options", None, QtGui.QApplication.UnicodeUTF8))
        self.serverLabel.setText(QtGui.QApplication.translate("SearchForm", "Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.baseDNLabel.setText(QtGui.QApplication.translate("SearchForm", "Base DN:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLimitLabel.setToolTip(QtGui.QApplication.translate("SearchForm", "Set the limit for retrived entries. (0 = No limit)", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLimitLabel.setText(QtGui.QApplication.translate("SearchForm", "Size limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("SearchForm", "Set the search level.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SearchForm", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("SearchForm", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.filterBuilderToolButton.setToolTip(QtGui.QApplication.translate("SearchForm", "Open the Filter Builder", None, QtGui.QApplication.UnicodeUTF8))
        self.filterBuilderToolButton.setText(QtGui.QApplication.translate("SearchForm", "...", None, QtGui.QApplication.UnicodeUTF8))

