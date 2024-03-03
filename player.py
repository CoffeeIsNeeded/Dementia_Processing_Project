import pygame as pg
import time

from settings import *

class Player:
    def __init__(self, main):
        self.main = main
        self.x, self.y = PLAYER_POS
        self.time_total = 0
        self.completion = 0
        self.game_stop = False
        self.time_end = (self.return_time() + 10)
        
    def return_time(self):
        return time.time()
    
    def movement(self):
        time = self.return_time()
        if time > self.time_end:
            x_change, y_change = 0, 0
        
            key = pg.key.get_pressed()
            if key[pg.K_UP]:
                y_change -= 1
                pg.time.wait(500)
                self.time_total += 500
            if key[pg.K_DOWN]:
                y_change += 1
                pg.time.wait(500)
                self.time_total += 500
            if key[pg.K_LEFT]:
                x_change -= 1
                pg.time.wait(500)
                self.time_total += 500
            if key[pg.K_RIGHT]:
                x_change += 1
                pg.time.wait(500)
                self.time_total += 500

            self.wall_collision(x_change, y_change)

    def finish_check(self, x, y):
        x, y = self.main.map.finish_square
        return [x, y]
    
    def wall_check(self, x, y):
        return (x, y) not in self.main.map.mapfinal
    
    def wall_collision(self, x_change, y_change):

        if self.wall_check(int(self.x + x_change), int(self.y)):
            self.x += x_change
        elif self.finish_check((self.x), (self.y)) == [int(self.x + x_change), int(self.y)]:
            self.game_stop = True
        else:
            self.x, self.y = PLAYER_START1
            if not self.wall_check(int(self.x), int(self.y)):
                self.x, self.y = PLAYER_START2
            pg.time.wait(1000)
        
        if self.wall_check(int(self.x), int(self.y + y_change)):
            self.y += y_change
        elif self.finish_check((self.x), (self.y)) == [int(self.x), int(self.y + y_change)]:
            self.game_stop = True
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