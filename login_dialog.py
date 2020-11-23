from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from player import Player


def login_animate(parent, color):
    parent.parallel_animation_group = QParallelAnimationGroup()
    parent.anim = None
    for i in range(4):
        parent.anim = QPropertyAnimation(parent.pieces[color][i], b"geometry")
        parent.anim.setDuration(1000)
        parent.anim.setEndValue(parent.bases[color][i].geometry())
        parent.parallel_animation_group.addAnimation(parent.anim)

    parent.parallel_animation_group.start()


class LoginDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        loadUi('ui/login_ui.ui', self)

        self.login_btn.clicked.connect(self.is_valid)
        self.cancel_btn.clicked.connect(self.close)

    def is_valid(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()
        color = self.color_combo_box.currentText().lower()

        with open('Players_list.txt') as file:
            for line in file:
                username_, password_ = line.split()
                if username == username_ and password == password_:
                    if username not in self.parent().players.keys():
                        player = Player(username, self.parent().pieces[color], self.parent().bases[color],
                                        self.parent().positions[color])
                        self.parent().players[color] = player
                        self.color_combo_box.removeItem(self.color_combo_box.currentIndex())
                        self.parent().names[len(self.parent().players) - 1].setText(player.username)
                        self.parent().names[len(self.parent().players) - 1].setStyleSheet(
                            f"""color: {self.parent().color_code[color]};
                                border: 0 solid rgba(0,0,0,0);""")
                        login_animate(self.parent(), color)
                        if len(self.parent().players) > 1 and not self.parent().start_game.isEnabled():
                            self.parent().start_game.setEnabled(True)
                        if len(self.parent().players) > 3:
                            self.parent().add_player.setDisabled(True)
                            if self.parent().add_player in self.parent().btn_list:
                                self.parent().btn_list.remove(self.parent().add_player)
                    else:
                        QMessageBox.critical(self, 'Wrong Input', 'This user already exist.', QMessageBox.Ok,
                                             QMessageBox.Ok)

                    self.username_line_edit.clear()
                    self.password_line_edit.clear()
                    self.close()
                    break
            else:
                QMessageBox.warning(self, 'Wrong Input', 'Username or Password is incorrect.', QMessageBox.Ok,
                                    QMessageBox.Ok)

    def combo_box_reset(self):
        self.color_combo_box.clear()
        self.color_combo_box.addItem('Red')
        self.color_combo_box.addItem('Blue')
        self.color_combo_box.addItem('Green')
        self.color_combo_box.addItem('Yellow')
