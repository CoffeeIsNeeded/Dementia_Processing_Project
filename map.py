import pygame as pg
from settings import *
import random
import time

_ = None
maplayout = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout1 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, 1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, _, _, 2],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout2 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, _, 1, 1],
             [1, 1, 1, 1, 1, _, 1, 1],
             [1, 1, 1, 1, 1, _, 1, 1],
             [1, 1, 1, 1, 1, _, _, 2],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout3 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, _, 2],
             [1, 1, 1, 1, 1, 1, _, 1],
             [1, _, _, _, _, _, _, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

maplayout4 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, _, _, _, _, 2],
             [1, 1, 1, _, 1, 1, 1, 1],
             [1, 1, 1, _, 1, 1, 1, 1],
             [1, _, _, _, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

class Map:
    def __init__(self, main):
        self.main = main
        self.maplayout = maplayout
        self.mapfinal = {}
        self.finish_square = []
        self.get_map()
        self.x, self.y = PLAYER_POS
        self.time_end = (self.return_time() + 10)
        
    def get_map(self):
        rannum = random.randint(1, 4)
        if rannum == 1:
            self.maplayout = maplayout1
            self.finish_square = 7, 5
        elif rannum == 2:
            self.maplayout = maplayout2
            self.finish_square = 7, 4
        elif rannum == 3:
            self.maplayout = maplayout3
            self.finish_square = 7, 2
        elif rannum == 4:
            self.maplayout = maplayout4
            self.finish_square = 7, 1
            
        for j, row in enumerate(self.maplayout):
            for i, value in enumerate(row):
                if value is not None:
                    self.mapfinal[(i, j)] = value
        
    def return_time(self):
        return time.time()
    
    def draw(self):
        for pos, value in self.mapfinal.items():
            match value:
                case 1:
                    colour = (72, 102, 120, 1)
                case 2:
                    colour = (0, 255, 0, 1)
            aabb = (pos[0] * 40, pos[1] * 40, 40, 40)
            
            time = self.return_time()
            if time > self.time_end:
                colour = (STAND_BACK_COL)
            pg.draw.rect(self.main.display, colour, aabb, 40)