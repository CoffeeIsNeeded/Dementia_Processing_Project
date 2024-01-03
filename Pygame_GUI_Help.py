import pygame as pg
import pygame_gui as pg_gui
from settings import *


pg.init()

pg.display.set_caption('Quick Start')
window_surface = pg.display.set_mode((RES))

background = pg.Surface((RES))
background.fill(pg.Color('#000000'))

manager = pg_gui.UIManager((RES))

start_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
                                             text='START',
                                             manager=manager)

settings_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 475), (100, 50)),
                                             text='SETTINGS',
                                             manager=manager)

quit_but = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 675), (100, 50)),
                                             text='QUIT',
                                             manager=manager)


clock = pg.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

        if event.type == pg_gui.UI_BUTTON_PRESSED:
            if event.ui_element == quit_but:
                is_running = False
            if event.ui_element == start_but:
                print("Start")
            if event.ui_element == settings_but:
                print("Settings")
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pg.display.update()