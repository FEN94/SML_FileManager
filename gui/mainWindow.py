# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from gui.newPCFolder import Ui_D_NewPCFolder
from logic.main import open_product_code
from logic.main import message
import sys
import subprocess
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(277, 162)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_findpc = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_findpc.setGeometry(QtCore.QRect(10, 10, 251, 111))
        self.groupBox_findpc.setObjectName("groupBox_findpc")
        self.label_productcode = QtWidgets.QLabel(self.groupBox_findpc)
        self.label_productcode.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_productcode.setObjectName("label_productcode")
        self.lineEdit_productcode = QtWidgets.QLineEdit(self.groupBox_findpc)
        self.lineEdit_productcode.setGeometry(QtCore.QRect(110, 30, 113, 22))
        self.lineEdit_productcode.setObjectName("lineEdit_productcode")
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_findpc)
        self.pushButton_search.setGeometry(QtCore.QRect(20, 60, 211, 24))
        self.pushButton_search.setObjectName("pushButton_search")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 21))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_PC_folder_s = QtWidgets.QAction(MainWindow)
        self.actionNew_PC_folder_s.setObjectName("actionNew_PC_folder_s")
        self.menuTools.addAction(self.actionNew_PC_folder_s)
        self.actionGMC_tool = QtWidgets.QAction(MainWindow)
        self.actionGMC_tool.setObjectName("actionGMC_tool")
        self.menuTools.addAction(self.actionGMC_tool)
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################Events and Actions################
        self.pushButton_search.clicked.connect(self.open_productcode)
        self.actionNew_PC_folder_s.triggered.connect(self.newPCFolder)
        self.actionGMC_tool.triggered.connect(self.openGMC_tool)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SML File Manager"))
        self.groupBox_findpc.setTitle(_translate("MainWindow", "Find Product Code"))
        self.label_productcode.setText(_translate("MainWindow", "Product Code:"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew_PC_folder_s.setText(_translate("MainWindow", "New PC folder(s)"))
        self.actionGMC_tool.setText(_translate("MainWindow", "Open GMC Tool"))
##################################################################################################################

    def open_productcode(self):
        if open_product_code(self.lineEdit_productcode.text().strip()) is False:
            message(QtWidgets.QMessageBox.Critical, "Product Code not found")

    def newPCFolder(self):
        newPCFolderWindow = QtWidgets.QDialog()
        ui = Ui_D_NewPCFolder()
        ui.setupUi(newPCFolderWindow)
        newPCFolderWindow.setModal(True)
        newPCFolderWindow.exec()

    def openGMC_tool(self):
        def thread():
            commad = "C:/GMC/GMC_2020.jar"
            subprocess.check_output(commad, shell=True)
        threading.Thread(target=thread).start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
