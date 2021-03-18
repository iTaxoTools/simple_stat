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


FORM_CLASS,_=loadUiType(resource_path("five.ui"))

class Main(QDialog, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Chi-square test")
        self.pushButton_2.clicked.connect(self.textchanged)
        self.pushButton.clicked.connect(self.seedata)

    def textchanged(self):
        row= int(self.comboBox.currentText())
        col= int(self.comboBox_2.currentText())
        self.model = QtGui.QStandardItemModel(row,col,self)
        self.tableView.setModel(self.model)


    def seedata(self):
        try:

            model = self.tableView.model()
            data = []
            for row in range(model.rowCount()):

                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(int(model.data(index)))
            print(data)
            import numpy as np
            dice = np.array(data)
            chi2_stat, p_val, dof, ex = stats.chi2_contingency(dice)
            xx= f"The chi2_stat is {round(chi2_stat, 4)}\n\n"
            xx+= f"The degrees of freedom is {dof}\n\n"
            xx+= f"The p-value is {p_val}\n\n"


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
