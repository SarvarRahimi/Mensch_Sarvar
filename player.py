from functools import reduce


class Player:
    def __init__(self, username, pieces, home, paths):
        self.username = username
        self.pieces = pieces
        self.home = home
        self.paths = paths
        self.roll = 0
        for element in self.pieces:
            element.setVisible(True)

    def is_gamer(self):
        return reduce((lambda x, y: x or y), [p.is_in_game() for p in self.pieces])

    def has_move(self, number):
        res = {pic: False for pic in self.pieces}
        for pic in self.pieces:
            list_pics = self.pieces[:]
            list_pics.remove(pic)
            if pic.is_in_base() and number == 6 and not \
                    reduce((lambda x, y: x or y), [p.geometry() == self.paths[0].geometry() for p in list_pics]):
                res[pic] = True
        for pic in self.pieces:
            if pic.is_in_game() or pic.is_win():
                list_pics = self.pieces[:]
                list_pics.remove(pic)
                p_i = [pos.geometry() for pos in self.paths].index(pic.geometry()) + number
                if p_i < len(self.paths) and not \
                        reduce((lambda x, y: x or y), [p.geometry() == self.paths[p_i].geometry() for p in list_pics]):
                    res[pic] = True
        return res
