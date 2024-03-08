import pygame as pg
from settings import *
import random
import time

class Maze_GUI:
    def __init__(self, main): # Initialising variables
        self.main = main

    def draw(self): # Draws the elements of the map.
        normal_bg = pg.Color("#45494e")
        values = (350, 0, 450, 800)
        pg.draw.rect(self.main.display, normal_bg, values, 100)
