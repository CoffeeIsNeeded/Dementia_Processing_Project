import pygame as pg
import pygame_gui as pg_gui
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
        self.display.fill((143, 186, 235, 1))
        self.player.draw()
        self.map.draw()
    
    def run(self):
        while self.running == True:
            self.chk_game_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)
            
if __name__ == '__main__':
    main = Main()
    main.run()

