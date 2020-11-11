class Peace:
    path = {
        'blue': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        'red': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6],
        'green': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'yellow': [19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    }

    def __init__(self, color, player):
        self.color = color
        self.home_positions = {'red': 25, 'green': 26, 'yellow': 27, 'blue': 28}
        self.win_position = {'red': 29, 'green': 30, 'yellow': 31, 'blue': 32}
        self.position = self.home_positions[self.color]
        self.is_in_home = True
        self.player = player
        self.count = 0
        self.win = False
        self.index = 0

    def move(self, number):
        if self.is_in_home:
            self.position = Peace.path[self.color][self.index]
            self.count += 1
            self.is_in_home = False
        else:
            self.index += number
            self.position = Peace.path[self.color][self.index]

    def remove(self):
        self.position = self.home_positions[self.color]
        self.is_in_home = True

    def win(self):
        if self.count == 25:
            self.win = True
            self.position = self.win_position[self.color]