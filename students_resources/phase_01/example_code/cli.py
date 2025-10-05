"""
CLI - Command Line Interface
Simple menu system for the coaching app
"""

from userService import add_user, get_user_by_email

def handle_add_user():
    """Handle adding a new user"""
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    add_user(name, int(age), email)

def handle_get_user():
    """Handle getting a user by email"""
    email = input("Enter email: ")
    user = get_user_by_email(email)

    if user:
        print(f"\nUser found:")
        print(f"ID: {user[0]}")
        print(f"Name: {user[1]}")
        print(f"Age: {user[2]}")
        print(f"Email: {user[3]}")
    else:
        print("User not found!")

def main_menu():
    """Display main menu and handle user choices"""

    while True:
        print("\n=== Coaching App ===")
        print("1. Add a user")
        print("2. Get user by email")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_get_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
