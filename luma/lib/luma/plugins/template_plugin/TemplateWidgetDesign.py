# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/template_plugin/TemplateWidgetDesign.ui'
#
# Created: Tue Sep 28 04:56:03 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class TemplateWidgetDesign(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("TemplateWidgetDesign")


        TemplateWidgetDesignLayout = QHBoxLayout(self,0,6,"TemplateWidgetDesignLayout")

        self.splitter6 = QSplitter(self,"splitter6")
        self.splitter6.setOrientation(QSplitter.Horizontal)

        self.frame3 = QFrame(self.splitter6,"frame3")
        self.frame3.setFrameShape(QFrame.NoFrame)
        self.frame3.setFrameShadow(QFrame.Raised)
        frame3Layout = QGridLayout(self.frame3,1,1,2,6,"frame3Layout")

        self.textLabel1 = QLabel(self.frame3,"textLabel1")

        frame3Layout.addMultiCellWidget(self.textLabel1,0,0,0,1)

        self.templateView = QListView(self.frame3,"templateView")
        self.templateView.addColumn(self.__tr("Name"))
        templateView_font = QFont(self.templateView.font())
        self.templateView.setFont(templateView_font)
        self.templateView.setAllColumnsShowFocus(1)
        self.templateView.setResizeMode(QListView.AllColumns)

        frame3Layout.addMultiCellWidget(self.templateView,1,1,0,1)

        self.addTemplateButton = QPushButton(self.frame3,"addTemplateButton")

        frame3Layout.addWidget(self.addTemplateButton,2,0)

        self.saveTemplateButton = QPushButton(self.frame3,"saveTemplateButton")

        frame3Layout.addWidget(self.saveTemplateButton,2,1)

        self.deleteTemplateButton = QPushButton(self.frame3,"deleteTemplateButton")

        frame3Layout.addWidget(self.deleteTemplateButton,3,1)

        self.duplicateTemplateButton = QPushButton(self.frame3,"duplicateTemplateButton")

        frame3Layout.addWidget(self.duplicateTemplateButton,3,0)

        self.frame4 = QFrame(self.splitter6,"frame4")
        self.frame4.setFrameShape(QFrame.NoFrame)
        self.frame4.setFrameShadow(QFrame.Raised)
        frame4Layout = QVBoxLayout(self.frame4,2,6,"frame4Layout")

        layout25 = QGridLayout(None,1,1,0,6,"layout25")

        self.nameLabel = QLabel(self.frame4,"nameLabel")
        self.nameLabel.setSizePolicy(QSizePolicy(0,0,0,0,self.nameLabel.sizePolicy().hasHeightForWidth()))
        self.nameLabel.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        layout25.addWidget(self.nameLabel,0,0)

        self.descriptionLabel = QLabel(self.frame4,"descriptionLabel")
        self.descriptionLabel.setAlignment(QLabel.WordBreak | QLabel.AlignTop)

        layout25.addWidget(self.descriptionLabel,2,1)

        self.templateLabel = QLabel(self.frame4,"templateLabel")

        layout25.addWidget(self.templateLabel,0,1)

        self.textLabel2 = QLabel(self.frame4,"textLabel2")
        self.textLabel2.setSizePolicy(QSizePolicy(0,5,0,0,self.textLabel2.sizePolicy().hasHeightForWidth()))
        self.textLabel2.setAlignment(QLabel.WordBreak | QLabel.AlignTop)

        layout25.addWidget(self.textLabel2,2,0)

        self.serverLabel = QLabel(self.frame4,"serverLabel")

        layout25.addWidget(self.serverLabel,1,1)

        self.textLabel6 = QLabel(self.frame4,"textLabel6")
        self.textLabel6.setSizePolicy(QSizePolicy(0,0,0,0,self.textLabel6.sizePolicy().hasHeightForWidth()))

        layout25.addWidget(self.textLabel6,1,0)
        frame4Layout.addLayout(layout25)
        spacer18 = QSpacerItem(21,16,QSizePolicy.Minimum,QSizePolicy.Fixed)
        frame4Layout.addItem(spacer18)

        layout15 = QGridLayout(None,1,1,0,6,"layout15")
        spacer15 = QSpacerItem(20,82,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layout15.addItem(spacer15,3,2)

        self.addClassButton = QPushButton(self.frame4,"addClassButton")

        layout15.addWidget(self.addClassButton,1,2)
        spacer11 = QSpacerItem(16,21,QSizePolicy.Fixed,QSizePolicy.Minimum)
        layout15.addItem(spacer11,2,0)

        self.classView = QListView(self.frame4,"classView")
        self.classView.addColumn(self.__tr("Objectclass"))
        self.classView.setSizePolicy(QSizePolicy(7,1,0,0,self.classView.sizePolicy().hasHeightForWidth()))
        self.classView.setMaximumSize(QSize(32767,150))
        self.classView.setResizeMode(QListView.AllColumns)

        layout15.addMultiCellWidget(self.classView,1,3,1,1)

        self.textLabel5 = QLabel(self.frame4,"textLabel5")
        self.textLabel5.setSizePolicy(QSizePolicy(5,0,0,0,self.textLabel5.sizePolicy().hasHeightForWidth()))

        layout15.addMultiCellWidget(self.textLabel5,0,0,0,1)

        self.deleteClassButton = QPushButton(self.frame4,"deleteClassButton")

        layout15.addWidget(self.deleteClassButton,2,2)
        frame4Layout.addLayout(layout15)

        layout14 = QGridLayout(None,1,1,0,6,"layout14")

        self.attributeView = QListView(self.frame4,"attributeView")
        self.attributeView.addColumn(self.__tr("Name"))
        self.attributeView.addColumn(self.__tr("Must"))
        self.attributeView.addColumn(self.__tr("Show"))
        self.attributeView.addColumn(self.__tr("Default value"))
        self.attributeView.setResizeMode(QListView.LastColumn)

        layout14.addMultiCellWidget(self.attributeView,1,4,1,1)

        self.textLabel7 = QLabel(self.frame4,"textLabel7")

        layout14.addMultiCellWidget(self.textLabel7,0,0,0,1)

        self.addAttributeButton = QPushButton(self.frame4,"addAttributeButton")

        layout14.addWidget(self.addAttributeButton,1,2)

        self.editAttributeButton = QPushButton(self.frame4,"editAttributeButton")

        layout14.addWidget(self.editAttributeButton,2,2)
        spacer14 = QSpacerItem(21,31,QSizePolicy.Minimum,QSizePolicy.MinimumExpanding)
        layout14.addItem(spacer14,4,2)
        spacer12 = QSpacerItem(16,21,QSizePolicy.Fixed,QSizePolicy.Minimum)
        layout14.addItem(spacer12,1,0)

        self.deleteAttributeButton = QPushButton(self.frame4,"deleteAttributeButton")

        layout14.addWidget(self.deleteAttributeButton,3,2)
        frame4Layout.addLayout(layout14)
        TemplateWidgetDesignLayout.addWidget(self.splitter6)

        self.languageChange()

        self.resize(QSize(673,552).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.addTemplateButton,SIGNAL("clicked()"),self.addTemplate)
        self.connect(self.templateView,SIGNAL("selectionChanged(QListViewItem*)"),self.displayTemplateInfo)
        self.connect(self.addClassButton,SIGNAL("clicked()"),self.addObjectClass)
        self.connect(self.addAttributeButton,SIGNAL("clicked()"),self.addAttribute)
        self.connect(self.deleteClassButton,SIGNAL("clicked()"),self.deleteObjectClass)
        self.connect(self.deleteAttributeButton,SIGNAL("clicked()"),self.deleteAttribute)
        self.connect(self.editAttributeButton,SIGNAL("clicked()"),self.editAttribute)

        self.setTabOrder(self.templateView,self.addTemplateButton)
        self.setTabOrder(self.addTemplateButton,self.saveTemplateButton)
        self.setTabOrder(self.saveTemplateButton,self.duplicateTemplateButton)
        self.setTabOrder(self.duplicateTemplateButton,self.deleteTemplateButton)
        self.setTabOrder(self.deleteTemplateButton,self.classView)
        self.setTabOrder(self.classView,self.addClassButton)
        self.setTabOrder(self.addClassButton,self.deleteClassButton)
        self.setTabOrder(self.deleteClassButton,self.attributeView)
        self.setTabOrder(self.attributeView,self.addAttributeButton)
        self.setTabOrder(self.addAttributeButton,self.editAttributeButton)
        self.setTabOrder(self.editAttributeButton,self.deleteAttributeButton)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.textLabel1.setText(self.__tr("<b>Templates</b>"))
        self.templateView.header().setLabel(0,self.__tr("Name"))
        self.addTemplateButton.setText(self.__tr("&Add..."))
        self.addTemplateButton.setAccel(self.__tr("Alt+A"))
        self.saveTemplateButton.setText(self.__tr("&Save"))
        self.saveTemplateButton.setAccel(self.__tr("Alt+S"))
        self.deleteTemplateButton.setText(self.__tr("&Delete..."))
        self.deleteTemplateButton.setAccel(self.__tr("Alt+D"))
        self.duplicateTemplateButton.setText(self.__tr("D&uplicate..."))
        self.duplicateTemplateButton.setAccel(self.__tr("Alt+U"))
        self.nameLabel.setText(self.__tr("<b>Name:</b>"))
        self.descriptionLabel.setText(self.__tr("This a description of the template you are currently working with."))
        self.templateLabel.setText(self.__tr("foo"))
        self.textLabel2.setText(self.__tr("<b>Description:</b>"))
        self.serverLabel.setText(self.__tr("bar"))
        self.textLabel6.setText(self.__tr("<b>Server:</b>"))
        self.addClassButton.setText(self.__tr("Add..."))
        self.classView.header().setLabel(0,self.__tr("Objectclass"))
        self.textLabel5.setText(self.__tr("<b>Objectclasses</b>"))
        self.deleteClassButton.setText(self.__tr("Delete"))
        self.attributeView.header().setLabel(0,self.__tr("Name"))
        self.attributeView.header().setLabel(1,self.__tr("Must"))
        self.attributeView.header().setLabel(2,self.__tr("Show"))
        self.attributeView.header().setLabel(3,self.__tr("Default value"))
        self.textLabel7.setText(self.__tr("<b>Attributes</b>"))
        self.addAttributeButton.setText(self.__tr("Add..."))
        self.editAttributeButton.setText(self.__tr("Edit..."))
        self.deleteAttributeButton.setText(self.__tr("Delete"))


    def addTemplate(self):
        print "TemplateWidgetDesign.addTemplate(): Not implemented yet"

    def typeChanged(self):
        print "TemplateWidgetDesign.typeChanged(): Not implemented yet"

    def displayTemplateInfo(self):
        print "TemplateWidgetDesign.displayTemplateInfo(): Not implemented yet"

    def addObjectClass(self):
        print "TemplateWidgetDesign.addObjectClass(): Not implemented yet"

    def addAttribute(self):
        print "TemplateWidgetDesign.addAttribute(): Not implemented yet"

    def deleteObjectClass(self):
        print "TemplateWidgetDesign.deleteObjectClass(): Not implemented yet"

    def deleteAttribute(self):
        print "TemplateWidgetDesign.deleteAttribute(): Not implemented yet"

    def editAttribute(self):
        print "TemplateWidgetDesign.editAttribute(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("TemplateWidgetDesign",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = TemplateWidgetDesign()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()