import pygame as pg
from settings import *
import random
import time

# All 4 2D arrays indicating the layout of the map:
_ = None # Acting as a null value.
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
    def __init__(self, main): # Initialising variables
        self.main = main
        self.maplayout = maplayout
        self.mapfinal = {}
        self.mapfinalgrid = {}
        self.mapfinalend = {}
        self.finish_square = []
        self.get_map()
        self.x, self.y = PLAYER_POS
        self.time_end = (self.return_time() + 10)
        
    def get_map(self): # Function: randomly selects an integer which will choose a randmly selected maplayout as well as the finish square for the map.
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
            
        for j, row in enumerate(self.maplayout): # Appends to a dictionary the coordinates of the walls of the maze with the wall value.
            for i, value in enumerate(row):
                if value is not None:
                    self.mapfinal[(i, j)] = value
                    if value == 2:
                        self.mapfinalend[(i, j)] = value
                value2 = 4
                self.mapfinalgrid[(i, j)] = value2
        
    def return_time(self): # Function: returns current time.
        return time.time()
    
    def draw_start_end(self): # Function: draws end and start of map as coloured boxes.
        for pos, value in self.mapfinalend.items(): 
            match value:
                case 2:
                    colour = (0, 255, 0, 1)
            wall_pos = (25 + (pos[0] * 50), 230 + (pos[1] * 50), 50, 50)
            pg.draw.rect(self.main.display, colour, wall_pos, 50)

    def draw_grid(self): # Function: draws map as a coloured grid.
        for pos, value in self.mapfinalgrid.items(): 
            match value:
                case 4:
                    colour = (255, 255, 255, 1)
            wall_pos = (25 + (pos[0] * 50), 230 + (pos[1] * 50), 50, 50)
            pg.draw.rect(self.main.display, colour, wall_pos, 5)

    def draw(self): # Draws all elements of the map.
        self.draw_grid()
        for pos, value in self.mapfinal.items(): # For every position in self.mapfinal.items() a coloured box is drawn.
            match value: # Allows different boxes to be different colours.
                case 1:
                    colour = (72, 102, 120, 1)
                case 2:
                    colour = (0, 255, 0, 1)
            wall_pos = (25 + (pos[0] * 50), 230 + (pos[1] * 50), 50, 50)
            
            time = self.return_time()
            if time > self.time_end: # draws the map normally up until this point, here the map grid, start and end are finally able to be seen.
                colour = (STAND_BACK_COL)
                self.draw_grid()
                self.draw_start_end()
            pg.draw.rect(self.main.display, colour, wall_pos, 50)
