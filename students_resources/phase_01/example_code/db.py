"""
Database Connection
Helper functions for database connections
"""

import sqlite3

def get_db_connection():
    """
    Get a connection to the database with Row factory enabled

    Returns:
        sqlite3.Connection: Database connection with named column access
    """
    conn = sqlite3.connect('coaching_app.db')
    conn.row_factory = sqlite3.Row  # Enable named column access
    return conn
