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
        self.connection = connection
        self.username = ""
        self.password = ""
        self.age = 0
        self.DB_username = ""
        self.DB_password = ""

        self.game_start = True
        self.graph_start = False
        self.count = 3
        self.value = 1
        self.time_array = []
        
        self.username_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 275), BUTTON_SIZE), manager)
        self.password_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 325), BUTTON_SIZE), manager)
        self.age_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 375), BUTTON_SIZE), manager)
        self.reg_but = pg_gui.elements.UIButton(pg.Rect((450, 675), BUTTON_SIZE), 'REGISTER', manager)
        self.back_but = pg_gui.elements.UIButton(pg.Rect((250, 675), BUTTON_SIZE), 'BACK', manager)
        
    def chk_text_entry(self, process, event):
        if process == self.username_entry:
            self.username = event.text
        if process == self.password_entry:
            self.password = event.text
        if process == self.age_entry:
            self.age = event.text
            
    def but(self, process):
        if process == self.reg_but:
            self.reg(connection)
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
        graph.username = self.username
        graph.password = self.password
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