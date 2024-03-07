import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.core import ObjectID
from settings import *
from Main import *
import Login_and_Register

pg.init()
pg.display.set_caption('Memory Processing Tool')
display = pg.display.set_mode((RES))
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = MANAGER

class Menu_But:
    def __init__(self):
        self.start_but = pg_gui.elements.UIButton(
            pg.Rect((350, 375), BUTTON_SIZE), 
            'START', manager, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Buttons', 
                object_id = '#start_Button'
                )
            )
        self.quit_but = pg_gui.elements.UIButton(
            pg.Rect((350, 575), BUTTON_SIZE), 
            'QUIT', 
            manager, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Buttons', 
                object_id = '#quit_Button'
                )
            )
        
    def but_pressed(self, but):
        if but == self.start_but:
            Login_and_Register.menu()
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
            manager.process_events(event)

        manager.update(time_delta)
        manager.get_theme().load_theme(THEME_PATH)
        display.blit(background, (0, 0))
        manager.draw_ui(display)

        pg.display.update()
        
menu()
