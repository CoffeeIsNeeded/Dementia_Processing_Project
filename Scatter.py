import matplotlib.pyplot as plt
import numpy as np
import sys

import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.core import ObjectID

import Database
from settings import *

pg.init()
pg.display.set_caption('Memory Processing Tool')
display = pg.display.set_mode((RES))
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES), THEME_PATH)
manager.get_theme().load_theme(THEME_PATH)

connection = Database.connect() # Connects to the database.
Database.create_tables(connection) # Creates database tables if not already created.

class Graph:
    def __init__(self): # Initalising Variables
        self.username = ""
        self.password = ""
        self.text = ""
        self.results_output = 0
        self.age = []
        self.time = []
        
        # ------GUI:------
        # Panels: 
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
            pg.Rect((250, 70), BUTTON_SIZE), 
            'START', 
            manager, 
            self.panel
            )
        self.quit_but = pg_gui.elements.UIButton(
            pg.Rect((430, 70), BUTTON_SIZE), 
            'QUIT', 
            manager, 
            self.panel
            )
        self.quit_but.hide()
        self.image_but = pg_gui.elements.UIButton(
            pg.Rect((0, 0), (790, 380)), 
            '', 
            manager, 
            self.graph_panel,
            object_id = ObjectID(
                object_id = '#image_but'
                )
            )
        
        # Text Boxes:
        self.scatter_text_box = pg_gui.elements.UITextBox(
            TEXT_ARRAY[4], 
            pg.Rect((10, 140), (760, 220)), 
            manager, 
            starting_height = 1, 
            container = self.panel, 
            object_id = ObjectID(
                class_id = '@Scatter_Text_Boxes', 
                object_id = '#scatter_text_box'
                )
            )

        # Labels:
        self.age_time_label = pg_gui.elements.UILabel(
            pg.Rect((220, 30), (340, 25)), 
            self.text, 
            manager, 
            self.panel,
            object_id = ObjectID(
                class_id = '@Scatter Labels', 
                object_id = '#age_time_label'
                )
            )

    def time_age(self):
        users = Database.get_all_age_y_time(connection) # Getting all user age and average time values from Database
        # Getting current user average time and age values:
        logged_user = Database.get_user(connection, self.username, self.password) 
        user_avg_time = logged_user[0][7]
        user_age = logged_user[0][3]
        # Appending all times and ages to two arrays as values to be plotted on the scatter graph:
        for user in users:
            self.age.append(user[0])
            self.time.append(user[1])
        # Working out quartile values for the time and age arrays for all users:  
        age_quantiles = np.quantile(self.age, [0, 0.25, 0.5, 0.75, 1])
        time_quantiles = np.quantile(self.time, [0, 0.25, 0.5, 0.75, 1])
        # Working out where the current users results are in comparision with the quartiles and judging the users time and age values according to that:
        if time_quantiles[0] <= user_avg_time < time_quantiles[1]:
            self.text = "Very Low Risk, High Processing Speed"
            self.results_output = 0
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text) # The label is changed for the user to read depending on thier results.
        if time_quantiles[1] <= user_avg_time < time_quantiles[2]:
            self.text = "Low Risk, Average Processing Speed"
            self.results_output = 1
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        if time_quantiles[2] <= user_avg_time < time_quantiles[3]:
            self.text = "Slow Processing Speed, "
            if age_quantiles[2] <= user_age <= age_quantiles[4]:
                self.text = self.text + "Average Risk"
                self.results_output = 2
            else:
                self.text = self.text + "Low Risk"
                self.results_output = 3
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        if time_quantiles[3] <= user_avg_time < time_quantiles[4]:
            self.text = "Very Slow Processing Speed, "
            if age_quantiles[2] <= user_age <= age_quantiles[4]:
                self.text = self.text + "High Risk"
                self.results_output = 4
            else:
                self.text = self.text + "Above Average Risk"
                self.results_output = 5
            pg_gui.elements.UILabel.set_text(self.age_time_label, self.text)
        

    def plot(self): # Function: Plots the scatter graph, gives it axis and saves it as an image.
        name ='age_time'
        plt.scatter(self.age, self.time)
        plt.xlabel("Age /years")
        plt.ylabel("Average Time /s")
        scatter = plt.gcf()
        scatter.set_size_inches(7.5, 3.5)
        plt.savefig(('Images/{}'.format(name)), dpi = 100)
        plt.close()
   
    def but_pressed(self, but): # Function: Checks if a specific button has been pressed and does the following action if one has.
        if but == self.start_but:
            self.run() # Runs the function run() which will plot and save a graph as well as giving the user a prompt on-screen depending on thier performance.
            print(self.results_output)
            self.scatter_text_box.append_html_text(TEXT_ARRAY[5])
            self.scatter_text_box.append_html_text(RESULTS_TEXT_ARRAY[self.results_output])
            self.start_but.hide()
            self.quit_but.show()
        if but == self.quit_but:
            pg.quit()
            sys.exit()

    def run(self): # Function: Runs the functions time_age() and plot() when active.
        self.time_age()
        self.plot()
    
but = Graph()

def menu(username, password): # Function: Runs the pygame loop and the pygame_gui UI elements for this specific file, as well as passing the username and password to the function time_age().
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