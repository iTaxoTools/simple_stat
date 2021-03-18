# -*- encoding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd
from rule3 import *

from PyQt5.QtGui import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


#FORM_CLASS,_=loadUiType(resource_path("rule3.ui"))

class Main(QDialog, Ui_Dialog):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Rule of three")
        self.a1 = QButtonGroup(self)

        self.a1.addButton(self.b11)
        self.a1.addButton(self.b22)
        self.b11.setAutoExclusive(True)
        self.b22.setAutoExclusive(True)
        self.a2 = QButtonGroup(self)
        self.a2.addButton(self.b1)
        self.a2.addButton(self.b2)
        self.a2.addButton(self.b3)
        self.a2.addButton(self.b4)


        self.b1.setAutoExclusive(True)
        self.b2.setAutoExclusive(True)
        self.b3.setAutoExclusive(True)
        self.b4.setAutoExclusive(True)


        self.b1.toggled.connect(self.state1)
        self.b2.toggled.connect(self.state2)
        self.b3.toggled.connect(self.state3)
        self.b4.toggled.connect(self.state4)
        self.p.clicked.connect(self.trigger1)


    def trigger1(self):

        if self.b11.isChecked() == True:

            self.download2()
        else:
            self.download1()



    def state1(self):
        if self.b1.isChecked():

            self.l1.setEnabled(False)
            self.l2.setEnabled(True)
            self.l3.setEnabled(True)
            self.l4.setEnabled(True)


    def state2(self):
        if self.b2.isChecked():
            self.l2.setEnabled(False)
            self.l1.setEnabled(True)
            self.l3.setEnabled(True)
            self.l4.setEnabled(True)


    def state3(self):
        if self.b3.isChecked():
            self.l3.setEnabled(False)
            self.l1.setEnabled(True)
            self.l2.setEnabled(True)
            self.l4.setEnabled(True)


    def state4(self):
        if self.b4.isChecked():
            self.l4.setEnabled(False)
            self.l3.setEnabled(True)
            self.l2.setEnabled(True)
            self.l1.setEnabled(True)


    def download2(self):
        try:

            l1= None
            l2= None
            l3= None
            l4= None
            if self.l2.text(): l2=float(self.l2.text())
            if self.l1.text(): l1=float(self.l1.text())
            if self.l3.text(): l3=float(self.l3.text())
            if self.l4.text(): l4=float(self.l4.text())
            xx= [self.b1, self.b2, self.b3, self.b4]

            if xx[0].isChecked():

                l1= (l3/l4)*l2
                self.l1.setStyleSheet("color: black;")
                self.l1.setText(str(round(l1, 5)))

            if xx[1].isChecked():

                l2= (l4/l3)*l1
                self.l2.setStyleSheet("color: black;")
                self.l2.setText(str(round(l2, 5)))


            if xx[2].isChecked():

                l3= (l1/l2)*l4
                self.l3.setStyleSheet("color: black;")
                self.l3.setText(str(round(l3, 5)))


            if xx[3].isChecked():

                l4= (l2/l1)*l3
                self.l4.setStyleSheet("color: black;")
                self.l4.setText(str(round(l4, 5)))

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")


    def download1(self):

        try:

            l1= None
            l2= None
            l3= None
            l4= None
            if self.l2.text(): l2=float(self.l2.text())
            if self.l1.text(): l1=float(self.l1.text())
            if self.l3.text(): l3=float(self.l3.text())
            if self.l4.text(): l4=float(self.l4.text())
            xx= [self.b1, self.b2, self.b3, self.b4]

            if xx[0].isChecked():

                l1= (l4/l3)*l2
                self.l1.setStyleSheet("color: black;")
                self.l1.setText(str(round(l1, 5)))

            if xx[1].isChecked():

                l2= (l3/l4)*l1
                self.l2.setStyleSheet("color: black;")
                self.l2.setText(str(round(l2, 5)))

            if xx[2].isChecked():

                l3= (l2/l1)*l4
                self.l3.setStyleSheet("color: black;")
                self.l3.setText(str(round(l3, 5)))

            if xx[3].isChecked():
                self.l4.setText("")
                l4= (l1/l2)*l3
                print(l4)
                self.l4.setStyleSheet("color: black;")
                self.l4.setText(str(round(l4, 5)))

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")



def main1():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':

    main1()
