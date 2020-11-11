from itertools import cycle
from random import randint
from .player import Player
# from .piece import Peace

players = []

a = Player('Thomas', 'red')
b = Player('zeus', 'blue')

players.append(a)
players.append(b)

turn = cycle(players)


def dice():
    return randint(range(1, 7))


while True:
    if (len(players) >= 2) and (len(players) <= 4):
        player_turn = turn.__next__()
        if player_turn.piece_in_yard == 0:
            for i in range(3):
                dice_number = dice()
                if dice_number == 6:
                    player_turn_piece = player_turn.pieces[randint(range(1, 5))]
                    player_turn_piece.move(dice_number)
                    break
