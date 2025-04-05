import getpass
import os

USER_DATA_FILE = "users.txt"

def register():
    print("\n--- Register ---")
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")

    # Check if user already exists
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            for line in file:
                stored_user, _ = line.strip().split(":")
                if stored_user == username:
                    print("Username already exists. Try a different one.")
                    return

    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{password}\n")
    print("Registration successful!\n")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if not os.path.exists(USER_DATA_FILE):
        print("No users found. Please register first.")
        return False

    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(":")
            if stored_user == username and stored_pass == password:
                print("Login successful!\n")
                return True

    print("Invalid username or password.\n")
    return False

def secured_page():
    print("🎉 Welcome to the secured page! You have access now.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                secured_page()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()