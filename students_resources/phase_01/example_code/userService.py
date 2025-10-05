"""
User Service
Functions to interact with the users table
"""

from db import get_db_connection

def add_user(name, age, email):
    """Add a new user to the database"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (name, age, email)
        VALUES (?, ?, ?)
    ''', (name, age, email))

    conn.commit()
    conn.close()
    print(f"✓ User {name} added successfully!")

def get_user_by_email(email):
    """Get a user by their email address"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE email = ?
    ''', (email,))

    user = cursor.fetchone()
    conn.close()

    return user
