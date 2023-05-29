# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 306)
        MainWindow.setMinimumSize(QtCore.QSize(439, 306))
        MainWindow.setMaximumSize(QtCore.QSize(439, 306))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(20, 250, 401, 41))
        self.btnGenerate.setStyleSheet("background-color: rgb(88, 88, 88);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"border-radius: 8px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")
        self.btnGenerate.setObjectName("btnGenerate")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 401, 131))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(0, 128))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnReset = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnReset.setMinimumSize(QtCore.QSize(0, 128))
        self.btnReset.setStyleSheet("background-color: rgb(88, 88, 88);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btnReset.setObjectName("btnReset")
        self.gridLayout.addWidget(self.btnReset, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 170, 401, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setMinimumSize(QtCore.QSize(240, 0))
        self.label1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.count_pass = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.count_pass.setStyleSheet("background-color: rgb(88, 88, 88);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.count_pass.setProperty("value", 5)
        self.count_pass.setObjectName("count_pass")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.count_pass)
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2.setMinimumSize(QtCore.QSize(240, 0))
        self.label2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.count_symbol = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.count_symbol.setStyleSheet("background-color: rgb(88, 88, 88);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.count_symbol.setProperty("value", 7)
        self.count_symbol.setObjectName("count_symbol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.count_symbol)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.specialCharacters = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.specialCharacters.setEnabled(True)
        self.specialCharacters.setTabletTracking(False)
        self.specialCharacters.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.specialCharacters.setAutoFillBackground(False)
        self.specialCharacters.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.specialCharacters.setChecked(True)
        self.specialCharacters.setObjectName("specialCharacters")
        self.verticalLayout.addWidget(self.specialCharacters)
        self.letters = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.letters.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.letters.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.letters.setChecked(True)
        self.letters.setObjectName("letters")
        self.verticalLayout.addWidget(self.letters)
        self.numbers = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.numbers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.numbers.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.numbers.setChecked(True)
        self.numbers.setObjectName("numbers")
        self.verticalLayout.addWidget(self.numbers)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролей"))
        self.btnGenerate.setText(_translate("MainWindow", "Сгенерировать пароль"))
        self.btnReset.setText(_translate("MainWindow", "Очистить"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label1.setText(_translate("MainWindow", "Кол-во паролей:"))
        self.label2.setText(_translate("MainWindow", "Кол-во символов:"))
        self.specialCharacters.setText(_translate("MainWindow", "спецсимволы"))
        self.letters.setText(_translate("MainWindow", "буквы"))
        self.numbers.setText(_translate("MainWindow", "цифры"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
