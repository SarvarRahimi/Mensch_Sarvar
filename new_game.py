from PyQt5.QtWidgets import QMessageBox


def new_game_func(parent, msgbox=True):

    result = None
    if msgbox:
        result = QMessageBox.warning(parent, 'New Game', 'wanna play a New Game?',
                                                         QMessageBox.Ok | QMessageBox.Cancel,
                                                         QMessageBox.Cancel)

    if result == QMessageBox.Ok or not msgbox:
        for key in parent.pieces.keys():
            for pic in parent.pieces[key]:
                pic.setDisabled(True)
                pic.setVisible(False)
                pic.setGeometry(330, 330, 60, 60)

        parent.players.clear()

        for btn in parent.btn_list:
            btn.setDisabled(True)

        if parent.add_player in parent.btn_list:
            parent.btn_list.append(parent.add_player)

        parent.add_player.setEnabled(True)
        parent.exit_game.setEnabled(True)

        for name in parent.names:
            name.setText('')

        parent.login.combo_box_reset()
        parent.turn_name.setText('')
