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

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS,_=loadUiType(resource_path("six.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Compare two independent samples (t-Test and U-test)")
        #self.plainTextEdit_2.setPlaceholderText('Paste here the first set of values.')

        #self.plainTextEdit.setPlaceholderText()

        self.pushButton.clicked.connect(self.textchanged)


    def textchanged(self):
        try:

            xx= self.plainTextEdit.toPlainText()
            xx= xx.split()
            xa= [float(x) for x in xx]
            yy= self.plainTextEdit_2.toPlainText()
            yy= yy.split()
            ya= [float(y) for y in yy]
            from scipy.stats import mannwhitneyu
            stat1, p1 = mannwhitneyu(xa, ya)
            from scipy.stats import wilcoxon
            stat2, p2 = wilcoxon(xa, ya)
            from scipy.stats import ttest_ind
            stat3, p3 = ttest_ind(xa, ya)

            text= "Statistics Results\n\n"

            text += f"Student’s t-Test:\nstat= {round(stat1, 4)}, p-value= {round(p1, 4)}\n\n"
            text += f"Mann-Whitney U Test:\nstat= {round(stat2, 4)}, p-value= {round(p2, 4)}\n\n"
            text += f"Wilcoxon Signed-Rank Test:\nstat= {round(stat3, 4)}, p-value= {round(p3, 4)}\n\n"

            self.plainTextEdit_3.setPlainText(text)

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
