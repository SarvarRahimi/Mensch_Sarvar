from piece import Piece


def set_val(parent):
    parent.setWindowTitle('Mensch Game')
    parent.setGeometry(310, 40, 900, 743)
    parent.players = {}
    parent.names = [parent.player_1, parent.player_2, parent.player_3, parent.player_4]
    parent.buttons = [parent.Add_Player, parent.Start_Game, parent.New_Game, parent.Exit, parent.Roll_Button]
    parent.colors = {'yellow': '#ffff00', 'red': '#ff0000', 'blue': '#0285ff', 'green': '#00ff00'}
    parent.roll_nums = {1: 'icons/one.png', 2: 'icons/two.png', 3: 'icons/three.png', 4: 'icons/four.png',
                        5: 'icons/five.png', 6: 'icons/six.png'}

    parent.home = {
        'yellow': [parent.yellow_home_1, parent.yellow_home_2, parent.yellow_home_3, parent.yellow_home_4],
        'red': [parent.red_home_1, parent.red_home_2, parent.red_home_3, parent.red_home_4],
        'blue': [parent.blue_home_1, parent.blue_home_2, parent.blue_home_3, parent.blue_home_4],
        'green': [parent.green_home_1, parent.green_home_2, parent.green_home_3, parent.green_home_4]
    }

    parent.paths = {
        'blue': [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5, parent.label6,
                 parent.label7, parent.label8, parent.label9, parent.label10, parent.label11, parent.label12,
                 parent.label13, parent.label14, parent.label15, parent.label16, parent.label17, parent.label18,
                 parent.label19, parent.label20, parent.label21, parent.label22, parent.label23, parent.label24,
                 parent.label25, parent.label26, parent.label27, parent.label28, parent.label29, parent.label30,
                 parent.label31, parent.label32, parent.label33, parent.label34, parent.label35, parent.label36,
                 parent.label37, parent.label38, parent.label39, parent.label40, parent.blue_win_1, parent.blue_win_2,
                 parent.blue_win_3, parent.blue_win_4],

        'red': [parent.label11, parent.label12, parent.label13, parent.label14, parent.label15, parent.label16,
                parent.label17, parent.label18, parent.label19, parent.label20, parent.label21, parent.label22,
                parent.label23, parent.label24, parent.label25, parent.label26, parent.label27, parent.label28,
                parent.label29, parent.label30, parent.label31, parent.label32, parent.label33, parent.label34,
                parent.label35, parent.label36, parent.label37, parent.label38, parent.label39, parent.label40,
                parent.label1, parent.label2, parent.label3, parent.label4, parent.label5, parent.label6, parent.label7,
                parent.label8, parent.label9, parent.label10, parent.red_win_1, parent.red_win_2, parent.red_win_3,
                parent.red_win_4],

        'green': [parent.label21, parent.label22, parent.label23, parent.label24, parent.label25, parent.label26,
                  parent.label27, parent.label28, parent.label29, parent.label30, parent.label31, parent.label32,
                  parent.label33, parent.label34, parent.label35, parent.label36, parent.label37, parent.label38,
                  parent.label39, parent.label40],

        'yellow': [parent.label1, parent.label2, parent.label3, parent.label4, parent.label5, parent.label6,
                   parent.label7, parent.label8, parent.label9, parent.label10, parent.label11, parent.label12,
                   parent.label13, parent.label14, parent.label15, parent.label16, parent.label17,
                   parent.label18, parent.label19, parent.label20, parent.label21, parent.label22, parent.label23,
                   parent.label24, parent.label25, parent.label26, parent.label27, parent.label28, parent.label29,
                   parent.label30, parent.label31, parent.label32, parent.label33, parent.label34, parent.label35,
                   parent.label36, parent.label37, parent.label38, parent.label39, parent.label40, parent.blue_win_1,
                   parent.blue_win_2, parent.blue_win_3, parent.blue_win_4]
    }

    parent.pieces = {
        'yellow': [Piece(parent.pieces_board, 'yellow', parent.home['yellow'], parent.paths['yellow'])
                   for _ in range(4)],
        'red': [Piece(parent.pieces_board, 'red', parent.home['red'], parent.paths['red']) for _ in range(4)],
        'blue': [Piece(parent.pieces_board, 'blue', parent.home['blue'], parent.paths['blue']) for _ in range(4)],
        'green': [Piece(parent.pieces_board, 'green', parent.home['green'], parent.paths['green']) for _ in range(4)]
    }
