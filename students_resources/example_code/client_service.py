"""
client_service.py - Database Operations for Clients

This file contains all the functions that clients need to:
- Log in to their account
- Log their workouts

Each function handles connecting to the database, running queries,
and returning the results.
"""

# Import our database connection helper
from db import get_db_connection

# Import datetime so we can record when workouts/nutrition are logged
from datetime import datetime


def authenticate_client(username, password):
    """
    Check if a client's username and password are correct.

    Args:
        username: The username the client typed in
        password: The password the client typed in

    Returns:
        A dictionary with the client's info if login successful
        None if the username or password is wrong
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Look for a client with this username AND password
    # We use ? placeholders to safely insert the values (prevents SQL injection)
    cursor.execute('''
        SELECT id, username, first_name, last_name, gender, age
        FROM clients
        WHERE username = ? AND password = ?
    ''', (username, password))

    # Try to get the result
    client = cursor.fetchone()

    # Close the database connection
    conn.close()

    # If we found a matching client, return their info as a dictionary
    if client is not None:
        # Create a dictionary with all the client's information
        # This makes it easy to access: client_info['first_name']
        client_info = {
            'id': client['id'],
            'username': client['username'],
            'first_name': client['first_name'],
            'last_name': client['last_name'],
            'gender': client['gender'],
            'age': client['age']
        }
        return client_info

    # No matching client found - wrong username or password
    return None


def add_workout_log(client_id, miles_run, push_up_count, bench_press_weight):
    """
    Save a new workout to the database.

    Args:
        client_id: The ID of the client who did the workout
        miles_run: How many miles they ran (can be decimal like 2.5)
        push_up_count: How many push-ups they did
        bench_press_weight: How much weight they bench pressed

    Returns:
        True if the workout was saved successfully
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Get the current date and time
    # This records exactly when the workout was logged
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insert the new workout into the database
    cursor.execute('''
        INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight)
        VALUES (?, ?, ?, ?, ?)
    ''', (client_id, current_time, miles_run, push_up_count, bench_press_weight))

    # Save the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

    # Return True to indicate success
    return True
