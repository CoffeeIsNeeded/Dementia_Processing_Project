from settings import *
import pygame as pg
import pygame_gui as pg_gui
import Database
from Main import *

pg.init()
pg.display.set_caption('Dementia Project')
display = pg.display.set_mode((RES))

background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = pg_gui.UIManager((RES))

clock = pg.time.Clock()
running = True

connection = Database.connect()

class Login:
    def __init__(self, connection):
        self.username = ""
        self.password = ""
        self.age = 0
        self.DB_username = ""
        self.DB_password = ""
        self.connection = connection
        self.username_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 275), BUTTON_SIZE), manager)
        self.password_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 325), BUTTON_SIZE), manager)
        self.age_entry = pg_gui.elements.UITextEntryLine(pg.Rect((350, 375), BUTTON_SIZE), manager)
        self.reg_but = pg_gui.elements.UIButton(pg.Rect((350, 675), BUTTON_SIZE), 'REGISTER', manager)
        
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
            print("Registration complete")
            main = Main()
            main.run()
            
    
    def reg(self, connection):
        null = 0
        Database.add_user(self.connection, self.username, self.password, self.age, null, null, null, null, null)

    def ent_cred(self):
        pass

    def chk_cred(self):
        pass

    def draw(self):
        pass
    
process = Login(connection)
def menu():
    clock = pg.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg_gui.UI_TEXT_ENTRY_CHANGED:
                process.chk_text_entry(event.ui_element, event)
            if event.type == pg_gui.UI_BUTTON_PRESSED:
                process.but(event.ui_element) 
            
            manager.process_events(event)

        manager.update(time_delta)

        display.blit(background, (0, 0))
        manager.draw_ui(display)

        pg.display.update()