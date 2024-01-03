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

    #def update_menu(self):
        #self.manager.update(self.time_delta)
        #pg.display.flip()

    def chk_game_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #def chk_events_menu(self):
        #for event in pg.event.get():
            #if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                #pg.quit()
                #sys.exit()
                
            #if event.type == pg_gui.UI_BUTTON_PRESSED:
                #self.game_start = False
            #self.manager.process_events(event)

    #def draw_menu(self):
        #self.display.fill((143, 186, 235, 1))
        #self.start_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), BUTTON_SIZE), text='START', manager=self.manager)
        #self.settings_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 475), BUTTON_SIZE), text='SETTINGS', manager=self.manager)
        #self.quit_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 675), BUTTON_SIZE), text='QUIT', manager=self.manager)
        #self.manager.draw_ui(self.display)
        
    def draw_game(self):
        self.display.fill((143, 186, 235, 1))
        self.player.draw()
        self.map.draw()
    
    def run(self):
        while self.running == True:
            #self.chk_events_menu()
            #self.update_menu()
            #self.draw_menu()
            #if self.game_start == False:
                #while self.running == True:
            self.chk_game_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)
            
if __name__ == '__main__':
    main = Main()
    main.run()

