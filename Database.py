import sqlite3

# ------SQL Queries:------
CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username VARCHAR(30), password VARCHAR(30), age INTEGER, t_1 INTEGER, t_2 INTEGER, t_3 INTEGER, t_avg INTEGER);"

INSERT_USER = "INSERT INTO users (username, password, age, t_1, t_2, t_3, t_avg) VALUES (?, ?, ?, ?, ?, ?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"
GET_ALL_AGE_Y_TIME = "SELECT age, t_avg FROM users;"
GET_USER_BY_NAME = "SELECT * FROM users WHERE username = ? AND password = ?;"
UPDATE_USER_TIMES_UP = "UPDATE users SET t_1 = ?, t_2 = ?, t_3 = ?, t_avg = ? WHERE username = ? AND password = ?;"
UPDATE_USER_TIMES_ID = "UPDATE users SET t_1 = ?, t_2 = ?, t_3 = ?, t_avg = ? WHERE id = ?;"

# ------SQL Functions:------
def connect(): # Function: Connects to the database.
    return sqlite3.connect("data.db")

def create_tables(connection): # Function: Creates a database table called users.
    with connection:
        connection.execute(CREATE_USER_TABLE)
        
def add_user(connection, username, password, age, t_1, t_2, t_3, t_avg): # Function: Adds a user to the database with the given values.
    with connection:
        connection.execute(INSERT_USER, (username, password, age, t_1, t_2, t_3, t_avg))

def get_all_users(connection): # Function: returns all users and thier data from the database.
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user(connection, username, password): # Function: returns a users information when a username and password are given that are in the database.
    with connection:
        return connection.execute(GET_USER_BY_NAME, (username, password)).fetchall()

def get_times_from_user(connection, username, password, t_1, t_2, t_3, t_avg): # Function: updates a specific user's time values when given the username, password, and all the time values.
    with connection:
        return connection.execute(UPDATE_USER_TIMES_UP, (username, password, t_1, t_2, t_3, t_avg))
    
def get_times_from_user_id(connection, identifer, t_1, t_2, t_3, t_avg): # Function: updates a specific user's time values when given the primary key identifier, and all the time values.
    with connection:
        return connection.execute(UPDATE_USER_TIMES_ID, (identifer, t_1, t_2, t_3, t_avg))
    
def get_all_age_y_time(connection): # Function: returns all users age and average time information.
    with connection:
        return connection.execute(GET_ALL_AGE_Y_TIME).fetchall()