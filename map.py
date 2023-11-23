import pygame as pg
from settings import *
import random

_ = False
maplayout = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout1 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [_, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, _, _, _],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout2 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [_, _, _, _, _, _, 1, 1],
             [1, 1, 1, 1, 1, _, 1, 1],
             [1, 1, 1, 1, 1, _, 1, 1],
             [1, 1, 1, 1, 1, _, _, _],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout3 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, _, _],
             [1, 1, 1, 1, 1, 1, _, 1],
             [_, _, _, _, _, _, _, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout4 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, _, _, _, _, _],
             [1, 1, 1, _, 1, 1, 1, 1],
             [1, 1, 1, _, 1, 1, 1, 1],
             [_, _, _, _, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 5]]


class Map:
    def __init__(self, main):
        self.main = main
        self.maplayout = maplayout
        self.mapfinal = {}
        self.get_map()
        self.x, self.y = PLAYER_POS
        
    def get_map(self):
        rannum = random.randint(1, 4)
        if rannum == 1:
            self.maplayout = maplayout1
        elif rannum == 2:
            self.maplayout = maplayout2
        elif rannum == 3:
            self.maplayout = maplayout3
        elif rannum == 4:
            self.maplayout = maplayout4
            
        for j, row in enumerate(self.maplayout):
            for i, value in enumerate(row):
                if value:
                    self.mapfinal[(i, j)] = value
                    print(self.mapfinal)
                    
        print(self.mapfinal)
        
    def draw(self):
        [pg.draw.rect(self.main.display, (72, 102, 120, 1), (pos[0] * 40, pos[1] * 40, 40, 40), 40) for pos in self.mapfinal]