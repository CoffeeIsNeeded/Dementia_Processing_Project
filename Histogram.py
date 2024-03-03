import matplotlib.pyplot as plt
import numpy as np
import sys

import pygame as pg
import pygame_gui as pg_gui

import Database
from settings import *

pg.init()
pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES), THEME_PATH)
manager.get_theme().load_theme(THEME_PATH)

connection = Database.connect()
Database.create_tables(connection)

class Graph:
    def __init__(self):
        self.age = []
        self.time = []
        self.graph_window = pg_gui.elements.UIWindow(pg.Rect((10, 10), (790, 400)), manager)
        self.window = pg_gui.elements.UIWindow(pg.Rect((10, 400), (790, 400)), manager)
        self.start_but = pg_gui.elements.UIButton(pg.Rect((250, 250), BUTTON_SIZE), 'START', manager, self.window)
        self.quit_but = pg_gui.elements.UIButton(pg.Rect((450, 250), BUTTON_SIZE), 'QUIT', manager, self.window)

    def time_age(self, username, password):
        users = Database.get_all_age_y_time(connection)
        logged_user = Database.get_user(connection, username, password)
        user_avg_time = logged_user[7]
        user_age = logged_user[3]
        
        for user in users:
            self.age.append(user[0])
            self.time.append(user[1])
            
        time_quartile = np.quantile(self.time, [0, 0.25, 0.5, 0.75, 1])
        age_quartile = np.quantile(self.age, [0, 0.25, 0.5, 0.75, 1])
        if time_quartile[0] <= user_avg_time < time_quartile[1]:
            print("User time quartile 1")
        if time_quartile[1] <= user_avg_time < time_quartile[2]:
            print("User time quartile 2")
        if time_quartile[2] <= user_avg_time < time_quartile[3]:
            print("User time quartile 3")
        if time_quartile[3] <= user_avg_time <= time_quartile[4]:
            print("User time quartile 4")

        if age_quartile[0] <= user_age < age_quartile[1]:
            print("User age quartile 1")
        if age_quartile[1] <= user_age < age_quartile[2]:
            print("User age quartile 2")
        if age_quartile[2] <= user_age < age_quartile[3]:
            print("User age quartile 3")
        if age_quartile[3] <= user_age <= age_quartile[4]:
            print("User age quartile 4")

    def plot(self):
        plt.bar(self.age, self.time)
        plt.savefig('age_time.png')
   
    def but_pressed(self, but):
        if but == self.start_but:
            self.run()
        if but == self.quit_but:
            pg.quit()
            sys.exit()

    def run(self):
        self.time_age()
        self.plot()
    
but = Graph()

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
