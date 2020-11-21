from PyQt5.QtWidgets import QApplication
from add_player import Login
from new_game import new_game_func


def init_menu(parent):
    parent.login = Login(parent)
    parent.Add_Player.triggered.connect(parent.login.exec_)
    parent.Start_Game.triggered.connect(parent.init_game)
    parent.Start_Game.setDisabled(True)
    parent.New_Game.triggered.connect(lambda: new_game_func(parent))
    parent.New_Game.setDisabled(True)
    parent.Exit.triggered.connect(QApplication.exit)
    parent.Roll_Button.setDisabled(True)
