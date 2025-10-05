# PHASE 1: Database Setup and User Management
============================================

## OBJECTIVE:
Learn how to create a SQLite database and perform basic user operations.

## INSTRUCTIONS:

1. Run the seeder script to create your database:
   - Open your terminal/command prompt
   - Navigate to the project directory
   - Run: python seed_database.py
   - You should see a success message and a new file called 'coaching_app.db'

2. Review the provided files:
   - userService.py: Contains functions to interact with the users table
   - cli.py: A simple command-line menu for the application

3. Run the application:
   - Run: python cli.py
   - Use the menu to:
     * Add a new user
     * Get a user by email
     * Exit the program

4. Explore and experiment:
   - Try adding some users
   - Try finding users by their email
   - Look at the code to understand how it works

CHALLENGE (Optional):
- Can you add a new menu option to list all users?
- Can you add validation to check if an email already exists?
