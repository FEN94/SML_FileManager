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
        MainWindow.setFixedSize(270, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_findpc = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_findpc.setGeometry(QtCore.QRect(10, 10, 251, 161))
        self.groupBox_findpc.setObjectName("groupBox_findpc")
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_findpc)
        self.pushButton_search.setGeometry(QtCore.QRect(20, 130, 211, 24))
        self.pushButton_search.setObjectName("pushButton_search")
        self.widget = QtWidgets.QWidget(self.groupBox_findpc)
        self.widget.setGeometry(QtCore.QRect(20, 30, 210, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_productcode = QtWidgets.QLabel(self.widget)
        self.label_productcode.setObjectName("label_productcode")
        self.horizontalLayout.addWidget(self.label_productcode)
        self.lineEdit_productcode = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_productcode.setObjectName("lineEdit_productcode")
        self.horizontalLayout.addWidget(self.lineEdit_productcode)
        self.widget1 = QtWidgets.QWidget(self.groupBox_findpc)
        self.widget1.setGeometry(QtCore.QRect(21, 62, 201, 47))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_gmc = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_gmc.setObjectName("radioButton_gmc")
        self.radioButton_gmc.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radioButton_gmc)
        self.comboBox_printingtype = QtWidgets.QComboBox(self.widget1)
        self.comboBox_printingtype.setObjectName("comboBox_printingtype")
        self.comboBox_printingtype.addItem("")
        self.comboBox_printingtype.addItem("")
        self.comboBox_printingtype.addItem("")
        self.comboBox_printingtype.addItem("")
        self.comboBox_printingtype.addItem("")
        self.comboBox_printingtype.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_printingtype)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.radioButton_nice_label = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_nice_label.setObjectName("radioButton_nice_label")
        self.verticalLayout.addWidget(self.radioButton_nice_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 21))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_PC_folder_s = QtWidgets.QAction(MainWindow)
        self.actionNew_PC_folder_s.setObjectName("actionNew_PC_folder_s")
        self.actionOpen_GMC_Tool = QtWidgets.QAction(MainWindow)
        self.actionOpen_GMC_Tool.setObjectName("actionOpen_GMC_Tool")
        self.actionConfigure_Path = QtWidgets.QAction(MainWindow)
        self.actionConfigure_Path.setObjectName("actionConfigure_Path")
        self.menuTools.addAction(self.actionNew_PC_folder_s)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionOpen_GMC_Tool)
        self.menuSettings.addAction(self.actionConfigure_Path)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################Events and Actions################
        self.pushButton_search.clicked.connect(self.open_productcode)
        self.radioButton_nice_label.clicked.connect(self.enable_cb_printingtype)
        self.radioButton_gmc.clicked.connect(self.enable_cb_printingtype)
        self.actionNew_PC_folder_s.triggered.connect(self.newPCFolder)
        self.actionOpen_GMC_Tool.triggered.connect(self.openGMC_tool)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_findpc.setTitle(_translate("MainWindow", "Find Product Code"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.label_productcode.setText(_translate("MainWindow", "Product Code:"))
        self.radioButton_gmc.setText(_translate("MainWindow", "GMC"))
        self.comboBox_printingtype.setItemText(0, _translate("MainWindow", "<Select type>"))
        self.comboBox_printingtype.setItemText(1, _translate("MainWindow", "Arc_Thermal"))
        self.comboBox_printingtype.setItemText(2, _translate("MainWindow", "Digital"))
        self.comboBox_printingtype.setItemText(3, _translate("MainWindow", "Offset"))
        self.comboBox_printingtype.setItemText(4, _translate("MainWindow", "PFL"))
        self.comboBox_printingtype.setItemText(5, _translate("MainWindow", "Woven"))
        self.radioButton_nice_label.setText(_translate("MainWindow", "NiceLabel"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionNew_PC_folder_s.setText(_translate("MainWindow", "New PC folder(s)"))
        self.actionOpen_GMC_Tool.setText(_translate("MainWindow", "Open GMC Tool"))
        self.actionConfigure_Path.setText(_translate("MainWindow", "Configure Path"))

    ##################################################################################################################

    def open_productcode(self):
        success = False
        if self.lineEdit_productcode.text() == "":
            message(QtWidgets.QMessageBox.Warning, "Enter Product Code")
        elif self.comboBox_printingtype.currentIndex() == 0 and self.radioButton_gmc.isChecked():
            message(QtWidgets.QMessageBox.Warning, "Must select a printing type.")
        else:
            if self.radioButton_gmc.isChecked():
                success = open_product_code(0, self.lineEdit_productcode.text(),
                                            self.comboBox_printingtype.currentText())
            elif self.radioButton_nice_label.isChecked():
                success = open_product_code(1, self.lineEdit_productcode.text(), "")
            if success is False:
                message(QtWidgets.QMessageBox.Critical, "Product Code not found")

    def enable_cb_printingtype(self):
        if self.radioButton_nice_label.isChecked():
            self.comboBox_printingtype.setEnabled(False)
        else:
            self.comboBox_printingtype.setEnabled(True)

    def newPCFolder(self):
        newPCFolderWindow = QtWidgets.QDialog()
        ui = Ui_D_NewPCFolder()
        ui.setupUi(newPCFolderWindow)
        newPCFolderWindow.setModal(True)
        newPCFolderWindow.exec()

    def openGMC_tool(self):
        def thread():
            command = "C:/GMC/GMC_2020.jar"
            subprocess.check_output(command, shell=True)
        threading.Thread(target=thread).start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
