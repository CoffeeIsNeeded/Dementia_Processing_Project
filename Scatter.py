import matplotlib.pyplot as plt
import numpy as np
import sys

import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.core import ObjectID

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
        self.username = ""
        self.password = ""
        self.text = ""
        self.age = []
        self.time = []
        
        # ------GUI:------
        self.graph_panel = pg_gui.elements.UIPanel(
            pg.Rect((10, 10), (790, 380)), 
            1, 
            manager,
            object_id = ObjectID(
                class_id = '@Scatter Panels', 
                object_id = '#graph_panel'
                )
            )
        self.panel = pg_gui.elements.UIPanel(
            pg.Rect((10, 400), (790, 380)), 
            1, 
            manager,
            object_id = ObjectID(
                class_id = '@Scatter Panels', 
                object_id = '#panel'
                )
            )
        
        # Buttons:
        self.start_but = pg_gui.elements.UIButton(
            pg.Rect((250, 250), BUTTON_SIZE), 
            'START', 
            manager, 
            self.panel
            )
        self.quit_but = pg_gui.elements.UIButton(
            pg.Rect((450, 250), BUTTON_SIZE), 
            'QUIT', 
            manager, 
            self.panel
            )
        self.image_but = pg_gui.elements.UIButton(
            pg.Rect((0, 0), (790, 380)), 
            '', 
            manager, 
            self.graph_panel,
            object_id = ObjectID(
                object_id = '#image_but'
                )
            )
        
        # Labels:
        self.age_time_label = pg_gui.elements.UILabel(
            pg.Rect((350, 100), (100, 50)), 
            self.text, 
            manager, 
            self.panel,
            object_id = ObjectID(
                class_id = '@Scatter Labels', 
                object_id = '#age_time_label'
                )
            )

    def time_age(self):
        users = Database.get_all_age_y_time(connection)
        logged_user = Database.get_user(connection, self.username, self.password)
        user_avg_time = logged_user[0][7]
        user_age = logged_user[0][3]
        
        for user in users:
            self.age.append(user[0])
            self.time.append(user[1])
            
        age_quantiles = np.quantile(self.age, [0, 0.25, 0.5, 0.75, 1])
        time_quantiles = np.quantile(self.time, [0, 0.25, 0.5, 0.75, 1])
        
        if time_quantiles[0] <= user_avg_time < time_quantiles[1]:
            self.text = "Very Low Risk, High Processing Speed"
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        elif time_quantiles[1] <= user_avg_time < time_quantiles[2]:
            self.text = "Low Risk, Normal Processing Speed"
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        elif time_quantiles[2] <= user_avg_time < time_quantiles[3]:
            self.text = "Slow Processing Speed, "
            if age_quantiles[2] <= user_age <= age_quantiles[4]:
                self.text = self.text + "Average Risk"
            else:
                self.text = self.text + "Low Risk"
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        elif time_quantiles[3] <= user_avg_time < time_quantiles[4]:
            self.text = "Very Slow Processing Speed, "
            if age_quantiles[2] <= user_age <= age_quantiles[4]:
                self.text = self.text + "High Risk"
            else:
                self.text = self.text + "Low Risk"
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        

    def plot(self):
        name ='age_time'
        plt.scatter(self.age, self.time)
        scatter = plt.gcf()
        scatter.set_size_inches(4, 3)
        plt.savefig(('Images/{}'.format(name)), dpi = 100)
        plt.close()
   
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

def menu(username, password):
    but.username = username
    but.password = password
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