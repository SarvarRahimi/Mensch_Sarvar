from PyQt5.QtWidgets import QMessageBox


def new_game_func(parent, flag=True):
    result = None
    if flag:
        result = QMessageBox.warning(parent, 'New Game', 'wanna play a New Game?',
                                                         QMessageBox.Ok | QMessageBox.Cancel,
                                                         QMessageBox.Cancel)

    if result == QMessageBox.Ok or not flag:
        for key in parent.pieces.keys():
            for pic in parent.pieces[key]:
                pic.setDisabled(True)
                pic.setVisible(False)
                pic.setGeometry(410, 410, 69, 69)

        parent.players.clear()

        for btn in parent.buttons:
            btn.setDisabled(True)

        if parent.Add_Player in parent.buttons:
            parent.buttons.append(parent.Add_Player)

        parent.Add_Player.setEnabled(True)
        parent.Exit.setEnabled(True)

        for name in parent.names:
            name.setText('')

        parent.login.combo_box_reset()
        parent.player_turn.setText('')