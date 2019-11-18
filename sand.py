#!/usr/bin/env python3
import itertools
import math


class Sand:
    def __init__(self,
                 x: int,
                 y: int,
                 count: int = 0,
                 neighbors: [] = []
                 ):
        self.count = count
        self.x = x
        self.y = y
        self.neighbors = neighbors

    def __repr__(self):
        return f'{self.x}, {self.y} -> {self.count} N:{len(self.neighbors)}'

    def set_neighbors(self,
                      neighbors: []
                      ):
        self.neighbors = neighbors

    def increment(self,
                  amount: int):
        self.count += amount

    def topple(self):
        if self.count >= 4:
            for _neighbor in self.neighbors:
                _neighbor.increment(1)
            self. count -= 4


class Pile:

    # Dict of special identity piles
    zeroes = {4: [[2, 2],
                  [2, 2]],
              9: [[2, 1, 2],
                  [1, 0, 1],
                  [2, 1, 2]],
              16: [[2, 3, 3, 2],
                   [3, 2, 2, 3],
                   [3, 2, 2, 3],
                   [2, 3, 3, 2]]}

    def __init__(self,
                 items: [[]] = []
                 ):
        self.sand = []

        if items == []:
            for x, y in itertools.product(range(0, self.__class__.height),
                                          range(0, self.__class__.width)):
                self.sand.append(Sand(x, y, count=0))

        else:
            for row in range(0, len(items)):
                for column in range(0, len(items[row])):
                    self.sand.append(Sand(column,
                                          row,
                                          count=items[row][column]))
        self.define_neighbors()

    def __repr__(self):
        rep = ''
        for row in [self.sand[i:i+self.__class__.width] for
                    i in range(0, len(self.sand), self.__class__.width)]:
            rep += str([item.count for item in row]) + "\n"

        return rep

    @classmethod
    def max_pile(cls):
        return Pile([[3] * cls.width] * cls.height)

    @classmethod
    def zero(cls):
        return Pile(cls.zeroes[cls.height * cls.width])

    @classmethod
    def set_dims(cls,
                 square: int = 16,
                 ):
        if math.sqrt(square) % 1 != 0:
            print("Size must be a square!")
            return

        cls.width = cls.height = int(math.sqrt(square))

    def define_neighbors(self):
        for _sand in self.sand:
            _sand.set_neighbors([candidate for candidate in self.sand
                                 if candidate.x == _sand.x
                                 and abs(_sand.y - candidate.y) == 1
                                 or candidate.y == _sand.y
                                 and abs(_sand.x - candidate.x) == 1])

    def unwieldy(self) -> bool:
        return [_sand for _sand in self.sand if _sand.count >= 4]

    def balance(self):
        # Recursively topple sand
        _unwieldy = self.unwieldy()

        if _unwieldy == []:
            return

        _sorted = sorted(_unwieldy,
                         key=(lambda x: x.count),
                         reverse=True)

        for item in [_sand for _sand in _sorted
                     if (_sand.count == _sorted[0].count)]:
            item.topple()

        self.balance()

    def add(self,
            pile
            ):
        for i in range(0, len(pile.sand)):
            self.sand[i].count += pile.sand[i].count

        self.balance()
