from settings import *
import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.core import ObjectID
import Database
from Scatter import menu as Scatter_Menu
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
    def __init__(self, connection): # Initalising Variables
        # Database Variables:
        self.connection = connection
        self.username = ""
        self.password = ""
        self.log_username = ""
        self.log_password = ""
        self.reg_username = ""
        self.reg_password = ""
        self.age = 0
        self.DB_username = []
        self.DB_password = []
        users = Database.get_all_users(connection)
        for user in users:
            self.DB_username.append(user[1])
            self.DB_password.append(user[2])
        # Login and Register Variables:
        self.reg_disabled = False
        self.log_disabled = False
        # Maze game variables:
        self.game_start = True
        self.graph_start = False
        self.count = 3
        self.time_array = []
        
        # --------- GUI: ---------
        # Panels:
        self.reg_panel = pg_gui.elements.UIPanel(
            pg.Rect((10, 10), (780, 780)), 
            1, 
            manager,
            object_id = ObjectID(
                class_id = '@Login_AND_Reg Panels', 
                object_id = '#login_and_reg_panel'
                )
            )
        self.preview_panel = pg_gui.elements.UIPanel(
            pg.Rect((10, 10), (780, 780)), 
            1, 
            manager,
            object_id = ObjectID(
                class_id = '@Login_AND_Reg Panels', 
                object_id = '#preview_panel'
                )
        ) 
        self.preview_panel.hide()

        # Text Entry:
        self.reg_username_entry = pg_gui.elements.UITextEntryLine(
            pg.Rect((465, 275), BUTTON_SIZE), 
            manager, 
            placeholder_text = "Username",
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Register_Text_Entry', 
                object_id = '#reg_username_entry'
                )
            )
        self.reg_password_entry = pg_gui.elements.UITextEntryLine(
            pg.Rect((465, 325), BUTTON_SIZE), 
            manager, 
            placeholder_text = "Password",
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Register_Text_Entry', 
                object_id = '#reg_password_entry'
                )
            )
        self.reg_age_entry = pg_gui.elements.UITextEntryLine(
            pg.Rect((465, 375), BUTTON_SIZE), 
            manager, 
            placeholder_text = "Age",
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Register_Text_Entry', 
                object_id = '#reg_age_entry'
                )
            ) 
        self.log_username_entry = pg_gui.elements.UITextEntryLine(
            pg.Rect((215, 300), BUTTON_SIZE), 
            manager, 
            placeholder_text = "Username",
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_Text_Entry', 
                object_id = '#log_username_entry'
                )
            )
        self.log_password_entry = pg_gui.elements.UITextEntryLine(
            pg.Rect((215, 350), BUTTON_SIZE), 
            manager, 
            placeholder_text = "Password",
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_Text_Entry', 
                object_id = '#log_password_entry'
                )
            )
        
        # Text Labels
        self.log_Label = pg_gui.elements.UILabel(
            pg.Rect((190, 200), (150, 50)), 
            "Login", 
            manager,
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_AND_Reg_Labels', 
                object_id = '#log_label'
                )
            )
        self.reg_Label = pg_gui.elements.UILabel(
            pg.Rect((440, 200), (150, 50)), 
            "Register", 
            manager,
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_AND_Reg_Labels', 
                object_id = '#reg_label'
                )
            )
        
        # Text Boxes:
        self.reg_text_box = pg_gui.elements.UITextBox(
            TEXT_ARRAY[2], 
            pg.Rect((580, 275), (190, 300)), 
            manager, 
            starting_height = 1, 
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_AND_Reg_Text_Boxes', 
                object_id = '#reg_guide_text'
                )
        )

        self.log_text_box = pg_gui.elements.UITextBox(
            TEXT_ARRAY[1], 
            pg.Rect((10, 275), (190, 300)), 
            manager, 
            starting_height = 1, 
            container = self.reg_panel, 
            object_id = ObjectID(
                class_id = '@Login_AND_Reg_Text_Boxes', 
                object_id = '#log_guide_text'
                )
        )

        self.preview_text_box = pg_gui.elements.UITextBox(
            TEXT_ARRAY[0], 
            pg.Rect((20, 20), (750, 500)), 
            manager, 
            starting_height = 1, 
            container = self.preview_panel, 
            object_id = ObjectID(
                class_id = '@Login_AND_Reg_Text_Boxes', 
                object_id = '#preview_text'
                )
        )

        # Buttons:
        self.reg_but = pg_gui.elements.UIButton(
            pg.Rect((465, 475), BUTTON_SIZE), 
            'REGISTER', 
            manager,
            container = self.reg_panel
            )
        self.log_but = pg_gui.elements.UIButton(
            pg.Rect((215, 475), BUTTON_SIZE), 
            'LOGIN', 
            manager,
            container = self.reg_panel
            )
        self.back_but = pg_gui.elements.UIButton(
            pg.Rect((340, 675), BUTTON_SIZE), 
            'BACK', 
            manager,
            container = self.reg_panel
            )
        self.preview_but = pg_gui.elements.UIButton(
            pg.Rect((340, 675), BUTTON_SIZE), 
            'CONTINUE', 
            manager,
            container = self.preview_panel
            )
        
    def chk_text_entry(self, process, event): # Function: Checks if text has been entered into the text_entry boxes. 
        # Changes either the username, password or age to the text inputted to the text_entry box.
        if process == self.reg_username_entry: 
            self.reg_username = event.text
        if process == self.reg_password_entry:
            self.reg_password = event.text
        if process == self.log_username_entry: 
            self.log_username = event.text
        if process == self.log_password_entry:
            self.log_password = event.text
        if process == self.reg_age_entry:
            try:
                self.age = int(event.text)
            except:
                self.age = 131
            
    def but(self, process): # Checks if a button is pressed and carries out the appropriate response.
        if process == self.reg_but: # Registers user information to the database if the appropriate conditions are met then: Starts the Maze game loop (Main.py); Starts Scatter graph file (Scatter.py)
            if self.reg_username not in self.DB_username:
                if (" " not in self.reg_username) and (" " not in self.reg_password):
                    if self.age <= 130:
                        self.username = self.reg_username
                        self.password = self.reg_password
                        self.reg_disabled = True
                        self.reg_panel.hide()
                        self.preview_panel.show()
        if process == self.preview_but:
            if self.reg_disabled == True:
                self.game_start = True
                self.reg(connection)
                while self.game_start:
                    self.game_loop()
                while self.graph_start:
                    self.run_graph()
            elif self.log_disabled == True:
                self.graph_start = True
                while self.graph_start:
                    Scatter_Menu(self.username, self.password)   
        if process == self.log_but: # Checks if information entered matches with user info in the database.
            n = -1
            self.game_start = False
            for name in self.DB_username:
                n += 1
                if self.log_username == name and self.log_password == self.DB_password[n]:
                    self.username = self.log_username
                    self.password = self.log_password
                    self.log_disabled = True
                    self.reg_panel.hide()
                    self.preview_panel.show()       
        if process == self.back_but:
            return False
        
    def game_loop(self): # Function: runs the maze in main 3 times and each time recorded is appended to a time_array, then starts the scatter graph file.
        if self.count != 0:
            main = Main()
            main.run()
            time = main.time_taken
            self.time_array.append(time)
            self.count -= 1
        elif self.count == 0:
            self.game_start = False
            self.graph_start = True

    def run_graph(self): # Function: creates a time average from the 3 time values and updates the users times with the new values. Then runs the scatter graph file.
        t_avg = 0
        for time in self.time_array:
            t_avg += time
        t_avg = int(t_avg / 3)
        Database.get_times_from_user(self.connection, self.time_array[0], self.time_array[1], self.time_array[2], t_avg, self.username, self.password)
        Scatter_Menu(self.username, self.password)

    def reg(self, connection): # Function: runs a database.py function add_user() to submit the username, password and age values into the database as a new user.
        null = 0
        Database.add_user(self.connection, self.username, self.password, self.age, null, null, null, null, null)
    
process = Login(connection)

def menu():# Function: Runs the pygame loop and the pygame_gui UI elements for this specific file
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