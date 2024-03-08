import pygame as pg
import pygame_gui as pg_gui
from pygame_gui.core import ObjectID
from settings import *
from Main import *
import Login_and_Register

pg.init()
pg.display.set_caption('Memory Processing Tool')
display = pg.display.set_mode((RES))
background = pg.Surface((RES))
display.fill((STAND_BACK_COL))

manager = MANAGER

class Menu_But:
    def __init__(self):
        # ------GUI:------     
        # Panels:
        self.main_menu_panel = pg_gui.elements.UIPanel(
            pg.Rect((10, 10), (780, 780)), 
            1, 
            manager,
            object_id = ObjectID(
                class_id = '@Main_Menu Panels', 
                object_id = '#main_menu_panel'
                )
            )
        
        # Buttons:
        self.start_but = pg_gui.elements.UIButton(
            pg.Rect((500, 375), BUTTON_SIZE), 
            'START', 
            manager,
            container = self.main_menu_panel, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Buttons', 
                object_id = '#start_Button'
                )
            )
        self.quit_but = pg_gui.elements.UIButton(
            pg.Rect((500, 550), BUTTON_SIZE), 
            'QUIT', 
            manager,
            container = self.main_menu_panel, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Buttons', 
                object_id = '#quit_Button'
                )
            )
        # Text Boxes:
        self.welcome_text_box = pg_gui.elements.UITextBox(
            TEXT_ARRAY[3], 
            pg.Rect((50, 350), (300, 250)), 
            manager, 
            starting_height = 1, 
            container = self.main_menu_panel, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Text_Boxes', 
                object_id = '#welcome_text_box'
                )
        )

        # Labels:
        self.title_Label = pg_gui.elements.UILabel(
            pg.Rect((60, 50), (650, 150)), 
            "Memory Processing Tool", 
            manager,
            container = self.main_menu_panel, 
            object_id = ObjectID(
                class_id = '@Main_Menu_Labels', 
                object_id = '#title_label'
                )
            )
        
    def but_pressed(self, but): # Function: Checks if button has been pressed and acts accordingly.
        if but == self.start_but:
            Login_and_Register.menu()
        if but == self.quit_but:
            pg.quit()
            sys.exit()
            
but = Menu_But()

def menu(): # Function: runs pygame and pygame_gui elements for this file.
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
        
menu()
