try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from libs.utils import newIcon, labelValidator

BB = QDialogButtonBox


class ExcelDialog(QMainWindow):

    def __init__(self, text="Generate Excel", parent=None, listItem=None):
        super(ExcelDialog, self).__init__(parent)

        self.label = QLabel()
        self.label.setGeometry(QRect(20, 20, 431, 17))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit()
        self.lineEdit.setGeometry(QRect(20, 70, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QComboBox()
        self.comboBox.setGeometry(QRect(150, 70, 51, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setGeometry(QRect(250, 70, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QLabel()
        self.label_2.setGeometry(QRect(370, 70, 21, 17))
        self.label_2.setObjectName("label_2")
        self.line = QFrame()
        self.line.setGeometry(QRect(0, 110, 491, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QLabel()
        self.label_3.setGeometry(QRect(20, 140, 391, 17))
        self.label_3.setObjectName("label_3")
        self.checkBox = QCheckBox()
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QRect(30, 180, 151, 23))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QCheckBox()
        self.checkBox_2.setGeometry(QRect(30, 220, 151, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QCheckBox()
        self.checkBox_3.setGeometry(QRect(30, 260, 131, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QCheckBox()
        self.checkBox_4.setGeometry(QRect(250, 260, 131, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QCheckBox()
        self.checkBox_5.setGeometry(QRect(250, 220, 211, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QCheckBox()
        self.checkBox_6.setGeometry(QRect(250, 180, 221, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QCheckBox()
        self.checkBox_7.setGeometry(QRect(30, 360, 231, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QCheckBox()
        self.checkBox_8.setGeometry(QRect(30, 400, 171, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QCheckBox()
        self.checkBox_9.setGeometry(QRect(250, 360, 161, 23))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QCheckBox()
        self.checkBox_10.setGeometry(QRect(250, 400, 231, 23))
        self.checkBox_10.setObjectName("checkBox_10")
        self.label_4 = QLabel()
        self.label_4.setGeometry(QRect(20, 330, 271, 20))
        font = QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QFrame()
        self.line_2.setGeometry(QRect(0, 310, 491, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QPushButton()
        self.pushButton.setGeometry(QRect(258, 70, 61, 25))
        self.pushButton.setObjectName("push")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter the scale, the unit and the corresponding pixels:"))
        self.comboBox.setItemText(0, _translate("Dialog", "cm"))
        self.comboBox.setItemText(1, _translate("Dialog", "mm"))
        self.comboBox.setItemText(2, _translate("Dialog", "µm"))
        self.label_2.setText(_translate("Dialog", "px"))
        self.label_3.setText(_translate("Dialog", "Select the excel columns:"))
        self.checkBox.setText(_translate("Dialog", "Name of the image"))
        self.checkBox_2.setText(_translate("Dialog", "Number os stomas"))
        self.checkBox_3.setText(_translate("Dialog", "Average height"))
        self.checkBox_4.setText(_translate("Dialog", "Width average"))
        self.checkBox_5.setText(_translate("Dialog", "Typical deviation of height"))
        self.checkBox_6.setText(_translate("Dialog", "Typical deviation of the width"))
        self.checkBox_7.setText(_translate("Dialog", "Number stomas per surface"))
        self.checkBox_8.setText(_translate("Dialog", "Area of ​​surface"))
        self.checkBox_9.setText(_translate("Dialog", "Stomas by surface"))
        self.checkBox_10.setText(_translate("Dialog", "Height/width of each stoma2"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print
            self.cb.itemText(count)
        print("Current index", i, "selection changed ", self.cb.currentText())

    def validate(self):
        try:
            if self.edit.text().trimmed():
                self.accept()
        except AttributeError:
            # PyQt5: AttributeError: 'str' object has no attribute 'trimmed'
            if self.edit.text().strip():
                self.accept()

    def postProcess(self):
        try:
            self.edit.setText(self.edit.text().trimmed())
        except AttributeError:
            # PyQt5: AttributeError: 'str' object has no attribute 'trimmed'
            self.edit.setText(self.edit.text())

    def popUp(self, text='', move=True):
        self.edit.setText(text)
        self.edit.setSelection(0, len(text))
        self.edit.setFocus(Qt.PopupFocusReason)
        if move:
            self.move(QCursor.pos())
        return self.edit.text() if self.exec_() else None

    def listItemClick(self, tQListWidgetItem):
        try:
            text = tQListWidgetItem.text().trimmed()
        except AttributeError:
            # PyQt5: AttributeError: 'str' object has no attribute 'trimmed'
            text = tQListWidgetItem.text().strip()
        self.edit.setText(text)

    def listItemDoubleClick(self, tQListWidgetItem):
        self.listItemClick(tQListWidgetItem)
        self.validate()
