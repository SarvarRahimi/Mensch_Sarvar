from itertools import cycle
from random import randint
# from .player import Player

players = [1, 2, 3, 4]
colors = cycle(players)


def dice():
    return randint(range(1, 7))
