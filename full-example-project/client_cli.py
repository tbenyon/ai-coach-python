"""
client_cli.py - Client Command Line Interface

This is the main app that clients use to:
- Log in to their account
- Log their workouts
- Log their nutrition

Run this file with: python3 client_cli.py
"""

# Import our service functions
from client_service import authenticate_client, add_workout_log, add_nutrition_log


# This variable stores the currently logged-in user
# It starts as None (no one is logged in)
# When someone logs in, it becomes a dictionary with their info
current_user = None


def handle_login():
    """
    Handle the login process.

    Asks the user for their username and password,
    then checks if they match a client in the database.
    """

    # We need to modify the global current_user variable
    global current_user

    # Check if someone is already logged in
    if current_user is not None:
        print(f"You are already logged in as {current_user['first_name']}!")
        return

    print("")
    print("--- Login ---")

    # Ask for username
    username = input("Enter your username: ")

    # Ask for password
    password = input("Enter your password: ")

    # Try to authenticate with the database
    client = authenticate_client(username, password)

    # Check if login was successful
    if client is not None:
        # Login successful! Store the user info
        current_user = client
        print("")
        print(f"Welcome, {current_user['first_name']} {current_user['last_name']}!")
    else:
        # Login failed
        print("")
        print("Invalid username or password. Please try again.")


def handle_logout():
    """
    Handle the logout process.

    Clears the current user so they need to log in again.
    """

    # We need to modify the global current_user variable
    global current_user

    # Check if someone is actually logged in
    if current_user is None:
        print("You are not logged in!")
        return

    # Say goodbye and clear the user
    print(f"Goodbye, {current_user['first_name']}!")
    current_user = None


def handle_log_workout():
    """
    Handle logging a new workout.

    Asks the user for their workout details and saves them to the database.
    """

    # Check if someone is logged in
    if current_user is None:
        print("Please log in first!")
        return

    print("")
    print("--- Log Workout ---")

    # Ask for miles run
    miles_input = input("How many miles did you run? ")

    # Try to convert to a number
    try:
        miles_run = float(miles_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Ask for push-ups
    pushups_input = input("How many push-ups did you do? ")

    # Try to convert to a number
    try:
        push_up_count = int(pushups_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Ask for bench press weight
    bench_input = input("How much did you bench press (lbs)? ")

    # Try to convert to a number
    try:
        bench_press_weight = float(bench_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Ask for an optional comment (just press Enter to skip)
    comment_input = input("Any comment about this workout? (press Enter to skip) ").strip()
    comment = comment_input if comment_input else None

    # Save the workout to the database
    success = add_workout_log(
        current_user['id'],
        miles_run,
        push_up_count,
        bench_press_weight,
        comment
    )

    # Show confirmation
    if success:
        print("")
        print("Workout logged successfully!")
        print(f"  Miles run: {miles_run}")
        print(f"  Push-ups: {push_up_count}")
        print(f"  Bench press: {bench_press_weight} lbs")
        if comment:
            print(f"  Comment: {comment}")


def handle_log_nutrition():
    """
    Handle logging nutrition.

    Asks the user for their nutrition details and saves them to the database.
    """

    # Check if someone is logged in
    if current_user is None:
        print("Please log in first!")
        return

    print("")
    print("--- Log Nutrition ---")

    # Ask for calories
    calories_input = input("How many calories did you consume today? ")

    # Try to convert to a number
    try:
        calories = int(calories_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Ask for protein percentage
    protein_input = input("What percentage was protein? (0-100) ")

    # Try to convert to a number
    try:
        protein_percent = int(protein_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Ask for carbs percentage
    carbs_input = input("What percentage was carbohydrates? (0-100) ")

    # Try to convert to a number
    try:
        carbs_percent = int(carbs_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Ask for fats percentage
    fats_input = input("What percentage was fats? (0-100) ")

    # Try to convert to a number
    try:
        fats_percent = int(fats_input)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # Save the nutrition log to the database
    success = add_nutrition_log(
        current_user['id'],
        calories,
        protein_percent,
        carbs_percent,
        fats_percent
    )

    # Show confirmation
    if success:
        print("")
        print("Nutrition logged successfully!")
        print(f"  Calories: {calories}")
        print(f"  Protein: {protein_percent}%")
        print(f"  Carbs: {carbs_percent}%")
        print(f"  Fats: {fats_percent}%")


def main_menu():
    """
    Display the main menu and handle user choices.

    This is the main loop of the application.
    It keeps running until the user chooses to exit.
    """

    print("")
    print("=================================")
    print("   Welcome to Fitness Tracker")
    print("         (Client App)")
    print("=================================")

    # Keep showing the menu until the user exits
    while True:
        print("")
        print("--- Main Menu ---")

        # Show different options based on login status
        if current_user is None:
            print("1. Login")
        else:
            print(f"Logged in as: {current_user['first_name']}")
            print("1. Logout")

        print("2. Log workout")
        print("3. Log nutrition")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        # Handle the choice
        if choice == "1":
            # Login or Logout depending on status
            if current_user is None:
                handle_login()
            else:
                handle_logout()

        elif choice == "2":
            handle_log_workout()

        elif choice == "3":
            handle_log_nutrition()

        elif choice == "4":
            # Exit the program
            print("")
            print("Thanks for using Fitness Tracker!")
            print("Goodbye!")
            break

        else:
            # Invalid choice
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


# This code runs when you execute the file directly
# (not when importing it as a module)
if __name__ == "__main__":
    main_menu()
