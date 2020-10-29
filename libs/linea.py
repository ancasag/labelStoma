from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog,QWidget, QPushButton, QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QPen
from PyQt5.Qt import Qt
#from libs.prueba import Ui_Dialog

class DibujarLineaApp(QDialog):

    def __init__(self):
        super().__init__()
        print('PyQt5 button click')
        #ui = Ui_Dialog()
        self.posicion_1 = [0,0]
        self.posicion_2 = [0, 0]
        #self.show()

    def mousePressEvent(self, event):
        print('he entrado aquiiiiii')
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()


    def mouseReleaseEvent(self, event):
        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()
        self.update()


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])
        painter.end()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ventana = DibujarLineaApp()
    ventana.show()
    #Dialog = QtWidgets.QDialog()
    sys.exit(app.exec_())