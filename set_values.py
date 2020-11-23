from PyQt5.QtGui import QIcon
from piece import Piece


def set_val(parent):
    parent.setWindowTitle('Mensch Game')
    parent.setWindowIcon(QIcon('ressource/dice_6.png'))
    parent.setGeometry(200, 40, 1150, 980)

    parent.bases = {
        'yellow': [parent.base_yellow_0, parent.base_yellow_1, parent.base_yellow_2, parent.base_yellow_3],
        'red': [parent.base_red_0, parent.base_red_1, parent.base_red_2, parent.base_red_3],
        'blue': [parent.base_blue_0, parent.base_blue_1, parent.base_blue_2, parent.base_blue_3],
        'green': [parent.base_green_0, parent.base_green_1, parent.base_green_2, parent.base_green_3]
    }

    parent.btn_list = [parent.add_player, parent.start_game, parent.new_game, parent.exit_game, parent.roll_dice]

    parent.color_code = {
        'yellow': '#F8D823',
        'red': '#EF0B0E',
        'blue': '#1334C4',
        'green': '#297C29'
    }

    parent.roll_nums = {
        1: 'ressource/dice_1.png',
        2: 'ressource/dice_2.png',
        3: 'ressource/dice_3.png',
        4: 'ressource/dice_4.png',
        5: 'ressource/dice_5.png',
        6: 'ressource/dice_6.png'
    }

    parent.players = {}

    parent.names = [parent.name_1, parent.name_2, parent.name_3, parent.name_4]

    parent.positions = {
        'yellow': [parent.start_yellow, parent.yellow_1, parent.yellow_2, parent.yellow_3, parent.yellow_4,
                   parent.yellow_5, parent.yellow_6, parent.yellow_7, parent.yellow_8, parent.yellow_9,
                   parent.start_red, parent.red_1, parent.red_2, parent.red_3, parent.red_4, parent.red_5, parent.red_6,
                   parent.red_7, parent.red_8, parent.red_9, parent.start_blue, parent.blue_1, parent.blue_2,
                   parent.blue_3, parent.blue_4, parent.blue_5, parent.blue_6, parent.blue_7, parent.blue_8,
                   parent.blue_9, parent.start_green, parent.green_1, parent.green_2, parent.green_3, parent.green_4,
                   parent.green_5, parent.green_6, parent.green_7, parent.green_8, parent.green_9, parent.home_yellow_0,
                   parent.home_yellow_1, parent.home_yellow_2, parent.home_yellow_3],
        'red': [parent.start_red, parent.red_1, parent.red_2, parent.red_3, parent.red_4, parent.red_5, parent.red_6,
                parent.red_7, parent.red_8, parent.red_9, parent.start_blue, parent.blue_1, parent.blue_2,
                parent.blue_3, parent.blue_4, parent.blue_5, parent.blue_6, parent.blue_7, parent.blue_8,
                parent.blue_9, parent.start_green, parent.green_1, parent.green_2, parent.green_3, parent.green_4,
                parent.green_5, parent.green_6, parent.green_7, parent.green_8, parent.green_9, parent.start_yellow,
                parent.yellow_1, parent.yellow_2, parent.yellow_3, parent.yellow_4, parent.yellow_5, parent.yellow_6,
                parent.yellow_7, parent.yellow_8, parent.yellow_9, parent.home_red_0, parent.home_red_1,
                parent.home_red_2, parent.home_red_3],
        'blue': [parent.start_blue, parent.blue_1, parent.blue_2, parent.blue_3, parent.blue_4, parent.blue_5,
                 parent.blue_6, parent.blue_7, parent.blue_8, parent.blue_9, parent.start_green, parent.green_1,
                 parent.green_2, parent.green_3, parent.green_4, parent.green_5, parent.green_6, parent.green_7,
                 parent.green_8, parent.green_9, parent.start_yellow, parent.yellow_1, parent.yellow_2, parent.yellow_3,
                 parent.yellow_4, parent.yellow_5, parent.yellow_6, parent.yellow_7, parent.yellow_8, parent.yellow_9,
                 parent.start_red, parent.red_1, parent.red_2, parent.red_3, parent.red_4, parent.red_5, parent.red_6,
                 parent.red_7, parent.red_8, parent.red_9, parent.home_blue_0, parent.home_blue_1, parent.home_blue_2,
                 parent.home_blue_3],
        'green': [parent.start_green, parent.green_1,
                  parent.green_2, parent.green_3, parent.green_4, parent.green_5, parent.green_6, parent.green_7,
                  parent.green_8, parent.green_9, parent.start_yellow, parent.yellow_1, parent.yellow_2,
                  parent.yellow_3,
                  parent.yellow_4, parent.yellow_5, parent.yellow_6, parent.yellow_7, parent.yellow_8, parent.yellow_9,
                  parent.start_red, parent.red_1, parent.red_2, parent.red_3, parent.red_4, parent.red_5, parent.red_6,
                  parent.red_7, parent.red_8, parent.red_9, parent.start_blue, parent.blue_1, parent.blue_2,
                  parent.blue_3, parent.blue_4, parent.blue_5, parent.blue_6, parent.blue_7, parent.blue_8,
                  parent.blue_9, parent.home_green_0, parent.home_green_1, parent.home_green_2, parent.home_green_3]
    }

    parent.pieces = {
        'yellow': [Piece(parent.main_board, 'yellow', parent.bases['yellow'], parent.positions['yellow']) for _ in range(4)],
        'red': [Piece(parent.main_board, 'red', parent.bases['red'], parent.positions['red']) for _ in range(4)],
        'blue': [Piece(parent.main_board, 'blue', parent.bases['blue'], parent.positions['blue']) for _ in range(4)],
        'green': [Piece(parent.main_board, 'green', parent.bases['green'], parent.positions['green']) for _ in range(4)]
    }
