import pygame as pg
import pygame_gui as pg_gui
from textwrap import fill
import time
import sys

from settings import *
from map import *
from player import *

pg.init()
manager = pg_gui.UIManager((RES), (THEME_PATH))

class Main:
    def __init__(self): # Initalised Variables
        self.display = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time_delta = self.clock.tick(60)/1000.0
        self.new_game()
        self.manager = pg_gui.UIManager((RES))
        self.game_start = True
        self.running = True
        
        # ------GUI:------
        # Colours:
        self.normal_bg = "#45494e"
        self.dark_bg = "#15191e"
        self.white = "#FFFFFF"
        
        # Fonts:
        self.title_font = pg.font.Font('Fonts\\times.ttf', 24)
        self.paragraph_font = pg.font.Font('Fonts\\times.ttf', 20)
    
    def record_time(self):
        return time.time()
        
    def new_game(self): # Function: Initialises and runs the classes Map() and Player(), which in turn resets the current instance when intialised again.
        #self.maze_gui = Maze_GUI(self)
        self.map = Map(self)
        self.player = Player(self)
           
    def update_game(self): # Function: Updates the player update() function and the pygame screen.
        self.player.update()
        pg.display.flip()

    def chk_game_events(self): # Function: Checks for any pygame events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def arrows(self): # Function: Contains a 2D array of gui element positions for arrows and passes the singular arrays as an argument to anotherfunction to be displayed.
        arrows = [
            [
                (525, 185, 10, 20), 
                (490, 135, 80, 90), 
                ((515, 185), (530, 155), (545, 185))
            ],
            [
                (525, 280, 10, 20), 
                (490, 260, 80, 90), 
                ((515, 300), (530, 330), (545, 300))
            ],
            [
                (505, 425, 20, 10), 
                (490, 385, 80, 90), 
                ((555, 430), (525, 445), (525, 415))
            ],
            [
                (535, 535, 20, 10), 
                (490, 495, 80, 90), 
                ((505, 540), (535, 555), (535, 525))
            ]
        ]
        for direction in arrows:
            self.draw_arrow(direction)
            
    def draw_arrow(self, direction): # Draws the gui arrows on the screen.
        arrow_line = direction[0]
        arrow_box = direction[1]
        arrow_triangle = direction[2]

        pg.draw.polygon(self.display, self.white, (arrow_triangle))
        pg.draw.rect(self.display, self.white, arrow_line, 10)
        pg.draw.rect(self.display, self.white, arrow_box, 5)

    def draw_text(self): # Function; Draws text on-screen and paragrahs the text.
        paragraphs = [
            ["Press the UP ARROW",  "button on the",  "keyboard to move 1", "space up"],
            ["Press the DOWN",  "ARROW button on the",  "keyboard to move 1", "space down"],
            ["Press the RIGHT",  "ARROW button on the",  "keyboard to move 1", "space right"],
            ["Press the LEFT",  "ARROW button on the",  "keyboard to move 1", "space left"]
            ]

        n = 0
        i = -45
        for paragraph in paragraphs:
            i += 45
            for text in paragraph:
                n += 20
                self.display.blit(self.paragraph_font.render(text, True, self.white), (600, 115 + n + i))
        self.display.blit(self.title_font.render('Keyboard Buttons', True, self.white), (540, 50))

    def draw_game(self): # Function: draws screen background, player and map from thier respective sources.
        self.display.fill(STAND_BACK_COL)
        self.player.draw()
        self.map.draw()
        
        # Background:
        values0 = (450, 0, 350, 800)
        values1 = (0, 0, 450, 230)
        values2 = (0, 605, 450, 195)
        values3 = (0, 205, 450, 400)
        
        pg.draw.rect(self.display, self.normal_bg, values0, 350)
        pg.draw.rect(self.display, self.dark_bg, values0, 10)
        pg.draw.rect(self.display, self.normal_bg, values1, 450)
        pg.draw.rect(self.display, self.normal_bg, values2, 450)
        pg.draw.rect(self.display, self.dark_bg, values3, 25)
        self.arrows()
        self.draw_text()
    
    def run(self): # Function: Runs the maze and records the time taken to complete the maze after a completion as self.time_taken
        time_start = self.record_time()
        self.running = True
        while self.running == True:
            self.chk_game_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(60)
            if self.player.game_stop == True:
                time_end = self.record_time()
                self.time_taken = (time_end - time_start)
                self.running = False