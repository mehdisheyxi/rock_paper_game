import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import random


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"UI\MASTER.ui", self)  # بارگذاری فایل .ui در لحظه اجرا
        self.setWindowIcon(QIcon(r"icon\master_icon.ico"))
        self.setWindowTitle('sang kaqaz qychi')
        self.start.clicked.connect(self.load_start)

    def load_start(self):
        self.newpage = start()
        self.newpage.show()


class start(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(r"UI\normal_game.ui", self)
        self.setWindowIcon(QIcon(r"icon\master_icon.ico"))
        self.setWindowTitle('now is gaming...')
        self.pc = ''
        self.sang.clicked.connect(self.handl)
        self.qeychi.clicked.connect(self.handl2)
        self.kagaz.clicked.connect(self.handl3)

    def handl(self):
        self.set_pc()
        self.process_sang()

    def handl2(self):
        self.set_pc()
        self.process_qeychi()

    def handl3(self):
        self.set_pc()
        self.process_kaqz()

    def set_pc(self):
        self.pc = random.choice(['sang', 'paper', 'qeychi'])

    def process_sang(self):
        self.ps.setText(f'{self.pc}')

        if self.pc == 'qeychi':
            mes = 'WIN'
        elif self.pc == 'paper':
            mes = 'lose'
        else:
            mes = 'barabar'
        self.label.setText(mes)

    def process_qeychi(self):
        self.ps.setText(f'{self.pc}')
        if self.pc == 'paper':
            mes = 'WIN'
        elif self.pc == 'sang':
            mes = 'lose'
        else:
            mes = 'barabar'
        self.label.setText(mes)

    def process_kaqz(self):
        self.ps.setText(f'{self.pc}')
        if self.pc == 'sang':
            mes = 'WIN'
        elif self.pc == 'qeychi':
            mes = 'lose'
        else:
            mes = 'barabar'
        self.label.setText(mes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
