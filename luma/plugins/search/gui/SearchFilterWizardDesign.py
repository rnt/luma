# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/debris/devel/git/luma/resources/forms/plugins/search/SearchFilterWizardDesign.ui'
#
# Created: Wed Mar 16 19:06:01 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SearchFilterWizard(object):
    def setupUi(self, SearchFilterWizard):
        SearchFilterWizard.setObjectName("SearchFilterWizard")
        SearchFilterWizard.resize(423, 451)
        self.gridLayout_4 = QtGui.QGridLayout(SearchFilterWizard)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtGui.QGroupBox(SearchFilterWizard)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.filterComboBox = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterComboBox.sizePolicy().hasHeightForWidth())
        self.filterComboBox.setSizePolicy(sizePolicy)
        self.filterComboBox.setObjectName("filterComboBox")
        self.gridLayout.addWidget(self.filterComboBox, 0, 1, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 3)
        self.actionAddFilter = QtGui.QPushButton(self.groupBox)
        self.actionAddFilter.setObjectName("actionAddFilter")
        self.gridLayout.addWidget(self.actionAddFilter, 1, 3, 1, 1)
        self.actionDeleteFilter = QtGui.QPushButton(self.groupBox)
        self.actionDeleteFilter.setObjectName("actionDeleteFilter")
        self.gridLayout.addWidget(self.actionDeleteFilter, 1, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(SearchFilterWizard)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbAttribute = QtGui.QRadioButton(self.groupBox_2)
        self.rbAttribute.setObjectName("rbAttribute")
        self.gridLayout_2.addWidget(self.rbAttribute, 0, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 2, 1, 2)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.actionAddSearchCriteria = QtGui.QPushButton(self.groupBox_2)
        self.actionAddSearchCriteria.setObjectName("actionAddSearchCriteria")
        self.gridLayout_2.addWidget(self.actionAddSearchCriteria, 1, 3, 1, 1)
        self.rbObjectClass = QtGui.QRadioButton(self.groupBox_2)
        self.rbObjectClass.setChecked(True)
        self.rbObjectClass.setObjectName("rbObjectClass")
        self.gridLayout_2.addWidget(self.rbObjectClass, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(SearchFilterWizard)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 0, 0, 1, 1)
        self.actionAddConcatenation = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionAddConcatenation.sizePolicy().hasHeightForWidth())
        self.actionAddConcatenation.setSizePolicy(sizePolicy)
        self.actionAddConcatenation.setObjectName("actionAddConcatenation")
        self.gridLayout_3.addWidget(self.actionAddConcatenation, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.line = QtGui.QFrame(SearchFilterWizard)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 5, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SearchFilterWizard)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 6, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(SearchFilterWizard)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.currentFilter = QtGui.QLineEdit(self.groupBox_4)
        self.currentFilter.setObjectName("currentFilter")
        self.gridLayout_8.addWidget(self.currentFilter, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 0, 1, 1)

        self.retranslateUi(SearchFilterWizard)
        QtCore.QObject.connect(self.rbObjectClass, QtCore.SIGNAL("toggled(bool)"), self.comboBox_2.setEnabled)
        QtCore.QObject.connect(self.rbAttribute, QtCore.SIGNAL("toggled(bool)"), self.comboBox_2.setDisabled)
        QtCore.QObject.connect(self.rbObjectClass, QtCore.SIGNAL("toggled(bool)"), self.comboBox_3.setDisabled)
        QtCore.QObject.connect(self.rbAttribute, QtCore.SIGNAL("toggled(bool)"), self.comboBox_3.setEnabled)
        QtCore.QObject.connect(self.comboBox_3, QtCore.SIGNAL("activated(int)"), self.lineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(SearchFilterWizard)
        SearchFilterWizard.setTabOrder(self.filterComboBox, self.actionAddFilter)
        SearchFilterWizard.setTabOrder(self.actionAddFilter, self.actionDeleteFilter)
        SearchFilterWizard.setTabOrder(self.actionDeleteFilter, self.rbObjectClass)
        SearchFilterWizard.setTabOrder(self.rbObjectClass, self.rbAttribute)
        SearchFilterWizard.setTabOrder(self.rbAttribute, self.comboBox_2)
        SearchFilterWizard.setTabOrder(self.comboBox_2, self.comboBox_3)
        SearchFilterWizard.setTabOrder(self.comboBox_3, self.lineEdit)
        SearchFilterWizard.setTabOrder(self.lineEdit, self.actionAddSearchCriteria)
        SearchFilterWizard.setTabOrder(self.actionAddSearchCriteria, self.comboBox_4)
        SearchFilterWizard.setTabOrder(self.comboBox_4, self.actionAddConcatenation)
        SearchFilterWizard.setTabOrder(self.actionAddConcatenation, self.currentFilter)
        SearchFilterWizard.setTabOrder(self.currentFilter, self.buttonBox)

    def retranslateUi(self, SearchFilterWizard):
        SearchFilterWizard.setWindowTitle(QtGui.QApplication.translate("SearchFilterWizard", "Search Filter Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SearchFilterWizard", "Filter bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SearchFilterWizard", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFilter.setText(QtGui.QApplication.translate("SearchFilterWizard", "Add current filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteFilter.setText(QtGui.QApplication.translate("SearchFilterWizard", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SearchFilterWizard", "Search criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.rbAttribute.setText(QtGui.QApplication.translate("SearchFilterWizard", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("SearchFilterWizard", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("SearchFilterWizard", "= (equals)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("SearchFilterWizard", "-= (approximately)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("SearchFilterWizard", ">= (greater than)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("SearchFilterWizard", "<= (less than)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddSearchCriteria.setText(QtGui.QApplication.translate("SearchFilterWizard", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.rbObjectClass.setText(QtGui.QApplication.translate("SearchFilterWizard", "ObjectClass", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SearchFilterWizard", "Concatenation", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("SearchFilterWizard", "and", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("SearchFilterWizard", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(2, QtGui.QApplication.translate("SearchFilterWizard", "not", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddConcatenation.setText(QtGui.QApplication.translate("SearchFilterWizard", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SearchFilterWizard", "Current Filter", None, QtGui.QApplication.UnicodeUTF8))

