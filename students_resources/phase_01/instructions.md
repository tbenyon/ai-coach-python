# PHASE 1: Database Setup and User Management
============================================

## OBJECTIVE:
Learn how to create a SQLite database and perform basic user operations.

## Core Steps

1. Run the seeder script to create your database:
   - Open your terminal/command prompt
   - Navigate to the project directory
   - Run: python seed_database.py
   - You should see a success message and a new file called 'coaching_app.db'

2. Review the provided files:
   - db.py: Contains database connection helper functions
   - userService.py: Contains functions to interact with the users table
   - cli.py: A simple command-line menu for the application

3. Run the application:
   - Run: python cli.py
   - Use the menu to:
     * Add a new user
     * Get the user you just added by email
     * Exit the program

## Questions

### Set 1: Understanding the Basics
1. In `cli.py`, what does the line `from userService import add_user, get_user_by_email` do?

2. In `db.py`, what is the name of the database file that the code connects to?

3. In `cli.py`, what happens when the user enters "3" in the main menu?

### Set 2: Understanding Functions and Flow
1. In `cli.py`, the `handle_add_user()` function collects user input. Why is `int(age)` used when calling `add_user()` instead of just `age`?

2. In `userService.py`, what does the `cursor.execute()` function do in the `add_user()` function?

3. In `cli.py`, look at the `handle_get_user()` function. How does the code access the user's name and email from the database result?

### Set 3: Advanced Concepts
1. Why do you think the database connection code was moved to a separate `db.py` file instead of being repeated in `userService.py`? What are the benefits of this approach?

2. In `cli.py`, the main menu uses a `while True:` loop. Explain how the program exits this infinite loop when the user selects option 3.

3. In `userService.py`, the SQL query uses `?` placeholders (e.g., `VALUES (?, ?, ?)`). Why do you think the code uses placeholders instead of directly inserting the values into the SQL string?

## Challenges
1. Explore and experiment:
   - Try adding some users
   - Try finding users by their email
   - Look at the code to understand how it works

CHALLENGE (Optional):
- Can you add a new menu option to list all users?
- Can you add validation to check if an email already exists?
