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
CB = pg_gui.UIManager((RES), 'Json_Files/theme_0.json')

# Pygame_GUI Managers
def set_theme(Value):
    if Value == 0: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_0.json')
    if Value == 1: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_1.json')
    if Value == 2: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_2.json')
    if Value == 3: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_3.json')
    if Value == 4: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_4.json')
    if Value == 5: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_5.json')
    if Value == 6: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_6.json')
    if Value == 7: 
        CB = pg_gui.UIManager((RES), 'Json_Files/theme_7.json')
        
        


