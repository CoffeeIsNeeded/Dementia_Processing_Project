import pygame as pg
import sys

from settings import *
from map import *
from player import *

class Main:
    def __init__(self):
        self.display = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
 
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
           
    def update(self):
        self.player.update()
        pg.display.flip()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def draw(self):
        self.display.fill((143, 186, 235, 1))
        self.player.draw()
        self.map.draw()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(60)
            
if __name__ == '__main__':
    main = Main()
    main.run()