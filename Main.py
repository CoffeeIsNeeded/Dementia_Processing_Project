import pygame as pg
import pygame_gui as pg_gui
import time
import sys

from settings import *
from map import *
from player import *
from maze_gui import *

pg.init()
manager = pg_gui.UIManager((RES), (THEME_PATH))

class Main:
    def __init__(self): # Initalised Variables
        self.display = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time_delta = self.clock.tick(60)/1000.0
        self.new_game()
        self.manager = pg_gui.UIManager((RES))
        self.game_start = True
        self.running = True
        self.time_taken = 0
    
    def record_time(self):
        return time.time()
        
    def new_game(self): # Function: Initialises and runs the classes Map() and Player(), which in turn resets the current instance when intialised again.
        self.maze_gui = Maze_GUI(self)
        self.map = Map(self)
        self.player = Player(self)
           
    def update_game(self): # Function: Updates the player update() function and the pygame screen.
        self.player.update()
        pg.display.flip()

    def chk_game_events(self): # Function: Checks for any pygame events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
    def draw_game(self): # Function: draws screen background, player and map from thier respective sources.
        self.display.fill(STAND_BACK_COL)
        self.maze_gui.draw()
        self.player.draw()
        self.map.draw()
    
    def run(self): # Function: Runs the maze and records the time taken to complete the maze after a completion as self.time_taken
        time_start = self.record_time()
        self.running = True
        while self.running == True:
            self.chk_game_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)
            if self.player.game_stop == True:
                time_end = self.record_time()
                self.time_taken = (time_end - time_start)
                self.running = False

if __name__ == "__main__":
    main = Main()
    main.run()