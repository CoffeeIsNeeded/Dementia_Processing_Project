import SQL

MENU_PROMT = """---SQL USER MENU---

Options:
1. Add User
2. See all users
3. See user by name
4. Update user times
5. Exit

Your Option: """

def menu():
    connection = SQL.connect()
    SQL.create_tables(connection)
    
    while (user_input := input(MENU_PROMT)) != "5":
        if user_input == "1":
            null = 0
            username = input("Enter username:")
            password = input("Enter password:")
            age = int(input("Enter age:"))
            
            SQL.add_user(connection, username, password, age, null, null, null, null, null)
        elif user_input == "2":
            users = SQL.get_all_users(connection)
            
            for user in users:
                print(user)
        elif user_input == "3":
            pass
        elif user_input == "4":
            username = input("Enter username:")
            password = input("Enter password:")
            t_1 = int(input("Enter time 1"))
            t_2 = int(input("Enter time 2"))
            t_3 = int(input("Enter time 3"))
            t_all = int(input("Enter time total"))

            SQL.get_times_from_user(connection, username, password, t_1, t_2, t_3, t_all)
        else:
            print("Ivalid Input")
menu()