# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beringungsoberflaeche\ringserieneingabe\dialogringserieneingabe.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogRingserienEingabe(object):
    def setupUi(self, DialogRingserienEingabe):
        DialogRingserienEingabe.setObjectName("DialogRingserienEingabe")
        DialogRingserienEingabe.resize(1035, 694)
        self.gridLayout = QtWidgets.QGridLayout(DialogRingserienEingabe)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_zusatzeingabe = QtWidgets.QGroupBox(DialogRingserienEingabe)
        self.groupBox_zusatzeingabe.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_zusatzeingabe.sizePolicy().hasHeightForWidth())
        self.groupBox_zusatzeingabe.setSizePolicy(sizePolicy)
        self.groupBox_zusatzeingabe.setMinimumSize(QtCore.QSize(800, 200))
        self.groupBox_zusatzeingabe.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_zusatzeingabe.setFont(font)
        self.groupBox_zusatzeingabe.setObjectName("groupBox_zusatzeingabe")
        self.label_8 = QtWidgets.QLabel(self.groupBox_zusatzeingabe)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 91, 35))
        self.label_8.setObjectName("label_8")
        self.INP_neueSerie_ringserie = QtWidgets.QLineEdit(self.groupBox_zusatzeingabe)
        self.INP_neueSerie_ringserie.setGeometry(QtCore.QRect(130, 30, 71, 35))
        self.INP_neueSerie_ringserie.setMaxLength(2)
        self.INP_neueSerie_ringserie.setObjectName("INP_neueSerie_ringserie")
        self.CMB_neueSerie_ringtyp_auswahl = QtWidgets.QComboBox(self.groupBox_zusatzeingabe)
        self.CMB_neueSerie_ringtyp_auswahl.setGeometry(QtCore.QRect(280, 30, 81, 35))
        self.CMB_neueSerie_ringtyp_auswahl.setEditable(False)
        self.CMB_neueSerie_ringtyp_auswahl.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.CMB_neueSerie_ringtyp_auswahl.setObjectName("CMB_neueSerie_ringtyp_auswahl")
        self.label_7 = QtWidgets.QLabel(self.groupBox_zusatzeingabe)
        self.label_7.setGeometry(QtCore.QRect(210, 30, 71, 35))
        self.label_7.setObjectName("label_7")
        self.BTN_ringtypenliste = QtWidgets.QPushButton(self.groupBox_zusatzeingabe)
        self.BTN_ringtypenliste.setGeometry(QtCore.QRect(360, 30, 171, 35))
        self.BTN_ringtypenliste.setObjectName("BTN_ringtypenliste")
        self.TBL_ringtypen = QtWidgets.QTableWidget(self.groupBox_zusatzeingabe)
        self.TBL_ringtypen.setGeometry(QtCore.QRect(20, 70, 961, 111))
        self.TBL_ringtypen.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TBL_ringtypen.setObjectName("TBL_ringtypen")
        self.TBL_ringtypen.setColumnCount(7)
        self.TBL_ringtypen.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringtypen.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.groupBox_zusatzeingabe, 5, 0, 1, 7)
        self.BTN_spezial = QtWidgets.QPushButton(DialogRingserienEingabe)
        self.BTN_spezial.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_spezial.setFont(font)
        self.BTN_spezial.setObjectName("BTN_spezial")
        self.gridLayout.addWidget(self.BTN_spezial, 2, 6, 1, 1)
        self.INP_end_ringnummer_neue_serie = QtWidgets.QLineEdit(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INP_end_ringnummer_neue_serie.sizePolicy().hasHeightForWidth())
        self.INP_end_ringnummer_neue_serie.setSizePolicy(sizePolicy)
        self.INP_end_ringnummer_neue_serie.setMinimumSize(QtCore.QSize(50, 0))
        self.INP_end_ringnummer_neue_serie.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.INP_end_ringnummer_neue_serie.setFont(font)
        self.INP_end_ringnummer_neue_serie.setObjectName("INP_end_ringnummer_neue_serie")
        self.gridLayout.addWidget(self.INP_end_ringnummer_neue_serie, 4, 3, 1, 1)
        self.BTN_info = QtWidgets.QPushButton(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_info.setFont(font)
        self.BTN_info.setObjectName("BTN_info")
        self.gridLayout.addWidget(self.BTN_info, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.CMB_ringserienauswahl = QtWidgets.QComboBox(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CMB_ringserienauswahl.setFont(font)
        self.CMB_ringserienauswahl.setObjectName("CMB_ringserienauswahl")
        self.horizontalLayout_2.addWidget(self.CMB_ringserienauswahl)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.BTN_beispiel_eingabe_ringserie = QtWidgets.QPushButton(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_beispiel_eingabe_ringserie.setFont(font)
        self.BTN_beispiel_eingabe_ringserie.setObjectName("BTN_beispiel_eingabe_ringserie")
        self.gridLayout.addWidget(self.BTN_beispiel_eingabe_ringserie, 2, 1, 1, 1)
        self.BTN_neue_ringserie = QtWidgets.QPushButton(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_neue_ringserie.sizePolicy().hasHeightForWidth())
        self.BTN_neue_ringserie.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_neue_ringserie.setFont(font)
        self.BTN_neue_ringserie.setObjectName("BTN_neue_ringserie")
        self.gridLayout.addWidget(self.BTN_neue_ringserie, 4, 6, 1, 1)
        self.INP_anz_ring_schnur = QtWidgets.QLineEdit(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INP_anz_ring_schnur.sizePolicy().hasHeightForWidth())
        self.INP_anz_ring_schnur.setSizePolicy(sizePolicy)
        self.INP_anz_ring_schnur.setMinimumSize(QtCore.QSize(50, 0))
        self.INP_anz_ring_schnur.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.INP_anz_ring_schnur.setFont(font)
        self.INP_anz_ring_schnur.setObjectName("INP_anz_ring_schnur")
        self.gridLayout.addWidget(self.INP_anz_ring_schnur, 3, 1, 1, 1)
        self.TBL_ringserien = OwnTable(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TBL_ringserien.sizePolicy().hasHeightForWidth())
        self.TBL_ringserien.setSizePolicy(sizePolicy)
        self.TBL_ringserien.setMinimumSize(QtCore.QSize(900, 0))
        self.TBL_ringserien.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TBL_ringserien.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.TBL_ringserien.setAlternatingRowColors(False)
        self.TBL_ringserien.setShowGrid(True)
        self.TBL_ringserien.setObjectName("TBL_ringserien")
        self.TBL_ringserien.setColumnCount(8)
        self.TBL_ringserien.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TBL_ringserien.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.TBL_ringserien, 1, 0, 1, 7)
        self.INP_zusatz = QtWidgets.QLineEdit(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INP_zusatz.sizePolicy().hasHeightForWidth())
        self.INP_zusatz.setSizePolicy(sizePolicy)
        self.INP_zusatz.setMinimumSize(QtCore.QSize(30, 0))
        self.INP_zusatz.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.INP_zusatz.setFont(font)
        self.INP_zusatz.setObjectName("INP_zusatz")
        self.gridLayout.addWidget(self.INP_zusatz, 3, 6, 1, 1)
        self.BTN_neueSerie_anlegen = QtWidgets.QPushButton(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_neueSerie_anlegen.setFont(font)
        self.BTN_neueSerie_anlegen.setObjectName("BTN_neueSerie_anlegen")
        self.gridLayout.addWidget(self.BTN_neueSerie_anlegen, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(220, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.BTN_close = QtWidgets.QPushButton(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_close.setFont(font)
        self.BTN_close.setObjectName("BTN_close")
        self.gridLayout.addWidget(self.BTN_close, 0, 6, 1, 1)
        self.INP_start_ringnummer_neue_serie = QtWidgets.QLineEdit(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.INP_start_ringnummer_neue_serie.sizePolicy().hasHeightForWidth())
        self.INP_start_ringnummer_neue_serie.setSizePolicy(sizePolicy)
        self.INP_start_ringnummer_neue_serie.setMinimumSize(QtCore.QSize(50, 0))
        self.INP_start_ringnummer_neue_serie.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.INP_start_ringnummer_neue_serie.setFont(font)
        self.INP_start_ringnummer_neue_serie.setMaxLength(8)
        self.INP_start_ringnummer_neue_serie.setObjectName("INP_start_ringnummer_neue_serie")
        self.gridLayout.addWidget(self.INP_start_ringnummer_neue_serie, 3, 3, 1, 1)
        self.BTN_clear = QtWidgets.QPushButton(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BTN_clear.setFont(font)
        self.BTN_clear.setObjectName("BTN_clear")
        self.gridLayout.addWidget(self.BTN_clear, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogRingserienEingabe)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogRingserienEingabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.retranslateUi(DialogRingserienEingabe)
        QtCore.QMetaObject.connectSlotsByName(DialogRingserienEingabe)
        DialogRingserienEingabe.setTabOrder(self.INP_neueSerie_ringserie, self.CMB_neueSerie_ringtyp_auswahl)
        DialogRingserienEingabe.setTabOrder(self.CMB_neueSerie_ringtyp_auswahl, self.BTN_ringtypenliste)
        DialogRingserienEingabe.setTabOrder(self.BTN_ringtypenliste, self.TBL_ringtypen)

    def retranslateUi(self, DialogRingserienEingabe):
        _translate = QtCore.QCoreApplication.translate
        DialogRingserienEingabe.setWindowTitle(_translate("DialogRingserienEingabe", "DialogRingserienEingabe"))
        self.groupBox_zusatzeingabe.setTitle(_translate("DialogRingserienEingabe", "Zusätzliche Daten für neue Ringserie:"))
        self.label_8.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p><span style=\" font-weight:700;\">Start</span>nummer der <span style=\" font-weight:700;\">gesamten</span> Serie! Wurden z.B. 1000 Ringe einer Serie geliefert von XX010001 bis XX011000 in 10 Schnureinheiten (Paketen), so trägt man die erste Nummer (10.001) bei Startnummer ein und die letzte Nummer (11.000) bei Endnummer. Natürlich ohne .</p></body></html>"))
        self.label_8.setText(_translate("DialogRingserienEingabe", "Ringserie:"))
        self.label_7.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p><span style=\" font-weight:700;\">Start</span>nummer der <span style=\" font-weight:700;\">gesamten</span> Serie! Wurden z.B. 1000 Ringe einer Serie geliefert von XX010001 bis XX011000 in 10 Schnureinheiten (Paketen), so trägt man die erste Nummer (10.001) bei Startnummer ein und die letzte Nummer (11.000) bei Endnummer. Natürlich ohne .</p></body></html>"))
        self.label_7.setText(_translate("DialogRingserienEingabe", "Ringtyp: "))
        self.BTN_ringtypenliste.setText(_translate("DialogRingserienEingabe", "Liste Ringtypen"))
        item = self.TBL_ringtypen.horizontalHeaderItem(0)
        item.setText(_translate("DialogRingserienEingabe", "Klasse"))
        item = self.TBL_ringtypen.horizontalHeaderItem(1)
        item.setText(_translate("DialogRingserienEingabe", "Material"))
        item = self.TBL_ringtypen.horizontalHeaderItem(2)
        item.setText(_translate("DialogRingserienEingabe", "Durchmesser"))
        item = self.TBL_ringtypen.horizontalHeaderItem(3)
        item.setText(_translate("DialogRingserienEingabe", "Höhe"))
        item = self.TBL_ringtypen.horizontalHeaderItem(4)
        item.setText(_translate("DialogRingserienEingabe", "Stärke"))
        item = self.TBL_ringtypen.horizontalHeaderItem(5)
        item.setText(_translate("DialogRingserienEingabe", "Farbe"))
        item = self.TBL_ringtypen.horizontalHeaderItem(6)
        item.setText(_translate("DialogRingserienEingabe", "Bemerkung"))
        self.BTN_spezial.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p>Möchte man ein Paket oder eine Schnur \'dazwischenschieben\' oder als nächstes behandeln, so kann man dieses Paket hier auswählen und markieren als das nächste zu verwendende - UNABHÄNGIG von der aktuell definierten Reihenfolge. </p></body></html>"))
        self.BTN_spezial.setText(_translate("DialogRingserienEingabe", "Änderungen speichern"))
        self.BTN_info.setText(_translate("DialogRingserienEingabe", "Info zu Ringmengen"))
        self.label.setText(_translate("DialogRingserienEingabe", "Ringserie:"))
        self.label_4.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p><span style=\" font-weight:700;\">End</span>nummer der <span style=\" font-weight:700;\">gesamten</span> Serie! Wurden z.B. 1000 Ringe einer Serie geliefert von XX010001 bis XX011000 in 10 Schnureinheiten (Paketen), so trägt man die erste Nummer (10.001) bei Startnummer ein und die letzte Nummer (11.000) bei Endnummer. Natürlich ohne .</p></body></html>"))
        self.label_4.setText(_translate("DialogRingserienEingabe", "Endnummer:"))
        self.BTN_beispiel_eingabe_ringserie.setText(_translate("DialogRingserienEingabe", "Beispiel"))
        self.BTN_neue_ringserie.setText(_translate("DialogRingserienEingabe", "Anlegen"))
        self.INP_anz_ring_schnur.setText(_translate("DialogRingserienEingabe", "100"))
        self.TBL_ringserien.setSortingEnabled(True)
        item = self.TBL_ringserien.horizontalHeaderItem(0)
        item.setText(_translate("DialogRingserienEingabe", "Ringserie"))
        item = self.TBL_ringserien.horizontalHeaderItem(1)
        item.setText(_translate("DialogRingserienEingabe", "Ringtyp"))
        item = self.TBL_ringserien.horizontalHeaderItem(2)
        item.setText(_translate("DialogRingserienEingabe", "Startnummer"))
        item = self.TBL_ringserien.horizontalHeaderItem(3)
        item.setText(_translate("DialogRingserienEingabe", "Endnummer"))
        item = self.TBL_ringserien.horizontalHeaderItem(4)
        item.setText(_translate("DialogRingserienEingabe", "Paketnummer\n"
"Reihenfolge"))
        item = self.TBL_ringserien.horizontalHeaderItem(5)
        item.setText(_translate("DialogRingserienEingabe", "letzte vergebene\n"
"Ringnummer"))
        item = self.TBL_ringserien.horizontalHeaderItem(6)
        item.setText(_translate("DialogRingserienEingabe", "Status"))
        item = self.TBL_ringserien.horizontalHeaderItem(7)
        item.setText(_translate("DialogRingserienEingabe", "Bemerkung"))
        self.BTN_neueSerie_anlegen.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p>Dies bedeutet, dass die Ringserie, die Du eingeben möchtest, bisher noch <span style=\" font-size:10pt; font-weight:700; color:#ff0000;\">nicht</span> auf der Station verwendet wurde. Wenn Du nur einen neuen Nummernbereich eingeben möchtest, wähle bitte die bisherige Ringserie links aus und nutze die untere Eingabemaske für das Hinzufügen neuer Nummern.</p></body></html>"))
        self.BTN_neueSerie_anlegen.setText(_translate("DialogRingserienEingabe", "Neue Ringserie anlegen ..."))
        self.label_6.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p>Es gibt (leider) einige Ringe, die keine numerischen Ringnummern haben, sondern zusätzlich noch ein Buchstabe. Z.B. die Serie 39 besteht aus 391F, 392F, 393F, ..., 399F. Um aber intern mit Zahlen rechnen zu können statt mit alphanumerischen Operationen (Texte umwandeln, aufsplitten, wieder zurückwandeln, ...) wurden für die 0,00001% der Fälle dieses Zusatzfeld ins Leben gerufen. Beinhaltet also der hintere Teil der Ringnummer (nach der Serie) einen nicht-numerischen Teil, wird dieser hier bei Zusatz eingetragen.</p></body></html>"))
        self.label_6.setText(_translate("DialogRingserienEingabe", "Zusatz:"))
        self.label_5.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p>Es wird die Anzahl je &quot;Paket&quot; benötigt. Die meisten Ringe sind auf einer Gummischnur aufgezogen. Am Beringertisch befindet sich meistens eine Schnur je Ringtyp/-serie. Die Serie lässt sich also in diese Pakete vereinzeln. Manche Ringe sind z.B. so groß, dass nur 10 Exemplare auf einem Schlauch aufgezogen sind. Dann ist hier 10 einzutragen. Die Standardpaketgröße beträgt 100 (Ringe je Schnur)</p></body></html>"))
        self.label_5.setText(_translate("DialogRingserienEingabe", "Anzahl Ringe pro \'Schnur\':"))
        self.BTN_close.setText(_translate("DialogRingserienEingabe", "Schließen"))
        self.BTN_clear.setText(_translate("DialogRingserienEingabe", "Clear"))
        self.label_2.setToolTip(_translate("DialogRingserienEingabe", "Automatisch Aufteilung der Pakete nach Anzahl Ringe pro Schnur"))
        self.label_2.setText(_translate("DialogRingserienEingabe", "Neue Pakete hinzufügen... "))
        self.label_3.setToolTip(_translate("DialogRingserienEingabe", "<html><head/><body><p><span style=\" font-weight:700;\">Start</span>nummer der <span style=\" font-weight:700;\">gesamten</span> Serie! Wurden z.B. 1000 Ringe einer Serie geliefert von XX010001 bis XX011000 in 10 Schnureinheiten (Paketen), so trägt man die erste Nummer (10.001) bei Startnummer ein und die letzte Nummer (11.000) bei Endnummer. Natürlich ohne .</p></body></html>"))
        self.label_3.setText(_translate("DialogRingserienEingabe", "Startnummer: "))
from rberi_lib import OwnTable
