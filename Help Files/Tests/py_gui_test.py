import pygame as pg
import pygame_gui as pg_g


pg.init()

pg.display.set_caption('Quick Start')
window_surface = pg.display.set_mode((800, 600))

background = pg.Surface((800, 600))
background.fill(pg.Color('#000000'))

manager = pg_g.UIManager((800, 600))

clock = pg.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pg.display.update()