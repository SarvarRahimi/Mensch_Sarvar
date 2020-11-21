from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from player import Player
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup


def login_animate(parent, color):
    parent.parallel = QParallelAnimationGroup()
    parent.anim = None
    for i in range(4):
        parent.anim = QPropertyAnimation(parent.pieces[color][i], b"geometry")
        parent.anim.setDuration(2000)
        parent.anim.setEndValue(parent.home[color][i].geometry())
        parent.parallel.addAnimation(parent.anim)

    parent.parallel.start()


class Login(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        loadUi('add_player_ui.ui', self)
        self.setFixedSize(382, 234)
        self.login_btn.clicked.connect(self.is_valid)
        self.cancel_btn.clicked.connect(self.close)

   def is_valid(self):
        username = self.username_box.text()
        password = self.password_box.text()
        color = self.color_box.currentText().lower()

        with open('sample_player.txt') as file:
            for line in file:
                sample_username, sample_password = line.split()
                if username == sample_username and password == sample_password:
                    if username not in self.parent().players.keys():
                        player = Player(username,
                                        self.parent().pieces[color],
                                        self.parent().home[color],
                                        self.parent().paths[color])
                        self.parent().players[color] = player
                        self.color_box.removeItem(self.color_box.currentIndex())
                        self.parent().names[len(self.parent().players) - 1].setText(player.username)
                        self.parent().names[len(self.parent().players) - 1].setStyleSheet(
                            f"""color: {self.parent().colors[color]};""")
                        login_animate(self.parent(), color)
                        if len(self.parent().players) > 1 and not self.parent().Start_Game.isEnabled():
                            self.parent().Start_Game.setEnabled(True)
                        if len(self.parent().players) > 3:
                            self.parent().Add_Player.setDisabled(True)
                            if self.parent().Add_Player in self.parent().buttons:
                                self.parent().buttons.remove(self.parent().Add_Player)
                    else:
                        QMessageBox.critical(self, 'Wrong', 'This user exists', QMessageBox.Ok, QMessageBox.Ok)
                    self.username.clear()
                    self.password.clear()
                    self.close()
                    break
            else:
                QMessageBox.warning(self, 'Wrong', 'Username or Password is incorrect', QMessageBox.Ok, QMessageBox.Ok)

    def combo_box_reset(self):
        self.color_box.clear()
        self.color_box.addItem('Red')
        self.color_box.addItem('Blue')
        self.color_box.addItem('Green')
        self.color_box.addItem('Yellow')
