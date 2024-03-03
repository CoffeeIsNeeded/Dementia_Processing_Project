import pygame as pg
import pygame_gui as pg_gui
import time
import sys

from settings import *
from map import *
from player import *

pg.init()

class Main:
    def __init__(self):
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
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
           
    def update_game(self):
        self.player.update()
        pg.display.flip()

    def chk_game_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
        
    def draw_game(self):
        self.display.fill(STAND_BACK_COL)
        self.player.draw()
        self.map.draw()
    
    def run(self):
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
                
            
if __name__ == '__main__':
    main = Main()
    main.run()

