from PyQt5.QtWidgets import QApplication


from login_dialog import LoginDialog
from new_game import new_game_func


def init_menu(parent):

    parent.login = LoginDialog(parent)
    parent.add_player.triggered.connect(parent.login.exec_)

    parent.start_game.triggered.connect(parent.init_game)
    parent.start_game.setDisabled(True)

    parent.new_game.triggered.connect(lambda: new_game_func(parent))
    parent.new_game.setDisabled(True)

    parent.exit_game.triggered.connect(QApplication.exit)

    parent.roll_dice.setDisabled(True)
