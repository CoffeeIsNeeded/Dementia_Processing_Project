import pygame as pg
import pygame_gui as pg_gui
from settings import *
import Main_Menu_GUI
import sys

display = pg.display.set_mode((RES))

pg.init()
pg.freetype.init()
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES), THEME_PATH)

class Settings_But:
    def __init__(self) -> None:
        self.theme = THEME_PATH
        self.continue_but = pg_gui.elements.UIButton(pg.Rect((350, 275), BUTTON_SIZE), 'CONTINUE', manager)
        self.colblind_dropdown = pg_gui.elements.UIDropDownMenu(['Colour Blind 0', 'Colour Blind 1', 'Colour Blind 2', 'Colour Blind 3', 'Colour Blind 4', 'Colour Blind 5'], 'Colour Blind 0', pg.Rect((100, 100), (200, 30)), manager)

    def but_pressed(self, but):
        if but == self.continue_but:
            Main_Menu_GUI.menu()
            
    def drop_used(self, used, pre_event):
        event = pre_event
        if used == self.colblind_dropdown:
            if event.text == 'Colour Blind 0':
                self.theme = 0
            if event.text == 'Colour Blind 1':
                self.theme = 1
            if event.text == 'Colour Blind 2':
                self.theme = 2
            if event.text == 'Colour Blind 3':
                self.theme = 3
            if event.text == 'Colour Blind 4':
                self.theme = 4
            if event.text == 'Colour Blind 5':
                self.theme = 5

    def theme_chk(self):
        return self.theme
        

element = Settings_But()

clock = pg.time.Clock()
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg_gui.UI_BUTTON_PRESSED:
            element.but_pressed(event.ui_element)
            if element.but_pressed(event.ui_element) == False:
                running = False
        if event.type == pg_gui.UI_DROP_DOWN_MENU_CHANGED:
            element.drop_used(event.ui_element, event)    
            
        manager.process_events(event)

    manager.update(time_delta)

    display.blit(background, (0, 0))
    manager.draw_ui(display)

    pg.display.update()
    theme = element.theme_chk()
    set_theme(theme)



