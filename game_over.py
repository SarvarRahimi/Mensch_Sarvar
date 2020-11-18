from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

from new_game import new_game_func


class GameOver(QDialog):
    def __init__(self, parent, names, colors):
        super().__init__(parent)
        loadUi('game_over_ui.ui', self)

        self.names = names.split()
        self.colors = colors.split()

        self.player_1.setText(f'1. {self.names[0]}')
        self.player_2.setText(f'2. {self.names[1]}')

        if len(self.names) == 3:
            self.player_3.setText(f'3. {self.names[2]}')

        elif len(self.names) == 4:
            self.player_3.setText(f'3. {self.names[2]}')
            self.player_4.setText(f'4. {self.names[3]}')

        self.new_game.clicked.connect(self.run_new_game)
        self.exit.clicked.connect(QApplication.exit)

    def run_new_game(self):
        self.player_1.setText('')
        self.player_2.setText('')
        self.player_3.setText('')
        self.player_4.setText('')

        new_game_func(self.parent(), flag=False)
        self.close()
