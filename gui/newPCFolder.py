# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProductCodeFolder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from logic.main import message, make_folder


class Ui_D_NewPCFolder(object):
    def setupUi(self, D_NewPCFolder):
        D_NewPCFolder.setObjectName("D_NewPCFolder")
        D_NewPCFolder.setFixedSize(929, 420)
        self.groupBox_productCode = QtWidgets.QGroupBox(D_NewPCFolder)
        self.groupBox_productCode.setGeometry(QtCore.QRect(10, 10, 911, 361))
        self.groupBox_productCode.setObjectName("groupBox_productCode")
        self.tableWidget_ProductCode = QtWidgets.QTableWidget(self.groupBox_productCode)
        self.tableWidget_ProductCode.setGeometry(QtCore.QRect(270, 10, 631, 341))
        self.tableWidget_ProductCode.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_ProductCode.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_ProductCode.setObjectName("tableWidget_ProductCode")
        # self.tableWidget_ProductCode.setColumnCount(5)
        self.tableWidget_ProductCode.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.tableWidget_ProductCode.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.tableWidget_ProductCode.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.tableWidget_ProductCode.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.tableWidget_ProductCode.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # self.tableWidget_ProductCode.setHorizontalHeaderItem(4, item)
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
        self.widget = QtWidgets.QWidget(self.groupBox_productCode)
        self.widget.setGeometry(QtCore.QRect(11, 29, 210, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_productCode = QtWidgets.QLabel(self.widget)
        self.label_productCode.setObjectName("label_productCode")
        self.horizontalLayout.addWidget(self.label_productCode)
        self.lineEdit_productCode = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_productCode.setObjectName("lineEdit_productCode")
        self.horizontalLayout.addWidget(self.lineEdit_productCode)
        self.widget1 = QtWidgets.QWidget(self.groupBox_productCode)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 110, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_numStyles = QtWidgets.QLabel(self.widget1)
        self.label_numStyles.setObjectName("label_numStyles")
        self.horizontalLayout_4.addWidget(self.label_numStyles)
        self.spinBox_numStyles = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_numStyles.setObjectName("spinBox_numStyles")
        self.spinBox_numStyles.setValue(1)
        self.horizontalLayout_4.addWidget(self.spinBox_numStyles)
        self.widget2 = QtWidgets.QWidget(self.groupBox_productCode)
        self.widget2.setGeometry(QtCore.QRect(11, 58, 245, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_printingType = QtWidgets.QLabel(self.widget2)
        self.label_printingType.setObjectName("label_printingType")
        self.horizontalLayout_3.addWidget(self.label_printingType)
        self.comboBox_printingType = QtWidgets.QComboBox(self.widget2)
        self.comboBox_printingType.setObjectName("comboBox_printingType")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.comboBox_printingType.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_printingType)
        self.checkBox_nicelabel = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_nicelabel.setObjectName("checkBox_nicelabel")
        self.horizontalLayout_3.addWidget(self.checkBox_nicelabel)
        self.pushButton_create = QtWidgets.QPushButton(D_NewPCFolder)
        self.pushButton_create.setGeometry(QtCore.QRect(840, 390, 75, 24))
        self.pushButton_create.setObjectName("pushButton_create")

        self.retranslateUi(D_NewPCFolder)
        QtCore.QMetaObject.connectSlotsByName(D_NewPCFolder)

        ################Events and Actions################
        self.pushButton_add.clicked.connect(self.addProductCode)
        self.pushButton_remove.clicked.connect(self.removeProductCode)
        self.pushButton_create.clicked.connect(self.create_folders)
        self.checkBox_nicelabel.clicked.connect(self.enable_printing_type)

    def retranslateUi(self, D_NewPCFolder):
        _translate = QtCore.QCoreApplication.translate
        D_NewPCFolder.setWindowTitle(_translate("D_NewPCFolder", "New Product Code Folder"))
        self.groupBox_productCode.setTitle(_translate("D_NewPCFolder", "Product Code Information"))
        # item = self.tableWidget_ProductCode.horizontalHeaderItem(0)
        # item.setText(_translate("D_NewPCFolder", "Product Code"))
        # item = self.tableWidget_ProductCode.horizontalHeaderItem(1)
        # item.setText(_translate("D_NewPCFolder", "Printing Type"))
        # item = self.tableWidget_ProductCode.horizontalHeaderItem(2)
        # item.setText(_translate("D_NewPCFolder", "Number of styles"))
        # item = self.tableWidget_ProductCode.horizontalHeaderItem(3)
        # item.setText(_translate("D_NewPCFolder", "Sub-Program"))
        # item = self.tableWidget_ProductCode.horizontalHeaderItem(4)
        # item.setText(_translate("D_NewPCFolder", "LOGO"))
        self.pushButton_add.setText(_translate("D_NewPCFolder", "Add"))
        self.pushButton_remove.setText(_translate("D_NewPCFolder", "Remove"))
        self.label_productCode.setText(_translate("D_NewPCFolder", "Product Code:"))
        self.label_numStyles.setText(_translate("D_NewPCFolder", "No. of styles:"))
        self.label_printingType.setText(_translate("D_NewPCFolder", "Printing Type:"))
        self.comboBox_printingType.setItemText(0, _translate("D_NewPCFolder", "<Select type>"))
        self.comboBox_printingType.setItemText(1, _translate("D_NewPCFolder", "Arc_Thermal"))
        self.comboBox_printingType.setItemText(2, _translate("D_NewPCFolder", "Digital"))
        self.comboBox_printingType.setItemText(3, _translate("D_NewPCFolder", "Offset"))
        self.comboBox_printingType.setItemText(4, _translate("D_NewPCFolder", "PFL"))
        self.comboBox_printingType.setItemText(5, _translate("D_NewPCFolder", "Woven"))
        self.checkBox_nicelabel.setText(_translate("D_NewPCFolder", "NiceLabel"))
        self.pushButton_create.setText(_translate("D_NewPCFolder", "Create"))

    ##################################################################################################################

    def enable_printing_type(self):
        if self.checkBox_nicelabel.isChecked():
            self.comboBox_printingType.setEnabled(False)
        else:
            self.comboBox_printingType.setEnabled(True)

    def create_table(self):
        if self.checkBox_nicelabel.isChecked() is False:
            width = int(self.tableWidget_ProductCode.width() / 5)
            self.tableWidget_ProductCode.setColumnCount(5)
        else:
            width = int(self.tableWidget_ProductCode.width() / 4)
            self.tableWidget_ProductCode.setColumnCount(4)
        self.tableWidget_ProductCode.setColumnWidth(0, width)
        self.tableWidget_ProductCode.setColumnWidth(1, width)
        self.tableWidget_ProductCode.setColumnWidth(2, width)
        self.tableWidget_ProductCode.setColumnWidth(3, width)
        if self.checkBox_nicelabel.isChecked() is False:
            self.tableWidget_ProductCode.setColumnWidth(4, width)
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
        if self.checkBox_nicelabel.isChecked() is False:
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget_ProductCode.setHorizontalHeaderItem(4, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_ProductCode.horizontalHeaderItem(0)
        item.setText(_translate("D_NewPCFolder", "Product Code"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(1)
        item.setText(_translate("D_NewPCFolder", "Printing Type"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(2)
        item.setText(_translate("D_NewPCFolder", "Number of styles"))
        item = self.tableWidget_ProductCode.horizontalHeaderItem(3)
        item.setText(_translate("D_NewPCFolder", "Sub-Program"))
        if self.checkBox_nicelabel.isChecked() is False:
            item = self.tableWidget_ProductCode.horizontalHeaderItem(4)
            item.setText(_translate("D_NewPCFolder", "LOGO"))

    def addProductCode(self):
        self.create_table()
        if self.lineEdit_productCode.text() == "":
            message(QtWidgets.QMessageBox.Warning, "Product Code field cannot be empty")
        elif self.comboBox_printingType.currentIndex() == 0 and self.checkBox_nicelabel.isChecked() is False:
            message(QtWidgets.QMessageBox.Warning, "Must select a printing type")
        else:
            rowPosition = self.tableWidget_ProductCode.rowCount()
            productCode = self.lineEdit_productCode.text()
            if self.checkBox_nicelabel.isChecked():
                printing_type = "Thermal"
            else:
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

    def removeProductCode(self):
        row_selected = self.tableWidget_ProductCode.currentRow()
        self.tableWidget_ProductCode.removeRow(row_selected)

    def create_folders(self):
        pc_list = []
        if self.tableWidget_ProductCode.rowCount() != 0:
            for row in range(self.tableWidget_ProductCode.rowCount()):
                pc = [self.tableWidget_ProductCode.item(row, 0).text().strip(),
                      self.tableWidget_ProductCode.item(row, 1).text(),
                      int(self.tableWidget_ProductCode.item(row, 2).text())]
                if self.tableWidget_ProductCode.item(row, 3).checkState() == 2:
                    pc.append(True)
                else:
                    pc.append(False)
                if self.checkBox_nicelabel.isChecked() is False:
                    if self.tableWidget_ProductCode.item(row, 4).checkState() == 2:
                        pc.append(True)
                    else:
                        pc.append(False)
                pc_list.append(pc)
            if make_folder(pc_list, self.checkBox_nicelabel.isChecked()):
                message(QtWidgets.QMessageBox.Information, "Folder(s) created successfully")
                self.reset_values()
        else:
            message(QtWidgets.QMessageBox.Warning, "Table cannot be empty")

    def reset_values(self):
        self.tableWidget_ProductCode.setColumnCount(0)
        for i in range(self.tableWidget_ProductCode.rowCount()):
            self.tableWidget_ProductCode.removeRow(0)
        self.lineEdit_productCode.clear()
        self.spinBox_numStyles.setValue(1)
        index = self.comboBox_printingType.findText("<Select type>", QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBox_printingType.setCurrentIndex(index)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     D_NewPCFolder = QtWidgets.QDialog()
#     ui = Ui_D_NewPCFolder()
#     ui.setupUi(D_NewPCFolder)
#     D_NewPCFolder.show()
#     sys.exit(app.exec_())
