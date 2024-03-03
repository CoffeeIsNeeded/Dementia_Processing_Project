import Database

MENU_PROMT = """---SQL USER MENU---

Options:
1. Add User
2. See all users
3. See user by name
4. Update user times - user
5. Update user times - user id
6. Exit

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

def Update_Times_User(connection):
    username = input("Enter username:")
    password = input("Enter password:")
            
    t_1 = int(input("Enter time 1"))
    t_2 = int(input("Enter time 2"))
    t_3 = int(input("Enter time 3"))
    t_avg = (t_1 + t_2 + t_3) / 3
            
    Database.get_times_from_user(connection, t_1, t_2, t_3, t_avg, username, password)

def Update_Times_User_ID(connection):
    identifier = int(input("Enter ID"))

    t_1 = int(input("Enter time 1"))
    t_2 = int(input("Enter time 2"))
    t_3 = int(input("Enter time 3"))
    t_avg = (t_1 + t_2 + t_3) / 3
            
    Database.get_times_from_user_id(connection, t_1, t_2, t_3, t_avg, identifier)

def Get_User_By_Name(connection):
    username = input("Enter username:")
    password = input("Enter password:")

    user = Database.get_user(connection, username, password)
    print(user)

def menu():
    connection = Database.connect()
    Database.create_tables(connection)
    
    while (user_input := input(MENU_PROMT)) != "6":
        if user_input == "1":
            Add_User(connection)
        elif user_input == "2":
            See_All_Users(connection)
        elif user_input == "3":
            Get_User_By_Name(connection)
        elif user_input == "4":
            Update_Times_User(connection)
        elif user_input == "5":
            Update_Times_User_ID(connection)
        else:
            print("Ivalid Input")
menu()