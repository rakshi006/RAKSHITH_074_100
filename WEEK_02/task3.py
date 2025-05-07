import hashlib

users = {}

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == hash_password(password):
        print("Login Successful")
    else:
        print("Invalid username or password")

def menu():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

menu()
