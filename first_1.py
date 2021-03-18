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


FORM_CLASS,_=loadUiType(resource_path("first.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Descriptive statistics")
        self.toolButton.clicked.connect(self.textchanged)
        #self.plainTextEdit_2.setPlaceholderText()



    def textchanged(self):
        try:

            xx= self.plainTextEdit_2.toPlainText()
            xx= xx.split()
            xa= [int(x) for x in xx]
            xx= pd.DataFrame({"Descriptive_analysis": xa})
            xx= xx.describe()
            xx= xx.rename(index={"count": 'Count', "std": 'StdDev', "mean":  'Mean', "min": 'Min', '25%':'25% Quartile', '50%':'Median', '75%':'75% Quartile', "max":"Max"})
            from scipy import stats
            kk= stats.sem(xa, axis=None, ddof=0)
            sum1= sum(xa)
            import statistics
            mm=  f'{round(statistics.mean(xa), 3)} ± {round(statistics.stdev(xa), 3)}'
            xx.loc["standard error", "Descriptive_analysis"]= kk
            xx.loc["sum", "Descriptive_analysis"]= sum1

            xx['Descriptive_analysis']= xx['Descriptive_analysis'].map(lambda x: str(round(float(x), 3)))
            xx.loc["Mean±stdev", "Descriptive_analysis"]= mm

            self.plainTextEdit.setPlainText(str(xx.astype(str)))

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
