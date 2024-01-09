import pygame as pg
import pygame_gui as pg_gui
import Dementia_Processing_Project.Database as Database

class Login:
    def __init__(self, username, password):
        username.self = username
        password.self = password
    
    def reg(self, connection):
        null = 0
        username = input("Enter username:")
        password = input("Enter password:")
        age = int(input("Enter age:"))
        Database.add_user(connection, username, password, age, null, null, null, null, null)

    def ent_cred(self):
        pass

    def chk_cred(self):
        pass

    def draw(self):
        pass