# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProductCodeFolder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from logic.main import message, make_folder

class Ui_D_NewPCFolder(object):
    def setupUi(self, D_NewPCFolder):
        D_NewPCFolder.setObjectName("D_NewPCFolder")
        D_NewPCFolder.resize(929, 420)
        self.groupBox_productCode = QtWidgets.QGroupBox(D_NewPCFolder)
        self.groupBox_productCode.setGeometry(QtCore.QRect(10, 10, 911, 361))
        self.groupBox_productCode.setObjectName("groupBox_productCode")
        self.tableWidget_ProductCode = QtWidgets.QTableWidget(self.groupBox_productCode)
        self.tableWidget_ProductCode.setGeometry(QtCore.QRect(270, 10, 631, 341))
        self.tableWidget_ProductCode.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_ProductCode.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_ProductCode.setObjectName("tableWidget_ProductCode")
        self.tableWidget_ProductCode.setColumnCount(5)
        self.tableWidget_ProductCode.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_ProductCode.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_ProductCode.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_ProductCode.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_ProductCode.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_ProductCode.setHorizontalHeaderItem(4, item)
        self.label_productCode = QtWidgets.QLabel(self.groupBox_productCode)
        self.label_productCode.setGeometry(QtCore.QRect(11, 29, 91, 16))
        self.label_productCode.setObjectName("label_productCode")
        self.label_printingType = QtWidgets.QLabel(self.groupBox_productCode)
        self.label_printingType.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_printingType.setObjectName("label_printingType")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_productCode)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 120, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_2.addWidget(self.pushButton_remove)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_productCode)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 30, 139, 53))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_productCode = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_productCode.setObjectName("lineEdit_productCode")
        self.verticalLayout_2.addWidget(self.lineEdit_productCode)
        self.comboBox_printingType = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_printingType.setObjectName("comboBox_printingType")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_printingType)
        self.label_numStyles = QtWidgets.QLabel(self.groupBox_productCode)
        self.label_numStyles.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_numStyles.setObjectName("label_numStyles")
        self.spinBox_numStyles = QtWidgets.QSpinBox(self.groupBox_productCode)
        self.spinBox_numStyles.setGeometry(QtCore.QRect(100, 90, 42, 22))
        self.spinBox_numStyles.setObjectName("spinBox_numStyles")
        self.spinBox_numStyles.setValue(1)
        self.layoutWidget2 = QtWidgets.QWidget(D_NewPCFolder)
        self.layoutWidget2.setGeometry(QtCore.QRect(720, 380, 195, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_create = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_create.setObjectName("pushButton_create")
        self.horizontalLayout.addWidget(self.pushButton_create)
        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)

        self.retranslateUi(D_NewPCFolder)
        QtCore.QMetaObject.connectSlotsByName(D_NewPCFolder)

        self.pushButton_add.clicked.connect(self.addProductCode)
        self.pushButton_remove.clicked.connect(self.removeProductCode)
        self.pushButton_close.clicked.connect(QtWidgets.qApp.quit)
        self.pushButton_create.clicked.connect(self.create_folders)

    def retranslateUi(self, D_NewPCFolder):
        _translate = QtCore.QCoreApplication.translate
        D_NewPCFolder.setWindowTitle(_translate("D_NewPCFolder", "New Product Code Folder"))
        self.groupBox_productCode.setTitle(_translate("D_NewPCFolder", "Product Code Information"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(0)
        item.setText(_translate("D_NewPCFolder", "Product Code"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(1)
        item.setText(_translate("D_NewPCFolder", "Printing Type"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(2)
        item.setText(_translate("D_NewPCFolder", "Number of styles"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(3)
        item.setText(_translate("D_NewPCFolder", "Sub-Program"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(4)
        item.setText(_translate("D_NewPCFolder", "LOGO"))
        self.label_productCode.setText(_translate("D_NewPCFolder", "Product Code:"))
        self.label_printingType.setText(_translate("D_NewPCFolder", "Printing Type:"))
        self.pushButton_add.setText(_translate("D_NewPCFolder", "Add"))
        self.pushButton_remove.setText(_translate("D_NewPCFolder", "Remove"))
        self.comboBox_printingType.setItemText(0, _translate("D_NewPCFolder", "<Select type>"))
        self.comboBox_printingType.setItemText(1, _translate("D_NewPCFolder", "Arc_Thermal"))
        self.comboBox_printingType.setItemText(2, _translate("D_NewPCFolder", "Digital"))
        self.comboBox_printingType.setItemText(3, _translate("D_NewPCFolder", "Offset"))
        self.comboBox_printingType.setItemText(4, _translate("D_NewPCFolder", "PFL"))
        self.comboBox_printingType.setItemText(5, _translate("D_NewPCFolder", "Woven"))
        self.label_numStyles.setText(_translate("D_NewPCFolder", "No. of styles:"))
        self.pushButton_create.setText(_translate("D_NewPCFolder", "Create"))
        self.pushButton_close.setText(_translate("D_NewPCFolder", "Close"))

    def addProductCode(self):
        if self.comboBox_printingType.currentIndex() != 0:
            rowPosition = self.tableWidget_ProductCode.rowCount()
            productCode = self.lineEdit_productCode.text()
            printing_type = self.comboBox_printingType.currentText()
            num_styles = self.spinBox_numStyles.value()
            if num_styles > 1:
                num_styles = str(num_styles)
            else:
                num_styles = "1"
            self.tableWidget_ProductCode.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem(productCode)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_ProductCode.setItem(rowPosition, 0, item)
            item = QtWidgets.QTableWidgetItem(printing_type)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_ProductCode.setItem(rowPosition, 1, item)
            item = QtWidgets.QTableWidgetItem(num_styles)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_ProductCode.setItem(rowPosition, 2, item)


            # This block of code create and enter a checkBox to the table
            checkBox_subProgram = QtWidgets.QTableWidgetItem()
            checkBox_subProgram.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            checkBox_subProgram.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget_ProductCode.setItem(rowPosition, 3, checkBox_subProgram)
            checkBox_logo = QtWidgets.QTableWidgetItem()
            checkBox_logo.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            checkBox_logo.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget_ProductCode.setItem(rowPosition, 4, checkBox_logo)
        else:
            message(QtWidgets.QMessageBox.Warning, "Must select a printing type")


    def removeProductCode(self):
        row_selected = self.tableWidget_ProductCode.currentRow()
        self.tableWidget_ProductCode.removeRow(row_selected)


    def create_folders(self):
        pc_list = []
        for row in range(self.tableWidget_ProductCode.rowCount()):
            pc = []
            pc.append(self.tableWidget_ProductCode.item(row, 0).text())
            pc.append(self.tableWidget_ProductCode.item(row, 1).text())
            pc.append(int(self.tableWidget_ProductCode.item(row, 2).text()))
            if self.tableWidget_ProductCode.item(row, 3).checkState() == 2:
                pc.append(True)
            else:
                pc.append(False)
            if self.tableWidget_ProductCode.item(row, 4).checkState() == 2:
                pc.append(True)
            else:
                pc.append(False)
            pc_list.append(pc)
        if make_folder(pc_list):
            message(QtWidgets.QMessageBox.Information, "Folder(s) created successfully")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_D_NewPCFolder()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())