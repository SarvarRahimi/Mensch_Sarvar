from itertools import cycle
from random import randint
from .player import Player
from .piece import Peace

players = []

a = Player('Thomas', 'red')
b = Player('zeus', 'blue')

players.append(a)
players.append(b)

turn = cycle(players)


def dice():
    return randint(range(1, 7))


def is_empty(first_piece, number):
    new_index = first_piece.index + number
    pos2 = Peace.path[first_piece.color][new_index]
    for player in players:
        for pic in player.piece_in_yard:
            if pic.position == pos2:
                return pic
    return True


while True:
    if (len(players) >= 2) or (len(players) <= 4):
        player_turn = turn.__next__()
        if player_turn.piece_in_yard == 0:
            for i in range(3):
                dice_number = dice()
                if dice_number == 6:
                    player_turn_piece = player_turn.pieces_in_home[randint(range(1, 5))]
                    player_turn_piece.move(dice_number)
                    break
        else:
            dice_number = dice()
            player_turn_piece = player_turn.piece_in_yard[0]
            if dice_number == 6:
                while dice_number == 6:
                    if not is_empty(player_turn_piece, dice_number):
                        remove_piece = is_empty(player_turn_piece, dice_number)
                        if remove_piece.player != player_turn_piece:
                            remove_piece.remove()
                            player_turn_piece.move(dice_number)
                    else:
                        player_turn_piece.move(dice_number)
            else:
                if not is_empty(player_turn_piece, dice_number):
                    remove_piece = is_empty(player_turn_piece, dice_number)
                    if remove_piece.player != player_turn_piece:
                        remove_piece.remove()
                        player_turn_piece.move(dice_number)
                else:
                    player_turn_piece.move(dice_number)
