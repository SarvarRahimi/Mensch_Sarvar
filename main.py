from sys import argv
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

from create_menu import init_menu
from game import Game
from set_values import set_val


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/project_ui.ui', self)

        self.game = None

        set_val(self)
        init_menu(self)

    def init_game(self):
        if not self.game:
            self.game = Game(self)
        else:
            self.game.first_step()


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()

    app.exec_()
