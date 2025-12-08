"""
trainer_service.py - Database Operations for Trainers

This file contains all the functions that trainers need to:
- View all their clients
- See a client's recent workouts
- See a client's recent nutrition logs
- Get client information by ID

Each function handles connecting to the database, running queries,
and returning the results as a list of dictionaries.
"""

# Import our database connection helper
from db import get_db_connection


def get_all_clients():
    """
    Get a list of all clients in the system.

    Returns:
        A list of dictionaries containing all clients
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Get all clients, ordered by their ID
    cursor.execute('''
        SELECT id, username, first_name, last_name, gender, age
        FROM clients
        ORDER BY id
    ''')

    # Fetch all the results
    clients = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert to list of dictionaries and return
    return [dict(client) for client in clients]


def get_client_by_id(client_id):
    """
    Get a single client's information by their ID.

    Args:
        client_id: The unique ID of the client

    Returns:
        The client's information if found, or None if not found
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Look for a client with this ID
    cursor.execute('''
        SELECT id, username, first_name, last_name, gender, age
        FROM clients
        WHERE id = ?
    ''', (client_id,))

    # Try to get the result
    client = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return the client (or None if not found)
    return client


def get_recent_workouts(client_id, limit=3):
    """
    Get a client's most recent workouts.

    Args:
        client_id: The ID of the client
        limit: How many workouts to return (default is 3)

    Returns:
        A list of dictionaries containing the client's most recent workouts
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Get the most recent workouts for this client
    # ORDER BY date_time DESC puts newest first
    # LIMIT ? restricts how many results we get
    cursor.execute('''
        SELECT id, client_id, date_time, miles_run, push_up_count, bench_press_weight
        FROM workout_log
        WHERE client_id = ?
        ORDER BY date_time DESC
        LIMIT ?
    ''', (client_id, limit))

    # Fetch all the results
    workouts = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert to list of dictionaries and return
    return [dict(w) for w in workouts]


def get_recent_nutrition_logs(client_id, limit=3):
    """
    Get a client's most recent nutrition logs.

    Args:
        client_id: The ID of the client
        limit: How many nutrition logs to return (default is 3)

    Returns:
        A list of dictionaries containing the client's most recent nutrition logs
    """

    # Get a connection to the database
    conn = get_db_connection()

    # Create a cursor to run our query
    cursor = conn.cursor()

    # Get the most recent nutrition logs for this client
    # ORDER BY date_time DESC puts newest first
    # LIMIT ? restricts how many results we get
    cursor.execute('''
        SELECT id, client_id, date_time, calories, protein_percent, carbs_percent, fats_percent
        FROM nutrition_log
        WHERE client_id = ?
        ORDER BY date_time DESC
        LIMIT ?
    ''', (client_id, limit))

    # Fetch all the results
    nutrition_logs = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert to list of dictionaries and return
    return [dict(n) for n in nutrition_logs]
