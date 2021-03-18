# -*- encoding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd
from scipy import stats
from PyQt5.QtGui import *

import statsmodels.stats.multitest as smt

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



FORM_CLASS,_=loadUiType(resource_path("seven.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Bonferroni correction")
        #self.plainTextEdit.setPlaceholderText()

        self.pushButton.clicked.connect(self.textchanged)

    def textchanged(self):
        try:

            xx= self.plainTextEdit.toPlainText()
            xx= xx.split()
            xa= [float(x) for x in xx]
            kk= float(self.comboBox_2.currentText())
            pp= str(self.comboBox_4.currentText())
            y= smt.multipletests(xa, alpha=kk, method=pp, is_sorted=False, returnsorted=False)


            text= "Corrected P-Values\n\n"
            for x in y[1]:
                x= round(x, 4)
                text += f"{x}\n\n"
            self.plainTextEdit_2.setPlainText(text)

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
