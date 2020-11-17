from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class Piece(QPushButton):
    def __init__(self, parent, color, home, paths):
        super().__init__(parent)
        self.setDisabled(True)
        self.setVisible(False)
        self.setGeometry(310, 340, 50, 50)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(f'icons/pawn_{color}.png'), QIcon.Normal)
        self.icon.addPixmap(QPixmap(f'icons/pawn_{color}.png'), QIcon.Disabled)
        self.setIcon(self.icon)
        self.setIconSize(QSize(50, 50))
        self.setStyleSheet("""border-color: rgba(255, 255, 255, 0);
                              background-color: rgba(255, 255, 255, 0);""")
        self.color = color
        self.setStatusTip(self.color.capitalize() + ' Piece')
        self.home = home
        self.paths = paths

    def is_in_home(self):
        return self.geometry() in [home.geometry() for home in self.home]

    def is_in_game(self):
        return self.geometry() in [position.geometry() for position in self.paths[:-4]]

    def is_win(self):
        return self.geometry() in [position.geometry() for position in self.paths[-4:]]

    def move(self, number):
        delay = 300
        if self.is_in_home():
            self.parent().anim = QPropertyAnimation(self, b"geometry")
            self.parent().anim.setDuration(delay)
            self.parent().anim.setEndValue(self.paths[0].geometry())
            self.parent().anim.start()
        else:
            delay *= number
            pic_index = [p.geometry() for p in self.paths].index(self.geometry())
            self.parent().anim_grp = QSequentialAnimationGroup()
            for i in range(number):
                self.parent().anim = QPropertyAnimation(self, b"geometry")
                self.parent().anim.setDuration(300)
                self.parent().anim.setStartValue(self.paths[pic_index + i].geometry())
                self.parent().anim.setEndValue(self.paths[pic_index + i + 1].geometry())
                self.parent().anim_grp.addAnimation(self.parent().anim)
            self.parent().anim_grp.start()
        return delay + 100
