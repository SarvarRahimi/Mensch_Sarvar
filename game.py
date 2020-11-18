import logging
from functools import reduce
from random import randint
from PyQt5.QtCore import QPropertyAnimation, QTimer
from PyQt5.QtGui import QIcon
from game_over import GameOver


class Game:

    def __init__(self, parent):
        self.parent = parent

        self.game_logger = logging.getLogger('mensch')
        self.file_handler = logging.FileHandler('mensch.log')
        self.file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s', datefmt='%y-%m-%d %H:%M:%S'))
        self.game_logger.setLevel(logging.INFO)
        self.game_logger.addHandler(self.file_handler)

        self.first()
        self.num = None
        self.play_dict = None
        self.win_list = None
        self.color_list = None
        self.turn = None

        self.parent.Roll_Button.clicked.connect(lambda: self.Roll_Button_func())

        for pic_list in self.parent.pieces.values():
            for pic in pic_list:
                pic.clicked.connect(lambda tmp, p=pic: self.move_piece(p))

    def __del__(self):
        self.file_handler.close()

    def first(self):
        self.parent.Add_Player.setDisabled(True)
        self.parent.Start_Game.setDisabled(True)
        self.parent.New_Game.setEnabled(True)
        self.parent.Roll_Button.setEnabled(True)
        self.num = 0
        self.play_dict = self.parent.players
        self.win_list = []
        self.color_list = [*self.parent.players.keys()]
        self.turn = self.color_list[0]
        self.parent.player_turn.setText(f'{self.play_dict[self.turn].username}')
        self.parent.player_turn.setStyleSheet(
            f"""color: {self.parent.colors[self.turn]}; border: 0 solid rgba(0,0,0,0);""")

    def next_turn(self):
        self.play_dict[self.turn].roll = 0
        self.turn = self.color_list[(self.color_list.index(self.turn) + 1) % len(self.color_list)]
        self.parent.player_turn.setText(f'{self.play_dict[self.turn].username}')
        self.parent.player_turn.setStyleSheet(f"""color: {self.parent.colors[self.turn]}; 
                                                                                    border: 0 solid rgba(0,0,0,0);""")

    def Roll_Button_func(self):
        self.num = randint(1, 6)
        self.parent.Roll_Button.setDisabled(True)
        self.parent.Roll_Button.setIcon(QIcon(self.parent.roll_nums[self.num]))
        move_dict = self.play_dict[self.turn].has_move(self.num)
        if reduce((lambda x, y: x or y), move_dict.values()) or self.num == 6:
            if not reduce((lambda x, y: x or y), move_dict.values()) and self.num == 6:
                self.parent.Roll_Button.setEnabled(True)
            for pic, value in move_dict.items():
                pic.setEnabled(value)
        else:
            self.parent.Roll_Button.setEnabled(True)
            if self.play_dict[self.turn].is_gamer():
                self.next_turn()
            else:
                if self.play_dict[self.turn].roll_num < 2:
                    self.play_dict[self.turn].roll_num += 1
                else:
                    self.next_turn()

    def move_piece(self, pic):
        delay = pic.move(self.num)

        for pic_ in self.play_dict[self.turn].pieces:
            pic_.setDisabled(True)

        QTimer.singleShot(delay, lambda: after_move())

        def after_move():
            nonlocal self, pic
            self.play_dict[self.turn].roll = 0

            if reduce((lambda x, y: x and y), [p.is_in_home() for p in self.play_dict[self.turn].pieces]):
                win_color = self.turn
                self.next_turn()
                self.num = 0
                self.color_list.remove(win_color)
                self.win_list.append((self.play_dict[win_color].username, win_color))
                del self.play_dict[win_color]

            if not self.play_dict:
                names = ' '.join(w[0] for w in self.win_list)
                colors = ' '.join(w[1] for w in self.win_list)
                self.game_logger.info(names)
                self.parent.finish = GameOver(self.parent, names, colors)
                self.parent.finish.exec_()
                return

            if 0 < self.num < 6:
                self.next_turn()

            for player in (p for p in self.play_dict.values() if pic not in p.pieces):
                for p in player.pieces:
                    if pic.geometry() == p.geometry():
                        for b in player.home:
                            if b.geometry() not in [m.geometry() for m in player.pieces]:
                                self.anim = QPropertyAnimation(p, b"geometry")
                                self.anim.setDuration(300)
                                self.anim.setEndValue(b.geometry())
                                self.anim.start()
                                QTimer.singleShot(300, lambda: self.parent.Roll_Button.setEnabled(True))
                                return

            self.parent.Roll_Button.setEnabled(True)
