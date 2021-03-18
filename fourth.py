# -*- encoding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd

from PyQt5.QtGui import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS,_=loadUiType(resource_path("fourth.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Fisher's exact test")
        self.pushButton.clicked.connect(self.textchanged)

    def textchanged(self):
        try:

            gr1= self.lineEdit.text()
            gr11= self.lineEdit_2.text()
            gr2= self.lineEdit_3.text()
            gr22= self.lineEdit_4.text()
            import scipy.stats as stats
            oddsratio, pvalue = stats.fisher_exact([[int(gr1), int(gr11)], [int(gr2), int(gr22)]])
            xx= f"The probability that we would observe this or an even more imbalanced ratio by chance is i.e., p-value is {round(pvalue, 4)}\n\n"
            xx+= f"A commonly used significance level is 5%\n\n"
            xx+= f"if we adopt that, we can therefore conclude that our observed imbalance is statistically significant if p-value < 0.05 else insignificant\n\n"

            self.plainTextEdit.setPlainText(xx)

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
