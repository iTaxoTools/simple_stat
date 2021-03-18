# -*- encoding:utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType

#import pylab
from PyQt5.QtGui import *
from scipy import stats
import matplotlib.pyplot as plt

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


FORM_CLASS,_=loadUiType(resource_path("second.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Test for normality")

        #self.plainTextEdit_2.setPlaceholderText()
        self.toolButton.clicked.connect(self.textchanged)

    def textchanged(self):
        try:

            xx= self.plainTextEdit_2.toPlainText()
            xx= xx.split()
            xa= [float(x) for x in xx]

            from scipy import stats
            from scipy.stats import shapiro
            stat1, p1 = shapiro(xa)
            #print('Statistics=%.3f, p=%.3f' % (stat, p))
            from scipy.stats import normaltest
            stat2, p2 = normaltest(xa)
            #print('Statistics=%.3f, p=%.3f' % (stat, p))
            from scipy.stats import chisquare
            stat3, p3 = chisquare(xa)
            from statsmodels.stats.diagnostic import lilliefors
            stat4, p4= lilliefors(xa)
            from scipy.stats import jarque_bera
            stat5, p5 = jarque_bera(xa)
            from scipy.stats import kstest
            stat6, p6= kstest(xa, "norm")
            from scipy.stats import skew
            val1= round(skew(xa), 3)
            from scipy.stats import kurtosis
            val2= round(kurtosis(xa), 3)
            import statistics
            mm=  f'{round(statistics.mean(xa), 3)} ± {round(statistics.stdev(xa), 3)}'
            text= f"Count of data is {len(xa)}\n\n"

            text += f"Mean ± standard deviation: {mm}\n\n"
            text += f"skewness = {val1}\n"
            text += f"kurtosis = {val2}\n\n"
            text += f"Shapiro-Wilk Test:\nstat= {round(stat1, 4)}, p-value= {round(p1, 4)}\n\n"
            text += f"D’Agostino’s K-squared test:\nstat= {round(stat2, 4)}, p-value= {round(p2, 4)}\n\n"
            text += f"Chi-Square Normality Test:\nstat= {round(stat3, 4)}, p-value= {round(p3, 4)}\n\n"
            text += f"Lilliefors Test for Normality:\nstat= {round(stat4, 4)}, p-value= {round(p4, 4)}\n\n"
            text += f"Jarque–Bera test for Normality:\nstat= {round(stat5, 4)}, p-value= {round(p5, 4)}\n\n"
            text += f"Kolmogorov-Smirnov test for Normality:\nstat= {round(stat6, 4)}, p-value= {round(p6, 4)}\n\n"
            self.plainTextEdit.setPlainText(text)

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
