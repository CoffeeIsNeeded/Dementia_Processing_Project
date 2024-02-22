import Database

MENU_PROMT = """---SQL USER MENU---

Options:
1. Add User
2. See all users
3. See user by name
4. Update user times
5. Exit

Your Option: """

def Add_User(connection):
    null = 0
    username = input("Enter username:")
    password = input("Enter password:")
    age = int(input("Enter age:"))
    Database.add_user(connection, username, password, age, null, null, null, null, null)

def See_All_Users(connection):
    users = Database.get_all_users(connection)
    for user in users:
        print(user)

def Update_Times(connection):
    username = input("Enter username:")
    password = input("Enter password:")
            
    t_1 = int(input("Enter time 1"))
    t_2 = int(input("Enter time 2"))
    t_3 = int(input("Enter time 3"))
    t_avg = (t_1 + t_2 + t_3) / 3
            
    Database.get_times_from_user(connection, t_1, t_2, t_3, t_avg, username, password)

def menu():
    connection = Database.connect()
    Database.create_tables(connection)
    
    while (user_input := input(MENU_PROMT)) != "5":
        if user_input == "1":
            Add_User(connection)
        elif user_input == "2":
            See_All_Users(connection)
        elif user_input == "3":
            pass
        elif user_input == "4":
            Update_Times(connection)
        else:
            print("Ivalid Input")
menu()