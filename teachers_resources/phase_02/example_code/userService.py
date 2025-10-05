"""
User Service
Functions to interact with the users table
"""

import sqlite3

def add_user(name, age, email):
    """Add a new user to the database"""
    conn = sqlite3.connect('coaching_app.db')
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
    conn = sqlite3.connect('coaching_app.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE email = ?
    ''', (email,))

    user = cursor.fetchone()
    conn.close()

    return user

def get_user_by_id(user_id):
    """Get a user by their ID"""
    conn = sqlite3.connect('coaching_app.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (user_id,))

    user = cursor.fetchone()
    conn.close()

    return user
