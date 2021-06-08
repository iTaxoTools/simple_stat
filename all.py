from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import re
import sys, os
from PyQt5.uic import loadUiType
import pandas as pd
from rule3 import *
from scipy import stats
import statsmodels.stats.multitest as smt

from PyQt5.QtGui import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

FORM_CLASS,_=loadUiType(resource_path("final_all.ui"))


#FORM_CLASS,_=loadUiType(resource_path("rule3.ui"))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        super(Main,self).__init__(parent)
        self.setupUi(self)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        self.setWindowIcon(QIcon(resource_path('icon/stat.ico')))
        self.setWindowTitle("Simple stats calculator")

        self.toolButton.clicked.connect(self.firsttextchanged)
        self.toolButton_2.clicked.connect(self.secondtextchanged)
        self.pushButton_2.clicked.connect(self.fourthtextchanged)
        self.pushButton_4.clicked.connect(self.seedata)
        self.pushButton_3.clicked.connect(self.fivetextchanged)
        self.pushButton_5.clicked.connect(self.sixtextchanged)
        self.pushButton.clicked.connect(self.thirdtextchanged)
        self.pushButton_6.clicked.connect(self.seventextchanged)


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


    def closeEvent(self, event):
         close = QMessageBox.question(self, "QUIT", "Are you sure want to close the program?",QMessageBox.Yes | QMessageBox.No)
         if close == QMessageBox.Yes:
             QApplication.closeAllWindows()
             event.accept()

         else:
             event.ignore()



    def seventextchanged(self):
        try:

            xx= self.plainTextEdit_9.toPlainText()
            xx= xx.split()
            xa= [float(x) for x in xx]
            kk= float(self.comboBox_3.currentText())
            pp= str(self.comboBox_4.currentText())
            y= smt.multipletests(xa, alpha=kk, method=pp, is_sorted=False, returnsorted=False)


            text= "Corrected P-Values\n\n"
            for x in y[1]:
                x= round(x, 4)
                text += f"{x}\n\n"
            self.plainTextEdit_10.setPlainText(text)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")



    def sixtextchanged(self):
        try:

            xx= self.plainTextEdit_6.toPlainText()
            xx= xx.split()
            xa= [float(x) for x in xx]
            yy= self.plainTextEdit_7.toPlainText()
            yy= yy.split()
            ya= [float(y) for y in yy]
            from scipy.stats import mannwhitneyu
            stat1, p1 = mannwhitneyu(xa, ya, alternative="two-sided")
            from scipy.stats import wilcoxon
            #stat2, p2 = wilcoxon(xa, ya)
            from scipy.stats import ttest_ind
            stat3, p3 = ttest_ind(xa, ya, equal_var = False)

            text= "Statistics Results\n\n"

            text += f"Student’s t-Test:\nstat= {round(stat3, 4)}, p-value= {round(p3, 4)}\n\n"
            text += f"Mann-Whitney U Test:\nstat= {round(stat1, 4)}, p-value= {round(p1, 4)}\n\n"
            #text += f"Wilcoxon Signed-Rank Test:\nstat= {round(stat3, 4)}, p-value= {round(p3, 4)}\n\n"

            self.plainTextEdit_8.setPlainText(text)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")




    def fivetextchanged(self):
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


            self.plainTextEdit_5.setPlainText(xx)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")




    def fourthtextchanged(self):
        try:

            gr1= self.lineEdit_4.text()
            gr11= self.lineEdit_5.text()
            gr2= self.lineEdit_6.text()
            gr22= self.lineEdit_7.text()
            import scipy.stats as stats
            oddsratio, pvalue = stats.fisher_exact([[int(gr1), int(gr11)], [int(gr2), int(gr22)]])
            xx= f"The probability that we would observe this or an even more imbalanced ratio by chance is i.e., p-value is {round(pvalue, 10)}\n\n"
            xx+= f"A commonly used significance level is 5%\n\n"
            xx+= f"if we adopt that, we can therefore conclude that our observed imbalance is statistically significant if p-value < 0.05\n\n"

            self.plainTextEdit_4.setPlainText(xx)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")



    def secondtextchanged(self):
        try:

            xx= self.plainTextEdit_11.toPlainText()
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
            # text += f"Chi-Square Normality Test:\nstat= {round(stat3, 4)}, p-value= {round(p3, 4)}\n\n"
            text += f"Lilliefors Test for Normality:\nstat= {round(stat4, 4)}, p-value= {round(p4, 4)}\n\n"
            text += f"Jarque–Bera test for Normality:\nstat= {round(stat5, 4)}, p-value= {round(p5, 4)}\n\n"
            # text += f"Kolmogorov-Smirnov test for Normality:\nstat= {round(stat6, 4)}, p-value= {round(p6, 4)}\n\n"
            self.plainTextEdit_12.setPlainText(text)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")


    def firsttextchanged(self):
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


    def thirdtextchanged(self):
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
            xx+= f"The probability of success in each trial or subject is {pval}, and The two-tail P-value is {round(aa, 8)}\n\n"
            xx+= f"The p-value for either {int(int(trial)*float(pval))} or more successes in {trial} trials is {round(bb, 8)} and will be significant if it is less than 0.05\n\n"
            xx+= f"The p-value of observing either {int(int(trial)*float(pval))} or less successes in {trial} trials is {round(cc, 8)} and will be significant if it is less than 0.05\n\n"
            self.plainTextEdit_3.setPlainText(xx)

        except Exception as e:

            print(e)

            QMessageBox.warning(self, "Warning", f"The output not obtained because {e}")
            return
        QMessageBox.information(self, "Information", "The output data generated successfully")







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
