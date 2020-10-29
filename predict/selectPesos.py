# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detectPesos.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    genera = False
    def setupUi(self, Ui_Dialog):
        Ui_Dialog.setObjectName("Dialog")
        Ui_Dialog.resize(384, 236)
        self.dialog = Ui_Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Ui_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Ui_Dialog)
        self.label.setGeometry(QtCore.QRect(26, 10, 311, 41))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Ui_Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 60, 141, 23))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Ui_Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 100, 381, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Ui_Dialog)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 113, 25))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(Ui_Dialog)
        self.buttonBox.accepted.connect(self.actualizar)
        QtCore.QMetaObject.connectSlotsByName(Ui_Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "What weights are you going to use to detect?"))
        self.radioButton.setText(_translate("Dialog", "Default weights"))
        self.radioButton_2.setText(_translate("Dialog", "Your own weights (Select the confidence)"))
        self.lineEdit.setText(_translate("Dialog", "0.4"))

    def actualizar(self):
        self.genera = True


        default = self.radioButton.isChecked()
        our = self.radioButton_2.isChecked()
        le1 = self.lineEdit.text()
        self.default_1 = default
        self.our_1 = our
        self.le_1 = le1
        self.dialog.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
