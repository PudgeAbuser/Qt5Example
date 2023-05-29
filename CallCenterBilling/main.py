import sys
import sqlalchemy as database
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from newFormBilling import Ui_MainWindow



class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addButton.clicked.connect(self.addNumber)
        self.ui.deleteButton.clicked.connect(self.deleteNumber)

        self.__table = self.ui.tableWidget
        self.__connection = None
        self.__engine = None
        self.__metadata = None
        self.__numbers = None
        self.InitDatabase()
        # self.firstStart()
        self.loadItems()
    def firstStart(self):
        new_products = [
            {'operator':'МТС', 'number':8286511590},
            {'operator': 'БИЛАЙН', 'number': 8296441397},
            {'operator': 'МЕГАФОН', 'number': 8236351696},
            {'operator': 'ТЕЛЕ2', 'number': 8286341394},
        ]
        insertion_querry = self.__numbers.insert().values(new_products)
        self.__connection.execute(insertion_querry)
        self.__connection.commit()
        
        
    def InitDatabase(self):
        self.__engine = database.create_engine('sqlite:///CallCenterBilling/database.db')
        self.__connection = self.__engine.connect()
        self.__metadata = database.MetaData()

        self.__numbers = database.Table(
            'products', self.__metadata,
            database.Column('id', database.Integer, primary_key=True),
            database.Column('operator', database.String),
            database.Column('number', database.Integer),
        )

        self.__metadata.create_all(self.__engine)

    def loadItems(self):
        numbers = [
            {'operator':'Phone 1', 'number':1000},
            {'operator': 'Phone 2', 'number': 2000},
            {'operator': 'Phone 3', 'number': 3000},
            {'operator': 'Phone 4', 'number': 4000},
        ]

        self.__table.setRowCount(len(numbers))
        self.__table.setColumnCount(2)

        self.__table.setHorizontalHeaderLabels(('Оператор','Номер'))

        self.__table.setColumnWidth(0,100)
        self.__table.setColumnWidth(1,100)

        row_index = 0
        for product in numbers:
            self.ui.tableWidget.setItem(row_index,0,QTableWidgetItem(str(product['operator'])))
            self.ui.tableWidget.setItem(row_index,1,QTableWidgetItem(str(product['number'])))
            row_index += 1

    def addNumber(self):
        print(1)

    def deleteNumber(self):
        print(2)

def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()