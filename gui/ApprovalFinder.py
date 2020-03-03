# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Fernandoestevez\Documents\PythonProjects\TestDataFinder\ui_files\ApprovalsFinder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 280)
        self.groupBox_tableProductCodes = QtWidgets.QGroupBox(Dialog)
        self.groupBox_tableProductCodes.setGeometry(QtCore.QRect(300, 10, 251, 221))
        self.groupBox_tableProductCodes.setObjectName("groupBox_tableProductCodes")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_tableProductCodes)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 231, 191))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_productCode = QtWidgets.QLabel(Dialog)
        self.label_productCode.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_productCode.setObjectName("label_productCode")
        self.lineEdit_productCode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_productCode.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEdit_productCode.setObjectName("lineEdit_productCode")
        self.label_styles = QtWidgets.QLabel(Dialog)
        self.label_styles.setGeometry(QtCore.QRect(20, 55, 47, 13))
        self.label_styles.setObjectName("label_styles")
        self.spinBox_styles = QtWidgets.QSpinBox(Dialog)
        self.spinBox_styles.setGeometry(QtCore.QRect(90, 45, 42, 22))
        self.spinBox_styles.setObjectName("spinBox_styles")
        self.pushButton_addProductCode = QtWidgets.QPushButton(Dialog)
        self.pushButton_addProductCode.setGeometry(QtCore.QRect(210, 20, 75, 21))
        self.pushButton_addProductCode.setObjectName("pushButton_addProductCode")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(350, 240, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_DeleteProductCode = QtWidgets.QPushButton(self.widget)
        self.pushButton_DeleteProductCode.setObjectName("pushButton_DeleteProductCode")
        self.horizontalLayout.addWidget(self.pushButton_DeleteProductCode)
        self.pushButton_clearTable = QtWidgets.QPushButton(self.widget)
        self.pushButton_clearTable.setObjectName("pushButton_clearTable")
        self.horizontalLayout.addWidget(self.pushButton_clearTable)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_addProductCode.clicked.connect(self.addProductCode)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_tableProductCodes.setTitle(_translate("Dialog", "Product Codes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Product Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "No. of Styles"))
        self.label_productCode.setText(_translate("Dialog", "Produc Code:"))
        self.label_styles.setText(_translate("Dialog", "Styles"))
        self.pushButton_addProductCode.setText(_translate("Dialog", "Add"))
        self.pushButton_DeleteProductCode.setText(_translate("Dialog", "Delete"))
        self.pushButton_clearTable.setText(_translate("Dialog", "Clear"))

    def addProductCode(self):
        rowPosition = self.tableWidget.rowCount()
        productCode = self.lineEdit_productCode.text()
        noStyles = self.spinBox_styles.text()
        self.tableWidget.insertRow(rowPosition)
        item = QtWidgets.QTableWidgetItem(productCode)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(rowPosition, 0, item)
        item = QtWidgets.QTableWidgetItem(noStyles)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(rowPosition, 1, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())