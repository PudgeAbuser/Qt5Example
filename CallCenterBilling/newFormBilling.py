# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CallCenterBilling/billing.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.operator1 = QtWidgets.QListWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.operator1.setFont(font)
        self.operator1.setAutoScrollMargin(21)
        self.operator1.setObjectName("operator1")
        item = QtWidgets.QListWidgetItem()
        self.operator1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.operator1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.operator1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.operator1.addItem(item)
        self.verticalLayout.addWidget(self.operator1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.number = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.number.setObjectName("number")
        self.verticalLayout_2.addWidget(self.number)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_3.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout_3.addWidget(self.deleteButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 301, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Оператор"))
        __sortingEnabled = self.operator1.isSortingEnabled()
        self.operator1.setSortingEnabled(False)
        item = self.operator1.item(0)
        item.setText(_translate("MainWindow", "МТС"))
        item = self.operator1.item(1)
        item.setText(_translate("MainWindow", "БИЛАЙН"))
        item = self.operator1.item(2)
        item.setText(_translate("MainWindow", "МЕГАФОН"))
        item = self.operator1.item(3)
        item.setText(_translate("MainWindow", "ТЕЛЕ2"))
        self.operator1.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Номер"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())