from .piece import Peace


class Player:
    def __init__(self, user_name, color):
        self.user_name = user_name
        self.allow_colors = ['red', 'green', 'yellow', 'blue']

        if color in self.allow_colors:
            self.color = color
        else:
            raise ValueError('this color is not value!')

        self.pieces_in_home = [Peace(self.color, self) for _ in range(4)]
        self.piece_in_yard = []
        self.win_piece = []
