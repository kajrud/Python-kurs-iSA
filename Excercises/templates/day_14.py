import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "My app"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, 1200, 800)

        self.button = QPushButton("Hello world!", self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.click_button)

        self.textbox = QLineEdit(self)
        self.textbox.move(50, 100)

        self.label = QLabel(self)
        self.label.move(50, 150)
        self.label.setText("No siemka")
        self.label.resize(200, 50)

        self.show()

    def click_button(self):
        print("No i po co klikasz")
        user_text = self.textbox.text()
        self.label.setText(f"Hello {user_text}")




app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())