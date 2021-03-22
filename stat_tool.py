from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import re
import sys, os
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Label(QLabel):
    def __init__(self, img):
        super(Label, self).__init__()
        self.setFrameStyle(QFrame.StyledPanel)
        self.pixmap = QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QPainter(self)
        point = QPoint(0,0)
        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        # start painting the label from left upper corner
        point.setX(size.width())
        point.setY(size.height())

        painter.drawPixmap(point, scaledPix)

class DlgMain(QDialog):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.resize(900, 900)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        self.setWindowIcon(QIcon(resource_path('icons/stat.ico')))
        self.setWindowTitle("Simple stats calculator")


        ######  Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(1)
        self.trwQt.setHeaderLabels(["Stats Tools"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_dblClicked)

        self.populateTree()

        #self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.setColumnWidth(0, 150)
        self.trwQt.expandItem(self.twistart)



        self.graph1= QGraphicsView()
        self.lytMain = QHBoxLayout()
        self.lytTree = QVBoxLayout()
        self.lbl = QLabel()
        self.lbl.setMaximumSize(QSize(100, 80))
        self.lbl.setText("")
        self.lbl.setPixmap(QPixmap(resource_path("icons/copy_21mm.png")))
        self.lbl.setScaledContents(True)
        self.lbl.setObjectName("label_42")
        self.lytTree.addWidget(self.lbl)
        self.lytTree.addWidget(self.trwQt)



        self.lytWev = QVBoxLayout()
        self.lytWev.addWidget(self.graph1)
        self.lytMain.addLayout(self.lytTree, 40)
        self.lytMain.addLayout(self.lytWev, 60)
        self.setLayout(self.lytMain)


    def closeEvent(self, event):
         close = QMessageBox.question(self, "QUIT", "Are you sure want to close program?",QMessageBox.Yes | QMessageBox.No)
         if close == QMessageBox.Yes:
             QApplication.closeAllWindows()
             event.accept()

         else:
             event.ignore()

    def populateTree(self):
        ##### Create top level items

        self.twistart = QTreeWidgetItem(self.trwQt, ["Start"])

        lsttools = ["Descriptive statistics", "Test for normality", "Binomial test", "Fisher's exact test", "Chi-square test", "Compare two independent samples (t-Test and U-test)", "Bonferroni correction", "Rule of Three"]
        for cls in lsttools:
            self.twistart.addChild(QTreeWidgetItem([cls]))


        ##### Add subitems to Qdialog
        twi = self.trwQt.findItems("Descriptive statistics", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        ###### add subitems to QFrame
        twi = self.trwQt.findItems("Test for normality", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))


        twi = self.trwQt.findItems("Binomial test", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        twi = self.trwQt.findItems("Fisher's exact test", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        twi = self.trwQt.findItems("Chi-square test", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        twi = self.trwQt.findItems("Compare two independent samples (t-Test and U-test)", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        twi = self.trwQt.findItems("Bonferroni correction", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        twi = self.trwQt.findItems("Rule of Three", Qt.MatchRecursive)[0]
        lstQDialog = ["Launch Tool", "Help Documentation"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))



    #####  Event handlers
    def evt_trwQt_dblClicked(self, twi, col):
        try:
            if twi.parent().text(0) == "Descriptive statistics":
                if twi.text(0) == "Help Documentation":


                    f = open(resource_path("help1.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()

                if twi.text(0)=="Launch Tool":
                    import first_1
                    self.window2 = first_1.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Test for normality":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help2.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()

                if twi.text(0)=="Launch Tool":
                    import second
                    self.window2 = second.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Binomial test":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()

                if twi.text(0)=="Launch Tool":
                    import third
                    self.window2 = third.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Fisher's exact test":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()

                if twi.text(0)=="Launch Tool":
                    import fourth
                    self.window2 = fourth.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Chi-square test":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()


                if twi.text(0)=="Launch Tool":
                    import five
                    self.window2 = five.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Compare two independent samples (t-Test and U-test)":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help6.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()


                if twi.text(0)=="Launch Tool":
                    import six_tool
                    self.window2 = six_tool.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()


            if twi.parent().text(0) == "Bonferroni correction":
                if twi.text(0) == "Help Documentation":
                    f = open(resource_path("help7.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()


                if twi.text(0)=="Launch Tool":
                    import seven
                    self.window2 = seven.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()



            if twi.parent().text(0) == "Rule of Three":
                if twi.text(0) == "Help Documentation":


                    f = open(resource_path("help.txt"), "rt")
                    mytext1 = QGraphicsSimpleTextItem(f.read())
                    self.scene = QGraphicsScene()
                    self.scene.addItem(mytext1)

                    self.graph1.setScene(self.scene)
                    f.close()

                if twi.text(0)=="Launch Tool":
                    import eight
                    self.window2 = eight.Main()
                    qr = self.frameGeometry()
                    cp = QDesktopWidget().availableGeometry().center()
                    qr.moveCenter(cp)
                    self.window2.move(qr.topLeft())
                    self.window2.setWindowState(self.window2.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                    self.window2.activateWindow()
                    self.window2.show()


        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Warning", f"The output  is not obtained because {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    QApplication.processEvents()
    app.exec_()
