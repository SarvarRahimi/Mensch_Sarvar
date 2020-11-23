from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

from new_game import new_game_func


class FinishDialog(QDialog):
    def __init__(self, parent, names, colors):
        super().__init__(parent)
        loadUi('ui/finish_ui.ui', self)

        self.names = names.split()
        self.colors = colors.split()

        self.setFixedSize(760, 560 - (4 - len(self.names)) * 80)

        self.name_widget.setGeometry(QRect(10, 10, 740, 460 - (4 - len(self.names)) * 80))

        self.name_1.setText(f'1. {self.names[0]}')
        self.icon_label_1.setPixmap(QPixmap(f'ressource/game_piece_{self.colors[0]}.png'))

        self.name_2.setText(f'2. {self.names[1]}')
        self.icon_label_2.setPixmap(QPixmap(f'ressource/game_piece_{self.colors[1]}.png'))

        if len(self.names) == 3:
            self.name_3.setText(f'3. {self.names[2]}')
            self.icon_label_3.setPixmap(QPixmap(f'ressource/game_piece_{self.colors[2]}.png'))
        elif len(self.names) == 4:
            self.name_3.setText(f'3. {self.names[2]}')
            self.icon_label_3.setPixmap(QPixmap(f'ressource/game_piece_{self.colors[2]}.png'))
            self.name_4.setText(f'4. {self.names[3]}')
            self.icon_label_4.setPixmap(QPixmap(f'ressource/game_piece_{self.colors[3]}.png'))

        self.new_game_btn.setGeometry(QRect(475, 500 - (4 - len(self.names)) * 80, 105, 35))
        self.new_game_btn.clicked.connect(self.run_new_game)

        self.exit_btn.setGeometry(QRect(600, 500 - (4 - len(self.names)) * 80, 105, 35))
        self.exit_btn.clicked.connect(QApplication.exit)

    def run_new_game(self):
        self.name_1.setText('')
        self.name_2.setText('')
        self.name_3.setText('')
        self.name_4.setText('')

        self.icon_label_1.clear()
        self.icon_label_2.clear()
        self.icon_label_3.clear()
        self.icon_label_4.clear()

        new_game_func(self.parent(), msgbox=False)
        self.close()
