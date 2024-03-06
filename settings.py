import pygame as pg
import pygame_gui as pg_gui

pg.freetype.init()

# Player:
PLAYER_START1 = 1.5, 1.5
PLAYER_START2 = 1.5, 4.5
PLAYER_POS = 1.5, 1.5
KEY_COOLDOWN = 0

# Start_up:
RES = WIDTH, HEIGHT = 800, 800

# GUI: 
BUTTON_SIZE = (100, 50)
STAND_BACK_COL = 143, 186, 235, 1
THEME_PATH = 'Json_Files/theme_0.json'
MANAGER = pg_gui.UIManager((RES), 'Json_Files/theme_0.json')
        
        


