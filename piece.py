from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class Piece(QPushButton):
    def __init__(self, parent, color, bases, positions):
        super().__init__(parent)
        self.setDisabled(True)
        self.setVisible(False)
        self.setGeometry(410, 410, 69, 69)

        self.__icon = QIcon()
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}.png'), QIcon.Normal)
        self.__icon.addPixmap(QPixmap(f'ressource/game_piece_{color}_disabled.png'), QIcon.Disabled)
        self.setIcon(self.__icon)
        self.setIconSize(QSize(69, 69))
        self.setStyleSheet("""border-color: rgba(255, 255, 255, 0);
                              background-color: rgba(255, 255, 255, 0);""")

        self.color = color
        self.setStatusTip(self.color.capitalize() + ' Piece')
        self.__bases = bases
        self.__positions = positions

    def is_in_base(self):
        return self.geometry() in [base.geometry() for base in self.__bases]

    def is_in_game(self):
        return self.geometry() in [position.geometry() for position in self.__positions[:-4]]

    def is_in_home(self):
        return self.geometry() in [position.geometry() for position in self.__positions[-4:]]

    def smooth_move(self, number):
        if self.is_in_base():
            deley = 500
            self.parent().anim = QPropertyAnimation(self, b"geometry")
            self.parent().anim.setDuration(deley)
            self.parent().anim.setEndValue(self.__positions[0].geometry())
            self.parent().anim.start()
        else:
            deley = 250 * number
            pic_index = [pos.geometry() for pos in self.__positions].index(self.geometry())
            self.parent().anim_grp = QSequentialAnimationGroup()
            for i in range(number):
                self.parent().anim = QPropertyAnimation(self, b"geometry")
                self.parent().anim.setDuration(250)
                self.parent().anim.setStartValue(self.__positions[pic_index + i].geometry())
                self.parent().anim.setEndValue(self.__positions[pic_index + i + 1].geometry())
                self.parent().anim_grp.addAnimation(self.parent().anim)
            self.parent().anim_grp.start()
        return deley + 100
