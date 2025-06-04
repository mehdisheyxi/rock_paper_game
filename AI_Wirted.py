import sys
import random
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"UI\MASTER.ui", self)
        self.setWindowIcon(QIcon(r"icon\master_icon.ico"))
        self.setWindowTitle('Sang Kagaz Qeychi')
        self.start.clicked.connect(self.load_start)

    def load_start(self):
        self.new_page = GamePage()
        self.new_page.show()


class GamePage(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(r"UI\normal_game.ui", self)
        self.setWindowIcon(QIcon(r"icon\master_icon.ico"))
        self.setWindowTitle('Now is Gaming...')

        self.choices = {
            'sang': 'qeychi',
            'qeychi': 'paper',
            'paper': 'sang'
        }

        self.sang.clicked.connect(lambda: self.play('sang'))
        self.qeychi.clicked.connect(lambda: self.play('qeychi'))
        self.kagaz.clicked.connect(lambda: self.play('paper'))

    def play(self, player_choice):
        pc_choice = random.choice(list(self.choices.keys()))
        self.ps.setText(pc_choice)

        if pc_choice == self.choices[player_choice]:
            result = 'WIN'
        elif player_choice == pc_choice:
            result = 'EQUAL'
        else:
            result = 'LOSE'

        self.label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
