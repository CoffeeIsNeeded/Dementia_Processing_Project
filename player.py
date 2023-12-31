import pygame as pg
from settings import *

class Player:
    def __init__(self, main):
        self.main = main
        self.x, self.y = PLAYER_POS
        
    def movement(self):
        x_change, y_change = 0, 0
        
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            y_change -= 1
            pg.time.wait(500)
        if key[pg.K_s]:
            y_change += 1
            pg.time.wait(500)
        if key[pg.K_a]:
            x_change -= 1
            pg.time.wait(500)
        if key[pg.K_d]:
            x_change += 1
            pg.time.wait(500)

        self.wall_collision(x_change, y_change)

    def wall_check(self, x, y):
        return (x, y) not in self.main.map.mapfinal
    
    def wall_collision(self, x_change, y_change):
        if self.wall_check(int(self.x + x_change), int(self.y)):
            self.x += x_change
        else:
            self.x, self.y = PLAYER_START1
            if not self.wall_check(int(self.x), int(self.y)):
                self.x, self.y = PLAYER_START2
            pg.time.wait(1000)
        if self.wall_check(int(self.x), int(self.y + y_change)):
            self.y += y_change
        else:
            self.x, self.y = PLAYER_START1
            if not self.wall_check(int(self.x), int(self.y)):
                self.x, self.y = PLAYER_START2
            pg.time.wait(1000)

    def update(self):
        self.movement()
    
    def draw(self):
        pg.draw.circle(self.main.display, (121, 52, 158, 1), (self.x * 40, self.y * 40), 15)
        pg.draw.circle(self.main.display, (196, 87, 255, 1), (self.x * 40, self.y * 40), 10)
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)