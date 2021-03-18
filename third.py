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


FORM_CLASS,_=loadUiType(resource_path("third.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Binomial test")
        self.pushButton.clicked.connect(self.textchanged)

    def textchanged(self):
        try:

            success= self.lineEdit.text()
            trial= self.lineEdit_2.text()
            pval= self.lineEdit_3.text()
            from scipy.stats import binom_test
            aa= binom_test(x= float(success), n=float(trial), p=float(pval), alternative="two-sided")
            bb= binom_test(x= float(success), n=float(trial), p=float(pval), alternative='greater')
            cc= binom_test(x= float(success), n=float(trial), p=float(pval), alternative='less')
            xx= f"Number of successes: {success}\n\n"
            xx+= f"Number of trials (or subjects) per experiment: {trial}\n\n"
            xx+= f"The probability of success in each trial or subject is {pval}, and The two-tail P value is {round(aa, 4)}\n\n"
            xx+= f"The p-value for either {int(int(trial)*float(pval))} or more successes in {trial} trials is {round(bb, 4)} and will be significant if it is less than 0.05\n\n"
            xx+= f"The p-value of observing either {int(int(trial)*float(pval))} or less successes in {trial} trials is {round(cc, 4)} will be significant if it is less than 0.05\n\n"
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
