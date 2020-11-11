from .piece import Peace


class Player:
    def __init__(self, user_name, color):
        self.user_name = user_name
        self.allow_colors = ['red', 'green', 'yellow', 'blue']

        if color in self.allow_colors:
            self.color = color
        else:
            raise ValueError('this color is not value!')

        self.piece_in_home = 4
        self.piece_in_yard = 0
        self.win_piece = 0
        self.pieces = [Peace(self.color, self) for _ in range(self.piece_in_home)]
