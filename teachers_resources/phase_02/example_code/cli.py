"""
CLI - Command Line Interface
Simple menu system for the coaching app
"""

from userService import add_user, get_user_by_email, get_user_by_id
from ai_service import generate_response

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

def handle_generate_feedback():
    """Handle generating AI feedback for a user"""
    user_id = input("Enter user ID: ")

    try:
        user_id = int(user_id)
    except ValueError:
        print("❌ User ID must be a number!")
        return

    user = get_user_by_id(user_id)

    if not user:
        print(f"❌ User with ID {user_id} not found!")
        return

    # Extract user details (tuple: id, name, age, email)
    _, name, age, email = user

    print(f"\nGenerating feedback for {name} aged {age}...")

    # Create prompt for AI
    if age < 5:
        prompt = f"Generate constructive coaching feedback for a toddler named {name}. Encourage them to get more crawling exercise and cut down on the baby food that has less protein."
    else:
        prompt = f"Generate constructive coaching feedback for a user named {name}. Focus on personal development and goal setting."

    prompt += "Keep the feedback short."

    try:
        feedback = generate_response(prompt)
        print(f"\n{'='*50}")
        print(f"Feedback for {name}:")
        print(f"{'='*50}")
        print(feedback)
        print(f"{'='*50}\n")
    except Exception as e:
        print(f"❌ Error generating feedback: {str(e)}")

def main_menu():
    """Display main menu and handle user choices"""

    while True:
        print("\n=== Coaching App ===")
        print("1. Add a user")
        print("2. Get user by email")
        print("3. Generate AI feedback for user")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_get_user()
        elif choice == "3":
            handle_generate_feedback()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
