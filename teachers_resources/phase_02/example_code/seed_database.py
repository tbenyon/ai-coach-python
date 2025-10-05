"""
Database Seeder Script
Creates the database and users table with sample data
"""

import sqlite3

def create_database():
    """Create database and users table with sample data"""

    # Connect to database (creates file if it doesn't exist)
    conn = sqlite3.connect('coaching_app.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT
        )
    ''')

    # Check if users already exist
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]

    if user_count == 0:
        # Insert sample users
        sample_users = [
            ('Alice Babyface', 3, 'alice@email.com'),
            ('Bob Smith', 16, 'bob@email.com'),
            ('Charlie Brown', 88, 'charlie@email.com')
        ]

        cursor.executemany('''
            INSERT INTO users (name, age, email)
            VALUES (?, ?, ?)
        ''', sample_users)

        # Save changes
        conn.commit()

        print("✓ Database created successfully!")
        print(f"✓ Inserted {len(sample_users)} sample users")
    else:
        print("✓ Database already seeded with users. No new users added.")

    # Close connection
    conn.close()

if __name__ == "__main__":
    create_database()
