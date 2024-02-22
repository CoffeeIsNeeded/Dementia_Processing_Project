import pygame as pg
import pygame_gui as pg_gui
from settings import *
from Main import *
import Login

pg.init()
pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES), THEME_PATH)
manager.get_theme().load_theme(THEME_PATH)

class Menu_But:
    def __init__(self):
        self.start_but = pg_gui.elements.UIButton(pg.Rect((350, 275), BUTTON_SIZE), 'START', manager)
        self.back_but = pg_gui.elements.UIButton(pg.Rect((350, 475), BUTTON_SIZE), 'BACK', manager)
        self.quit_but = pg_gui.elements.UIButton(pg.Rect((350, 675), BUTTON_SIZE), 'QUIT', manager)
        
    def but_pressed(self, but):
        if but == self.start_but:
            Login.menu()
        if but == self.back_but:
            return False
        if but == self.quit_but:
            pg.quit()
            sys.exit()
            
but = Menu_But()

def menu():
    clock = pg.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg_gui.UI_BUTTON_PRESSED:
                but.but_pressed(event.ui_element)
                if but.but_pressed(event.ui_element) == False:
                    running = False
            manager.process_events(event)

        manager.update(time_delta)
        manager.get_theme().load_theme(THEME_PATH)
        display.blit(background, (0, 0))
        manager.draw_ui(display)

        pg.display.update()
