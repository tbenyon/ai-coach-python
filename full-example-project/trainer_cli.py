"""
trainer_cli.py - Trainer Command Line Interface

This is the main app that trainers use to:
- View their list of clients
- See a client's recent workouts
- See a client's recent nutrition logs
- Generate AI-powered feedback for a client

Run this file with: python3 trainer_cli.py
"""

# Import json to print data nicely (built into Python)
import json

# Import our service functions
from trainer_service import get_all_clients, get_client_by_id, get_recent_workouts, get_recent_nutrition_logs
from ai_service import call_ai


def handle_show_clients():
    """Display a list of all clients."""

    print("")
    print("--- All Clients ---")

    # Get all clients and print as JSON
    clients = get_all_clients()
    print(json.dumps(clients, indent=2))


def handle_get_workouts():
    """Display a client's recent workouts."""

    print("")
    print("--- Recent Workouts ---")

    # Ask for the client ID
    id_input = input("Enter client ID: ")

    # Try to convert to a number
    try:
        client_id = int(id_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Get the workouts and print as JSON
    workouts = get_recent_workouts(client_id)
    print(json.dumps(workouts, indent=2))


def handle_get_nutrition():
    """Display a client's recent nutrition logs."""

    print("")
    print("--- Recent Nutrition Logs ---")

    # Ask for the client ID
    id_input = input("Enter client ID: ")

    # Try to convert to a number
    try:
        client_id = int(id_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Get the nutrition logs and print as JSON
    nutrition = get_recent_nutrition_logs(client_id)
    print(json.dumps(nutrition, indent=2))


def generate_feedback(client_name, workouts_json, nutrition_json):
    """
    Build a prompt and call the AI to generate feedback.

    Args:
        client_name: The client's first name
        workouts_json: JSON string of recent workouts
        nutrition_json: JSON string of recent nutrition logs

    Returns:
        The AI's feedback as a string, or None if there was an error
    """

    # Build the prompt for the AI
    prompt = f"""You are a friendly fitness coach giving feedback to {client_name}.

Here are their recent workouts:
{workouts_json}

Here are their recent nutrition logs:
{nutrition_json}

Please provide brief, encouraging feedback on their progress.
Comment on their workout consistency and suggest improvements.
Also review their nutrition and suggest any changes.
Keep the feedback friendly and motivational.
Keep it under 150 words."""

    # Call the AI and return the response
    return call_ai(prompt)


def handle_generate_feedback():
    """Generate AI feedback for a client."""

    print("")
    print("--- Generate AI Feedback ---")

    # Ask for the client ID
    id_input = input("Enter client ID: ")

    # Try to convert to a number
    try:
        client_id = int(id_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Check if the client exists
    client = get_client_by_id(client_id)

    if client is None:
        print(f"No client found with ID {client_id}")
        return

    print("")
    print(f"Generating feedback for {client['first_name']}...")
    print("(This may take a moment)")
    print("")

    # Get recent workouts and nutrition as JSON
    workouts_json = json.dumps(get_recent_workouts(client_id), indent=2)
    nutrition_json = json.dumps(get_recent_nutrition_logs(client_id), indent=2)

    # Generate feedback using AI
    feedback = generate_feedback(client['first_name'], workouts_json, nutrition_json)

    # Check if feedback was generated successfully
    if feedback is None:
        print("Could not generate feedback. Check your API key configuration.")
        return

    # Display the feedback
    print("=" * 50)
    print("AI COACHING FEEDBACK")
    print("=" * 50)
    print("")
    print(feedback)
    print("")
    print("=" * 50)


def main_menu():
    """
    Display the main menu and handle user choices.

    This is the main loop of the application.
    It keeps running until the user chooses to exit.
    """

    print("")
    print("=================================")
    print("   Welcome to Fitness Tracker")
    print("        (Trainer App)")
    print("=================================")

    # Keep showing the menu until the user exits
    while True:
        print("")
        print("--- Main Menu ---")
        print("1. Show list of clients")
        print("2. Get recent workouts")
        print("3. Get recent nutrition logs")
        print("4. Generate AI feedback")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        # Handle the choice
        if choice == "1":
            handle_show_clients()

        elif choice == "2":
            handle_get_workouts()

        elif choice == "3":
            handle_get_nutrition()

        elif choice == "4":
            handle_generate_feedback()

        elif choice == "5":
            # Exit the program
            print("")
            print("Thanks for using Fitness Tracker!")
            print("Goodbye!")
            break

        else:
            # Invalid choice
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")


# This code runs when you execute the file directly
# (not when importing it as a module)
if __name__ == "__main__":
    main_menu()
