# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rule3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 598)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.b11 = QtWidgets.QRadioButton(self.splitter)
        self.b11.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.b11.setObjectName("b11")
        self.b22 = QtWidgets.QRadioButton(self.splitter)
        self.b22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b22.setAutoFillBackground(True)
        self.b22.setObjectName("b22")
        self.verticalLayout_10.addWidget(self.splitter)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b1 = QtWidgets.QRadioButton(Dialog)
        self.b1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b1.setAutoFillBackground(False)
        self.b1.setStyleSheet("")
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.l1 = QtWidgets.QLineEdit(Dialog)
        self.l1.setMaximumSize(QtCore.QSize(130, 16777215))
        self.l1.setObjectName("l1")
        self.horizontalLayout.addWidget(self.l1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMaximumSize(QtCore.QSize(100, 100))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(resource_path("icon/rule3a.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.splitter_3 = QtWidgets.QSplitter(Dialog)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.b2 = QtWidgets.QRadioButton(self.splitter_3)
        self.b2.setMaximumSize(QtCore.QSize(20, 20))
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.l2 = QtWidgets.QLineEdit(self.splitter_3)
        self.l2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.l2.setObjectName("l2")
        self.verticalLayout.addWidget(self.splitter_3)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setMaximumSize(QtCore.QSize(100, 100))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(resource_path("icon/rule3b.png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.splitter_4 = QtWidgets.QSplitter(Dialog)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.b3 = QtWidgets.QRadioButton(self.splitter_4)
        self.b3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.l3 = QtWidgets.QLineEdit(self.splitter_4)
        self.l3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.l3.setObjectName("l3")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMaximumSize(QtCore.QSize(100, 100))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(resource_path("icon/rule3c.png")))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMaximumSize(QtCore.QSize(300, 30))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.splitter_5 = QtWidgets.QSplitter(Dialog)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.b4 = QtWidgets.QRadioButton(self.splitter_5)
        self.b4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.b4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.l4 = QtWidgets.QLineEdit(self.splitter_5)
        self.l4.setMaximumSize(QtCore.QSize(130, 16777215))
        self.l4.setObjectName("l4")
        self.verticalLayout_3.addWidget(self.splitter_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMaximumSize(QtCore.QSize(100, 100))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(resource_path("icon/rule3d.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.p = QtWidgets.QPushButton(Dialog)
        self.p.setObjectName("p")
        self.verticalLayout_11.addWidget(self.p)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Rule of Three"))
        self.label_2.setText(_translate("Dialog", "Calculator"))
        self.label_3.setText(_translate("Dialog", "Type of proportions:"))
        self.b11.setText(_translate("Dialog", "Direct (if magnitude increases, the other one also increases)(default)"))
        self.b22.setText(_translate("Dialog", "Inverse (if magnitude increases, the other one decreases)"))
        self.label_4.setText(_translate("Dialog", "If the quantity"))
        self.label_5.setText(_translate("Dialog", "corresponds to:"))
        self.label_6.setText(_translate("Dialog", "Then, the following quantity"))
        self.label_7.setText(_translate("Dialog", "correspond to:"))
        self.p.setText(_translate("Dialog", "Calculate"))
