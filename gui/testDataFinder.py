# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ferna\OneDrive\PythonProjects\TestDataFinder\ui_files\testDataFinder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import logic.main as m


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 173)
        self.label_productCode = QtWidgets.QLabel(Dialog)
        self.label_productCode.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_productCode.setObjectName("label_productCode")
        self.lineEdit_productCode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_productCode.setGeometry(QtCore.QRect(90, 40, 161, 20))
        self.lineEdit_productCode.setObjectName("lineEdit_productCode")
        self.label_path = QtWidgets.QLabel(Dialog)
        self.label_path.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_path.setObjectName("label_path")
        self.lineEdit_path = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_path.setEnabled(True)
        self.lineEdit_path.setGeometry(QtCore.QRect(90, 80, 291, 20))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(220, 140, 75, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_ok.clicked.connect(self.setPath)
        self.pushButton_close.clicked.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test Data Finder"))
        self.label_productCode.setText(_translate("Dialog", "Product Code:"))
        self.label_path.setText(_translate("Dialog", "Path:"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
        self.pushButton_ok.setText(_translate("Dialog", "Ok"))

    def getProductCode(self):
        product_code = self.lineEdit_productCode.text()
        path = m.find_testData(product_code)
        return path
    def setPath(self):
        path = self.getProductCode()
        self.lineEdit_path.setText(path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
