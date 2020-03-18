# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D_MainWindow(object):
    def setupUi(self, D_MainWindow):
        D_MainWindow.setObjectName("D_MainWindow")
        D_MainWindow.setEnabled(True)
        D_MainWindow.resize(345, 255)
        self.centralwidget = QtWidgets.QWidget(D_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 321, 101))
        self.groupBox.setObjectName("groupBox")
        self.label_productCode = QtWidgets.QLabel(self.groupBox)
        self.label_productCode.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_productCode.setObjectName("label_productCode")
        self.lineEdit_productCode = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_productCode.setGeometry(QtCore.QRect(90, 30, 111, 20))
        self.lineEdit_productCode.setObjectName("lineEdit_productCode")
        self.label_printingType = QtWidgets.QLabel(self.groupBox)
        self.label_printingType.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_printingType.setObjectName("label_printingType")
        self.comboBox_printingType = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_printingType.setGeometry(QtCore.QRect(90, 60, 111, 22))
        self.comboBox_printingType.setObjectName("comboBox_printingType")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 62, 101, 21))
        self.pushButton.setObjectName("pushButton")
        D_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(D_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 345, 21))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        D_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(D_MainWindow)
        self.statusbar.setObjectName("statusbar")
        D_MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Product_Code_Folder = QtWidgets.QAction(D_MainWindow)
        self.actionNew_Product_Code_Folder.setObjectName("actionNew_Product_Code_Folder")
        self.actionFind_Test_Data = QtWidgets.QAction(D_MainWindow)
        self.actionFind_Test_Data.setObjectName("actionFind_Test_Data")
        self.menuTools.addAction(self.actionNew_Product_Code_Folder)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(D_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(D_MainWindow)

    def retranslateUi(self, D_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        D_MainWindow.setWindowTitle(_translate("D_MainWindow", "SML File Manager"))
        self.groupBox.setTitle(_translate("D_MainWindow", "Find Product Code"))
        self.label_productCode.setText(_translate("D_MainWindow", "Product Code:"))
        self.label_printingType.setText(_translate("D_MainWindow", "Printing Type:"))
        self.comboBox_printingType.setItemText(0, _translate("D_MainWindow", "<Select>"))
        self.comboBox_printingType.setItemText(1, _translate("D_MainWindow", "Arc_Thermal"))
        self.comboBox_printingType.setItemText(2, _translate("D_MainWindow", "Digital"))
        self.comboBox_printingType.setItemText(3, _translate("D_MainWindow", "Offset"))
        self.comboBox_printingType.setItemText(4, _translate("D_MainWindow", "PFL"))
        self.comboBox_printingType.setItemText(5, _translate("D_MainWindow", "Woven"))
        self.pushButton.setText(_translate("D_MainWindow", "Open"))
        self.menuTools.setTitle(_translate("D_MainWindow", "Tools"))
        self.actionNew_Product_Code_Folder.setText(_translate("D_MainWindow", "New Product Code Folder"))
        self.actionFind_Test_Data.setText(_translate("D_MainWindow", "Find Test Data"))
