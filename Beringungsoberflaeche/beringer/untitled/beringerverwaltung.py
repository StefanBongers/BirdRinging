# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beringungsoberflaeche\beringer\untitled\beringerverwaltung.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_beringerverwaltung(object):
    def setupUi(self, beringerverwaltung):
        beringerverwaltung.setObjectName("beringerverwaltung")
        beringerverwaltung.resize(1132, 341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(beringerverwaltung.sizePolicy().hasHeightForWidth())
        beringerverwaltung.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(beringerverwaltung)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 1101, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CMB_nachname = QtWidgets.QComboBox(self.layoutWidget)
        self.CMB_nachname.setMinimumSize(QtCore.QSize(200, 0))
        self.CMB_nachname.setEditable(True)
        self.CMB_nachname.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.CMB_nachname.setObjectName("CMB_nachname")
        self.gridLayout.addWidget(self.CMB_nachname, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.CMB_nachname_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.CMB_nachname_2.setMinimumSize(QtCore.QSize(200, 0))
        self.CMB_nachname_2.setEditable(True)
        self.CMB_nachname_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.CMB_nachname_2.setObjectName("CMB_nachname_2")
        self.gridLayout.addWidget(self.CMB_nachname_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.TBL_beringer = QtWidgets.QTableWidget(self.layoutWidget)
        self.TBL_beringer.setEnabled(True)
        self.TBL_beringer.setMaximumSize(QtCore.QSize(16777215, 150))
        self.TBL_beringer.setObjectName("TBL_beringer")
        self.TBL_beringer.setColumnCount(11)
        self.TBL_beringer.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_beringer.setHorizontalHeaderItem(10, item)
        self.TBL_beringer.horizontalHeader().setDefaultSectionSize(100)
        self.TBL_beringer.verticalHeader().setVisible(False)
        self.TBL_beringer.verticalHeader().setHighlightSections(True)
        self.verticalLayout.addWidget(self.TBL_beringer)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BTN_speichern = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_speichern.setObjectName("BTN_speichern")
        self.horizontalLayout_2.addWidget(self.BTN_speichern)
        self.BTN_neu = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_neu.setObjectName("BTN_neu")
        self.horizontalLayout_2.addWidget(self.BTN_neu)
        self.BTN_abbrechen = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_abbrechen.setObjectName("BTN_abbrechen")
        self.horizontalLayout_2.addWidget(self.BTN_abbrechen)
        self.BTN_aktivieren = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_aktivieren.setObjectName("BTN_aktivieren")
        self.horizontalLayout_2.addWidget(self.BTN_aktivieren)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BTN_schliessen = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_schliessen.setMinimumSize(QtCore.QSize(200, 25))
        self.BTN_schliessen.setObjectName("BTN_schliessen")
        self.horizontalLayout_3.addWidget(self.BTN_schliessen)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(beringerverwaltung)
        QtCore.QMetaObject.connectSlotsByName(beringerverwaltung)

    def retranslateUi(self, beringerverwaltung):
        _translate = QtCore.QCoreApplication.translate
        beringerverwaltung.setWindowTitle(_translate("beringerverwaltung", "beringerverwaltung"))
        self.label.setText(_translate("beringerverwaltung", "Nachname:"))
        self.label_2.setText(_translate("beringerverwaltung", "Vorname:"))
        item = self.TBL_beringer.verticalHeaderItem(0)
        item.setText(_translate("beringerverwaltung", "1"))
        item = self.TBL_beringer.horizontalHeaderItem(0)
        item.setText(_translate("beringerverwaltung", "Vorname"))
        item = self.TBL_beringer.horizontalHeaderItem(1)
        item.setText(_translate("beringerverwaltung", "Nachname"))
        item = self.TBL_beringer.horizontalHeaderItem(2)
        item.setText(_translate("beringerverwaltung", "Straße"))
        item = self.TBL_beringer.horizontalHeaderItem(3)
        item.setText(_translate("beringerverwaltung", "PLZ"))
        item = self.TBL_beringer.horizontalHeaderItem(4)
        item.setText(_translate("beringerverwaltung", "Stadt"))
        item = self.TBL_beringer.horizontalHeaderItem(5)
        item.setText(_translate("beringerverwaltung", "Land"))
        item = self.TBL_beringer.horizontalHeaderItem(6)
        item.setText(_translate("beringerverwaltung", "Telefon"))
        item = self.TBL_beringer.horizontalHeaderItem(7)
        item.setText(_translate("beringerverwaltung", "Fax"))
        item = self.TBL_beringer.horizontalHeaderItem(8)
        item.setText(_translate("beringerverwaltung", "Email"))
        item = self.TBL_beringer.horizontalHeaderItem(9)
        item.setText(_translate("beringerverwaltung", "Anmerkung"))
        item = self.TBL_beringer.horizontalHeaderItem(10)
        item.setText(_translate("beringerverwaltung", "Wiederfanganzeige"))
        self.BTN_speichern.setText(_translate("beringerverwaltung", "Speichern"))
        self.BTN_neu.setText(_translate("beringerverwaltung", "Neu..."))
        self.BTN_abbrechen.setText(_translate("beringerverwaltung", "Abbrechen"))
        self.BTN_aktivieren.setText(_translate("beringerverwaltung", "Beringer für aktuelles Jahr freischalten"))
        self.BTN_schliessen.setText(_translate("beringerverwaltung", "Schließen"))