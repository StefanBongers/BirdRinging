# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beringungsoberflaeche\artenverwaltung\artenverwaltung\dialog_toleranzen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(374, 638)
        self.BTN_speichern = QtWidgets.QPushButton(Dialog)
        self.BTN_speichern.setGeometry(QtCore.QRect(10, 600, 141, 24))
        self.BTN_speichern.setObjectName("BTN_speichern")
        self.BTN_abbruch = QtWidgets.QPushButton(Dialog)
        self.BTN_abbruch.setGeometry(QtCore.QRect(220, 600, 141, 24))
        self.BTN_abbruch.setObjectName("BTN_abbruch")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 50, 351, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 14, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 13, 1, 1, 1)
        self.CHB_masse_anzeigen = QtWidgets.QCheckBox(self.layoutWidget)
        self.CHB_masse_anzeigen.setObjectName("CHB_masse_anzeigen")
        self.gridLayout.addWidget(self.CHB_masse_anzeigen, 12, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 12, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        self.INP_masse_mw = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_masse_mw.setObjectName("INP_masse_mw")
        self.gridLayout.addWidget(self.INP_masse_mw, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.INP_quot_stdab = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_quot_stdab.setObjectName("INP_quot_stdab")
        self.gridLayout.addWidget(self.INP_quot_stdab, 15, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.BTN_fluegel_diag = QtWidgets.QToolButton(self.layoutWidget)
        self.BTN_fluegel_diag.setCheckable(False)
        self.BTN_fluegel_diag.setObjectName("BTN_fluegel_diag")
        self.gridLayout_3.addWidget(self.BTN_fluegel_diag, 0, 2, 2, 1)
        self.INP_fluegel_tol_neg = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_fluegel_tol_neg.setObjectName("INP_fluegel_tol_neg")
        self.gridLayout_3.addWidget(self.INP_fluegel_tol_neg, 1, 0, 1, 1)
        self.INP_fluegel_tol_pos = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_fluegel_tol_pos.setObjectName("INP_fluegel_tol_pos")
        self.gridLayout_3.addWidget(self.INP_fluegel_tol_pos, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 7, 1, 1, 1)
        self.INP_masse_stdab = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_masse_stdab.setObjectName("INP_masse_stdab")
        self.gridLayout.addWidget(self.INP_masse_stdab, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.INP_fluegel_stdab = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_fluegel_stdab.setObjectName("INP_fluegel_stdab")
        self.gridLayout.addWidget(self.INP_fluegel_stdab, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.BTN_teilfeder_diag = QtWidgets.QToolButton(self.layoutWidget)
        self.BTN_teilfeder_diag.setCheckable(False)
        self.BTN_teilfeder_diag.setObjectName("BTN_teilfeder_diag")
        self.gridLayout_2.addWidget(self.BTN_teilfeder_diag, 0, 2, 2, 1)
        self.INP_teilfeder_tol_neg = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_teilfeder_tol_neg.setObjectName("INP_teilfeder_tol_neg")
        self.gridLayout_2.addWidget(self.INP_teilfeder_tol_neg, 1, 0, 1, 1)
        self.INP_teilfeder_tol_pos = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_teilfeder_tol_pos.setObjectName("INP_teilfeder_tol_pos")
        self.gridLayout_2.addWidget(self.INP_teilfeder_tol_pos, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 16, 0, 1, 1)
        self.INP_teilfeder_mw = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_teilfeder_mw.setObjectName("INP_teilfeder_mw")
        self.gridLayout.addWidget(self.INP_teilfeder_mw, 0, 1, 1, 1)
        self.INP_fluegel_mw = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_fluegel_mw.setObjectName("INP_fluegel_mw")
        self.gridLayout.addWidget(self.INP_fluegel_mw, 4, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 1, 1, 1)
        self.BTN_masse_diag = QtWidgets.QToolButton(self.layoutWidget)
        self.BTN_masse_diag.setCheckable(False)
        self.BTN_masse_diag.setObjectName("BTN_masse_diag")
        self.gridLayout_4.addWidget(self.BTN_masse_diag, 0, 2, 2, 1)
        self.INP_masse_tol_neg = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_masse_tol_neg.setObjectName("INP_masse_tol_neg")
        self.gridLayout_4.addWidget(self.INP_masse_tol_neg, 1, 0, 1, 1)
        self.INP_masse_tol_pos = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_masse_tol_pos.setObjectName("INP_masse_tol_pos")
        self.gridLayout_4.addWidget(self.INP_masse_tol_pos, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 11, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.INP_quot_mw = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_quot_mw.setObjectName("INP_quot_mw")
        self.gridLayout.addWidget(self.INP_quot_mw, 14, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_5.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 1, 1, 1)
        self.BTN_quot_diag = QtWidgets.QToolButton(self.layoutWidget)
        self.BTN_quot_diag.setCheckable(False)
        self.BTN_quot_diag.setObjectName("BTN_quot_diag")
        self.gridLayout_5.addWidget(self.BTN_quot_diag, 0, 2, 2, 1)
        self.INP_quot_tol_neg = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_quot_tol_neg.setObjectName("INP_quot_tol_neg")
        self.gridLayout_5.addWidget(self.INP_quot_tol_neg, 1, 0, 1, 1)
        self.INP_quot_tol_pos = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_quot_tol_pos.setObjectName("INP_quot_tol_pos")
        self.gridLayout_5.addWidget(self.INP_quot_tol_pos, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 16, 1, 1, 1)
        self.INP_teilfeder_stdab = QtWidgets.QLineEdit(self.layoutWidget)
        self.INP_teilfeder_stdab.setObjectName("INP_teilfeder_stdab")
        self.gridLayout.addWidget(self.INP_teilfeder_stdab, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 15, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 17, 0, 1, 1)
        self.CHB_quot_anzeigen = QtWidgets.QCheckBox(self.layoutWidget)
        self.CHB_quot_anzeigen.setObjectName("CHB_quot_anzeigen")
        self.gridLayout.addWidget(self.CHB_quot_anzeigen, 17, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.INP_teilfeder_mw, self.INP_teilfeder_stdab)
        Dialog.setTabOrder(self.INP_teilfeder_stdab, self.INP_teilfeder_tol_neg)
        Dialog.setTabOrder(self.INP_teilfeder_tol_neg, self.INP_teilfeder_tol_pos)
        Dialog.setTabOrder(self.INP_teilfeder_tol_pos, self.INP_fluegel_mw)
        Dialog.setTabOrder(self.INP_fluegel_mw, self.INP_fluegel_stdab)
        Dialog.setTabOrder(self.INP_fluegel_stdab, self.INP_fluegel_tol_neg)
        Dialog.setTabOrder(self.INP_fluegel_tol_neg, self.INP_fluegel_tol_pos)
        Dialog.setTabOrder(self.INP_fluegel_tol_pos, self.INP_masse_mw)
        Dialog.setTabOrder(self.INP_masse_mw, self.INP_masse_stdab)
        Dialog.setTabOrder(self.INP_masse_stdab, self.INP_masse_tol_neg)
        Dialog.setTabOrder(self.INP_masse_tol_neg, self.INP_masse_tol_pos)
        Dialog.setTabOrder(self.INP_masse_tol_pos, self.CHB_masse_anzeigen)
        Dialog.setTabOrder(self.CHB_masse_anzeigen, self.INP_quot_mw)
        Dialog.setTabOrder(self.INP_quot_mw, self.INP_quot_stdab)
        Dialog.setTabOrder(self.INP_quot_stdab, self.INP_quot_tol_neg)
        Dialog.setTabOrder(self.INP_quot_tol_neg, self.INP_quot_tol_pos)
        Dialog.setTabOrder(self.INP_quot_tol_pos, self.CHB_quot_anzeigen)
        Dialog.setTabOrder(self.CHB_quot_anzeigen, self.BTN_speichern)
        Dialog.setTabOrder(self.BTN_speichern, self.BTN_abbruch)
        Dialog.setTabOrder(self.BTN_abbruch, self.BTN_teilfeder_diag)
        Dialog.setTabOrder(self.BTN_teilfeder_diag, self.BTN_fluegel_diag)
        Dialog.setTabOrder(self.BTN_fluegel_diag, self.BTN_masse_diag)
        Dialog.setTabOrder(self.BTN_masse_diag, self.BTN_quot_diag)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.BTN_speichern.setText(_translate("Dialog", "Speichern und Schließen"))
        self.BTN_abbruch.setText(_translate("Dialog", "Abbruch"))
        self.label_16.setText(_translate("Dialog", "Toleranzwerte:"))
        self.label_18.setText(_translate("Dialog", "Quotient - Teilfeder : Flügel:"))
        self.CHB_masse_anzeigen.setText(_translate("Dialog", "anzeigen"))
        self.label_17.setText(_translate("Dialog", "Gewicht - Toleranzfehler:"))
        self.label.setText(_translate("Dialog", "Teilfeder-Mittelwert:"))
        self.label_2.setText(_translate("Dialog", "Teilfeder-Standardabweichung:"))
        self.label_12.setText(_translate("Dialog", "kleiner:"))
        self.label_13.setText(_translate("Dialog", "größer:"))
        self.BTN_fluegel_diag.setText(_translate("Dialog", "..."))
        self.label_6.setText(_translate("Dialog", "Flügellänge - Standardabw."))
        self.label_7.setText(_translate("Dialog", "Gewicht - Toleranzfenster\n"
"(Faktor Standardabw.)"))
        self.label_4.setText(_translate("Dialog", "Flügellänge - Toleranzfenster\n"
"(Faktor Standardabw.)"))
        self.label_10.setText(_translate("Dialog", "kleiner:"))
        self.label_11.setText(_translate("Dialog", "größer:"))
        self.BTN_teilfeder_diag.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "Teilfeder-Toleranzfenster\n"
"(Faktor Standardabweichung)"))
        self.label_21.setText(_translate("Dialog", "Quotient - Teilfeder : Flügel\n"
"(Faktor):"))
        self.label_14.setText(_translate("Dialog", "kleiner:"))
        self.label_15.setText(_translate("Dialog", "größer:"))
        self.BTN_masse_diag.setText(_translate("Dialog", "..."))
        self.label_9.setText(_translate("Dialog", "Gewicht - Mittelwert:"))
        self.label_8.setText(_translate("Dialog", "Gewicht - Standardabw."))
        self.label_19.setText(_translate("Dialog", "kleiner:"))
        self.label_20.setText(_translate("Dialog", "größer:"))
        self.BTN_quot_diag.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "Flügellänge - Mittelwert:"))
        self.label_22.setText(_translate("Dialog", "Quotient - Std.Abw.:"))
        self.label_23.setText(_translate("Dialog", "Quotient - Toleranzfehler:"))
        self.CHB_quot_anzeigen.setText(_translate("Dialog", "anzeigen"))
