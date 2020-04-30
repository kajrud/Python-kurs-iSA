from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
import day_15_2 as excel

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('day_15.ui', self)

        self.setWindowTitle('My Excel')

        self.buttonOpen: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.buttonOpen.triggered.connect(self.action_open)

        self.buttonSave: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionSave')
        self.buttonSave.triggered.connect(self.action_save)

        self.buttonExit: QtWidgets.QAction = self.findChild(QtWidgets.QAction, 'actionExit')
        self.buttonExit.triggered.connect(self.action_exit)

        self.infoBar: QtWidgets.QLabel = self.findChild(QtWidgets.QLabel, 'statusBar')


        self.tableWidget: QtWidgets.QTableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.tableWidget.doubleClicked.connect(self.slotDoubleClicked)

        self.show()

    def slotDoubleClicked(self, mi: QtCore.QModelIndex):
        print('double click')
        print(type(mi))
        self.infoBar.setText(f"Komórka Row: {mi.row() +1}, Column: {mi.column() +1}")

    def action_save(self):
        try:
            print('save')
            row_count = self.tableWidget.rowCount()
            col_count = self.tableWidget.columnCount()
            data = []
            for row in range(row_count):
                cols = []
                for col in range (col_count):
                    cols.append(self.tableWidget.item(row, col).text())
                data.append(cols)

            excel.dump(self.path_to_file, data)
        except:
            pass


    def action_open(self):
        print('open')
        self.infoBar.setText("Trwa otwieranie...")
        file = QtWidgets.QFileDialog.getOpenFileNames(self, "Wybierz plik", filter="Excel (*.xlsx)")
        path_to_file = file[0]
        self.path_to_file = path_to_file[0]
        if self.path_to_file != "":
            data = excel.load(self.path_to_file)

            self.tableWidget.setRowCount(data['rowCount'])
            self.tableWidget.setColumnCount(data["colCount"])

            for row_idx, row in enumerate(data['data']):
                for col_idx, col in enumerate(row):
                    self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(col))

        self.infoBar.setText("Załadowano plik")
        
    def action_exit(self):
        print('exit')
        exit()

app = QtWidgets.QApplication(sys.argv)
window = App()
app.exec_()