import pygame as pg
import pygame_gui as pg_gui
from settings import *
import settings_GUI
from Main import *

pg.init()

pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))

background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES))

clock = pg.time.Clock()
running = True

class Menu_But:
    def __init__(self) -> None:
        self.start_but = pg_gui.elements.UIButton(pg.Rect((350, 275), BUTTON_SIZE), 'START', manager)
        self.settings_but = pg_gui.elements.UIButton(pg.Rect((350, 475), BUTTON_SIZE), 'SETTINGS', manager)
        self.quit_but = pg_gui.elements.UIButton(pg.Rect((350, 675), BUTTON_SIZE), 'QUIT', manager)
        
    def but_pressed(self, but):
        if but == self.start_but:
            main = Main()
            main.run()
        if but == self.settings_but:
            self.settingsdone = settings_GUI.menu()
        if but == self.quit_but:
            pg.quit()
            sys.quit()
            
but = Menu_But()

while running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg_gui.UI_BUTTON_PRESSED:
            but.but_pressed(event.ui_element)
        manager.process_events(event)

    manager.update(time_delta)

    display.blit(background, (0, 0))
    manager.draw_ui(display)

    pg.display.update()