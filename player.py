import pygame as pg
import time

from settings import *

class Player:
    def __init__(self, main): # Initalising variables
        self.main = main
        self.x, self.y = PLAYER_POS
        self.game_stop = False
        self.time_end = (self.return_time() + 10)
        
    def return_time(self): # Function: returns time at current point.
        return time.time()
    
    def movement(self): # Function: Adds or subtracts an integer value of one when the given key is pressed then is passed as arguments to be checked and updated to the position in wall_collision()
        time = self.return_time()
        if time > self.time_end:
            x_change, y_change = 0, 0
        
            key = pg.key.get_pressed()
            if key[pg.K_UP]:
                y_change -= 1
                pg.time.wait(250)
            if key[pg.K_DOWN]:
                y_change += 1
                pg.time.wait(250)
            if key[pg.K_LEFT]:
                x_change -= 1
                pg.time.wait(250)
            if key[pg.K_RIGHT]:
                x_change += 1
                pg.time.wait(250)

            self.wall_collision(x_change, y_change)

    def finish_check(self, x, y): # Returns the finsh square coordinates from the final map.
        x, y = self.main.map.finish_square
        return [x, y]
    
    def wall_check(self, x, y): # Returns coordintes not in the final map.
        return (x, y) not in self.main.map.mapfinal
    
    def wall_collision(self, x_change, y_change): # Function: Adds the movement values to x and y, checks if player has hit the finish, checks if a player has hit the wall and updates the x and y values accordingly.
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

    def update(self): # Function: updates movement on-screen.
        self.movement()
    
    def draw(self): # Function: Draws the player as a pygame circle.
        pg.draw.circle(self.main.display, (121, 52, 158, 1), (25 + (self.x * 50), 230 + (self.y * 50)), 19)
        pg.draw.circle(self.main.display, (196, 87, 255, 1), (25 + (self.x * 50), 230 + (self.y * 50)), 13)
    
    @property
    def pos(self): # Function: returns x and y as a argument with pos()
        return self.x, self.y
    
    @property
    def map_pos(self): # Function: returns x and y as a intger argument with map_pos()
        return int(self.x), int(self.y)