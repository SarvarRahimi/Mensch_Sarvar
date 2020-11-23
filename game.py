from functools import reduce
from random import randint

from PyQt5.QtCore import QPropertyAnimation, QTimer
from PyQt5.QtGui import QPixmap
from finish_dialog import FinishDialog


class Game:

    def __init__(self, parent):

        self.parent = parent
        self.num = None
        self.play_dict = None
        self.win_list = None
        self.color_list = None
        self.turn = None
        self.first_step()
        self.parent.roll_dice.clicked.connect(lambda: self.onClick_roll_dice())
        for pic_list in self.parent.pieces.values():
            for pic in pic_list:
                pic.clicked.connect(lambda tmp, p=pic: self.move_piece(p))

    def first_step(self):
        self.parent.add_player.setDisabled(True)
        self.parent.start_game.setDisabled(True)
        self.parent.new_game.setEnabled(True)
        self.parent.roll_dice.setEnabled(True)
        self.num = 0
        self.play_dict = self.parent.players
        self.win_list = []
        self.color_list = [*self.parent.players.keys()]
        self.turn = self.color_list[0]
        self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        self.parent.turn_name.setStyleSheet(
            f"""color: {self.parent.color_code[self.turn]};
                        border: 0 solid rgba(0,0,0,0);""")

    def next_turn(self):
        self.play_dict[self.turn].roll_num = 0
        self.turn = self.color_list[(self.color_list.index(self.turn) + 1) % len(self.color_list)]
        self.parent.turn_name.setText(f'Turn: {self.play_dict[self.turn].username}')
        self.parent.turn_name.setStyleSheet(
            f"""color: {self.parent.color_code[self.turn]};
                border: 0 solid rgba(0,0,0,0);""")

    def onClick_roll_dice(self):
        self.num = randint(1, 6)
        self.parent.roll_dice.setDisabled(True)

        length = 1.3
        QTimer.singleShot(length * 500, lambda: self.inner_func())

    def inner_func(self):
        self.parent.dice_label.setPixmap(QPixmap(self.parent.roll_nums[self.num]))

        move_dict = self.play_dict[self.turn].has_move(self.num)
        if reduce((lambda x, y: x or y), move_dict.values()) or self.num == 6:
            if not reduce((lambda x, y: x or y), move_dict.values()) and self.num == 6:
                self.parent.roll_dice.setEnabled(True)
            for pic, value in move_dict.items():
                pic.setEnabled(value)
        else:
            self.parent.roll_dice.setEnabled(True)
            if self.play_dict[self.turn].is_gamer():
                self.next_turn()
            else:
                if self.play_dict[self.turn].roll_num < 2:
                    self.play_dict[self.turn].roll_num += 1
                else:
                    self.next_turn()

    def move_piece(self, pic):
        deley = pic.smooth_move(self.num)

        for pic_ in self.play_dict[self.turn].pieces:
            pic_.setDisabled(True)

        QTimer.singleShot(deley, lambda: after_move())

        def after_move():
            nonlocal self, pic
            self.play_dict[self.turn].roll_num = 0

            if reduce((lambda x, y: x and y), [m.is_in_home() for m in self.play_dict[self.turn].pieces]):
                win_color = self.turn
                self.next_turn()
                self.num = 0
                self.color_list.remove(win_color)
                self.win_list.append((self.play_dict[win_color].username, win_color))
                del self.play_dict[win_color]

            if not self.play_dict:
                names = ' '.join(w[0] for w in self.win_list)
                colors = ' '.join(w[1] for w in self.win_list)
                self.parent.finish = FinishDialog(self.parent, names, colors)
                self.parent.finish.exec_()
                return

            if 0 < self.num < 6:
                self.next_turn()

            for plyr in (p for p in self.play_dict.values() if pic not in p.pieces):
                for p in plyr.pieces:
                    if pic.geometry() == p.geometry():
                        for b in plyr.bases:
                            if b.geometry() not in [m.geometry() for m in plyr.pieces]:
                                self.anim = QPropertyAnimation(p, b"geometry")
                                self.anim.setDuration(500)
                                self.anim.setEndValue(b.geometry())
                                self.anim.start()
                                QTimer.singleShot(500, lambda: self.parent.roll_dice.setEnabled(True))
                                return

            self.parent.roll_dice.setEnabled(True)
