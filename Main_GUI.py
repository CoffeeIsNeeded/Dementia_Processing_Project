import pygame as pg
import pygame_gui as pg_gui
from settings import *
from Main import *

pg.init()

pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))

background = pg.Surface((RES))
display.fill((143, 186, 235, 1))

manager = pg_gui.UIManager((RES))

start_but = pg_gui.elements.UIButton(pg.Rect((350, 275), BUTTON_SIZE), 'START', manager)
settings_but = pg_gui.elements.UIButton(pg.Rect((350, 475), BUTTON_SIZE), 'SETTINGS', manager)
quit_but = pg_gui.elements.UIButton(pg.Rect((350, 675), BUTTON_SIZE), 'QUIT', manager)

clock = pg.time.Clock()
running = True

while running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

        if event.type == pg_gui.UI_BUTTON_PRESSED:
            if event.ui_element == quit_but:
                pg.quit()
                sys.exit()
            if event.ui_element == start_but:
                main = Main()
                main.run()
            if event.ui_element == settings_but:
                print("Settings")
        manager.process_events(event)

    manager.update(time_delta)

    display.blit(background, (0, 0))
    manager.draw_ui(display)

    pg.display.update()