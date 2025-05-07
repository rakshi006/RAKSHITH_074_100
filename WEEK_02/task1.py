users = []

def add_user():
    uid = int(input("Enter user ID: "))
    name = input("Enter name: ")
    email = input("Enter email: ")
    users.append({"id": uid, "name": name, "email": email})
    print("User added.")

def get_user_by_id():
    uid = int(input("Enter user ID to retrieve: "))
    for u in users:
        if u["id"] == uid:
            print("User found:", u)
            return
    print("User not found.")

def update_user():
    uid = int(input("Enter user ID to update: "))
    for u in users:
        if u["id"] == uid:
            name = input("Enter new name : ")
            email = input("Enter new email : ")
            if name != "":
                u["name"] = name
            if email != "":
                u["email"] = email
            print("User updated.")
            return
    print("User not found.")

def delete_user():
    uid = int(input("Enter user ID to delete: "))
    for u in users:
        if u["id"] == uid:
            users.remove(u)
            print("User deleted.")
            return
    print("User not found.")

def show_menu():
    while True:
        print("\n--- User Manager ---")
        print("1. Add User")
        print("2. Get User by ID")
        print("3. Update User")
        print("4. Delete User")
        print("5. Show All Users")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            get_user_by_id()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("All users:", users)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

show_menu()
