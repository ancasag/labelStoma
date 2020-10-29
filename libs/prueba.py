# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog,QWidget, QPushButton, QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt
from libs.linea import DibujarLineaApp

class Ui_Dialog(object):
    genera = False

    def setupUi(self, Ui_Dialog):
        Ui_Dialog.setObjectName("Dialog")
        Ui_Dialog.resize(498, 488)
        self.dialog = Ui_Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Ui_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 440, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Ui_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 17))
        self.label.setObjectName("label")

        self.escala = QtWidgets.QLineEdit(Ui_Dialog)
        self.escala.setGeometry(QtCore.QRect(20, 70, 113, 25))
        self.escala.setObjectName("lineEdit")

        self.medidas = QtWidgets.QComboBox(Ui_Dialog)
        self.medidas.setGeometry(QtCore.QRect(150, 70, 51, 25))
        self.medidas.setObjectName("comboBox")
        self.medidas.addItem("")
        self.medidas.addItem("")
        self.medidas.addItem("")

        self.line = QtWidgets.QFrame(Ui_Dialog)
        self.line.setGeometry(QtCore.QRect(0, 110, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Ui_Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 391, 17))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(30, 180, 151, 23))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 220, 161, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 260, 131, 24))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 260, 131, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(250, 220, 211, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(250, 180, 221, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 360, 231, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 400, 171, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(250, 360, 161, 23))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Ui_Dialog)
        self.checkBox_10.setGeometry(QtCore.QRect(250, 400, 231, 23))
        self.checkBox_10.setObjectName("checkBox_10")
        self.label_4 = QtWidgets.QLabel(Ui_Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 431, 20))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Ui_Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 310, 491, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.buttonBox.accepted.connect(self.actualizar)
        self.retranslateUi(Ui_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Ui_Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter the scale and the corresponding unit:"))
        self.medidas.setItemText(0, _translate("Dialog", "cm"))
        self.medidas.setItemText(1, _translate("Dialog", "mm"))
        self.medidas.setItemText(2, _translate("Dialog", "µm"))
        #self.label_2.setText(_translate("Dialog", "px"))
        self.label_3.setText(_translate("Dialog", "Select the excel columns:"))
        self.checkBox.setText(_translate("Dialog", "Name of the image"))
        self.checkBox_2.setText(_translate("Dialog", "Number os stomata"))
        self.checkBox_3.setText(_translate("Dialog", "Average height"))
        self.checkBox_4.setText(_translate("Dialog", "Width average"))
        self.checkBox_5.setText(_translate("Dialog", "Typical deviation of height"))
        self.checkBox_6.setText(_translate("Dialog", "Typical deviation of the width"))
        self.checkBox_7.setText(_translate("Dialog", "Number stomata per surface"))
        self.checkBox_8.setText(_translate("Dialog", "Area of ​​surface"))
        self.checkBox_9.setText(_translate("Dialog", "Stomata by surface"))
        self.checkBox_10.setText(_translate("Dialog", "Height/width of each stoma"))
        self.label_4.setText(_translate("Dialog", "If you do not have a surface, the columns will be empty"))



    def actualizar(self):
        self.genera = True
        # Se lee el valor de la caja de texto
        escalas = int(self.escala.text())
        #pixeles = int(self.pixel.text())
        unidad = self.medidas.currentText()
        ch2 = self.checkBox_2.isChecked()
        ch3 = self.checkBox_3.isChecked()
        ch4 = self.checkBox_4.isChecked()
        ch5 = self.checkBox_5.isChecked()
        ch6 = self.checkBox_6.isChecked()
        ch7 = self.checkBox_7.isChecked()
        ch8 = self.checkBox_8.isChecked()
        ch9 = self.checkBox_9.isChecked()
        ch10 = self.checkBox_10.isChecked()
        # if self.escalas.setValidator(QtGui.QDoubleValidator()):
        self.esca = escalas
        # else:
        #     QtGui.QMessageBox.about(self, "The scale must be a number")
        # if self.pixeles.setValidator(QtGui.QDoubleValidator()):
        #self.pix = pixeles
        # else:
        #     QtGui.QMessageBox.about(self, "The pixels must be a number")
        self.uni = unidad
        self.che2 = ch2
        self.che3 = ch3
        self.che4 = ch4
        self.che5 = ch5
        self.che6 = ch6
        self.che7 = ch7
        self.che8 = ch8
        self.che9 = ch9
        self.che10 = ch10
        # close dialog
        self.dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
