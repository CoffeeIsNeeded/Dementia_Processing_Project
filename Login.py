from settings import *
import pygame as pg
import pygame_gui as pg_gui
import Database
import Histogram
from Histogram import *
from Main import *

pg.init()
pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))

background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES), THEME_PATH)

clock = pg.time.Clock()
running = True

connection = Database.connect()

class Login:
    def __init__(self, connection):
        # Database Variables:
        self.connection = connection
        self.username = ""
        self.password = ""
        self.age = 0
        self.DB_username = []
        self.DB_password = []
        users = Database.get_all_users(connection)
        for user in users:
            self.DB_username.append(user[1])
            self.DB_password.append(user[2])
        # Maze game variables:
        self.game_start = True
        self.graph_start = False
        self.count = 3
        self.time_array = []
        
        # --------- GUI: ---------
        # Text Entry:
        self.reg_username_entry = pg_gui.elements.UITextEntryLine(pg.Rect((475, 275), BUTTON_SIZE), manager)
        self.reg_password_entry = pg_gui.elements.UITextEntryLine(pg.Rect((475, 325), BUTTON_SIZE), manager)
        self.reg_age_entry = pg_gui.elements.UITextEntryLine(pg.Rect((475, 375), BUTTON_SIZE), manager) 
        self.log_username_entry = pg_gui.elements.UITextEntryLine(pg.Rect((225, 275), BUTTON_SIZE), manager)
        self.log_password_entry = pg_gui.elements.UITextEntryLine(pg.Rect((225, 325), BUTTON_SIZE), manager)
        self.log_age_entry = pg_gui.elements.UITextEntryLine(pg.Rect((225, 375), BUTTON_SIZE), manager)
        
        # Text Labels
        self.log_Label = pg_gui.elements.UILabel(pg.Rect((475, 200), BUTTON_SIZE), "Login", manager)
        self.reg_Label = pg_gui.elements.UILabel(pg.Rect((225, 200), BUTTON_SIZE), "Register", manager)
        
        # Buttons:
        self.reg_but = pg_gui.elements.UIButton(pg.Rect((225, 475), BUTTON_SIZE), 'REGISTER', manager)
        self.log_but = pg_gui.elements.UIButton(pg.Rect((475, 475), BUTTON_SIZE), 'LOGIN', manager)
        self.back_but = pg_gui.elements.UIButton(pg.Rect((350, 675), BUTTON_SIZE), 'BACK', manager)
        
    def chk_text_entry(self, process, event):
        if process == self.reg_username_entry or process == self.log_username_entry:
            self.username = event.text
        if process == self.reg_password_entry or process == self.log_password_entry:
            self.password = event.text
        if process == self.reg_age_entry or process == self.log_age_entry:
            self.age = event.text
            
    def but(self, process):
        if process == self.reg_but:
            if self.username not in self.DB_username:
                self.game_start = True
                self.reg(connection)
                while self.game_start:
                    self.game_loop()
                while self.graph_start:
                    self.run_graph()
        if process == self.log_but:
            n = 0
            self.game_start = False
            for name in self.DB_username:
                n += 1
                if self.username == name and self.password == self.DB_password[n]:
                    self.game_start = True
            while self.game_start:
                self.game_loop()
            while self.graph_start:
                self.run_graph()          
        if process == self.back_but:
            return False
        
    def game_loop(self):
        if self.count != 0:
            main = Main()
            main.run()
            time = main.time_taken
            self.time_array.append(time)
            self.count -= 1
            print(self.time_array)
        elif self.count == 0:
            self.game_start = False
            self.graph_start = True

    def run_graph(self):
        t_avg = 0
        for time in self.time_array:
            t_avg += time
        Database.get_times_from_user(self.connection, self.time_array[0], self.time_array[1], self.time_array[2], t_avg, self.username, self.password)
        graph = Graph()
        graph.time_age(self.username, self.password)
        Histogram.menu()

    def reg(self, connection):
        null = 0
        Database.add_user(self.connection, self.username, self.password, self.age, null, null, null, null, null)

    def ent_cred(self):
        pass

    def chk_cred(self):
        pass
    
process = Login(connection)

def menu():
    clock = pg.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        manager.get_theme().load_theme(THEME_PATH)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg_gui.UI_TEXT_ENTRY_CHANGED:
                process.chk_text_entry(event.ui_element, event)
            if event.type == pg_gui.UI_BUTTON_PRESSED:
                process.but(event.ui_element)
                if process.but(event.ui_element) == False:
                    running = False
            
            manager.process_events(event)

        manager.update(time_delta)

        display.blit(background, (0, 0))
        manager.draw_ui(display)

        pg.display.update()