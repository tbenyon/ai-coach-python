"""
db.py - Database Connection and Setup

This file does two things:
1. Provides get_db_connection() for other files to use
2. When run directly (python3 db.py), seeds the database with sample data

You can run this script multiple times safely - it won't duplicate data!
"""

# Import sqlite3 to work with our database (built into Python)
import sqlite3

# Import os to check if files exist (built into Python)
import os


def get_db_connection():
    """
    Create and return a connection to the database.

    Returns:
        A database connection object that we can use to run queries
    """

    # Connect to the database file called 'coaching_app.db'
    conn = sqlite3.connect('coaching_app.db')

    # This lets us access columns by name instead of by number
    # For example: user['username'] instead of user[0]
    conn.row_factory = sqlite3.Row

    return conn


def seed_database():
    """
    Set up the database tables and add sample data.
    This function is idempotent - safe to run multiple times.
    """

    print("Setting up the database...")
    print("")

    # Connect to the database (creates the file if it doesn't exist)
    conn = sqlite3.connect('coaching_app.db')
    cursor = conn.cursor()

    # ============================================================
    # CREATE THE DATABASE TABLES
    # ============================================================

    print("Creating 'clients' table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    print("  'clients' table is ready!")

    print("Creating 'workout_log' table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workout_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            date_time TEXT NOT NULL,
            miles_run REAL NOT NULL,
            push_up_count INTEGER NOT NULL,
            bench_press_weight REAL NOT NULL
        )
    ''')
    print("  'workout_log' table is ready!")

    print("Creating 'nutrition_log' table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nutrition_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            date_time TEXT NOT NULL,
            calories INTEGER NOT NULL,
            protein_percent INTEGER NOT NULL,
            carbs_percent INTEGER NOT NULL,
            fats_percent INTEGER NOT NULL
        )
    ''')
    print("  'nutrition_log' table is ready!")
    print("")

    conn.commit()

    # ============================================================
    # ADD SAMPLE CLIENT DATA
    # ============================================================

    print("Adding sample data...")
    print("")

    # Check if Tom already exists
    cursor.execute('SELECT id FROM clients WHERE username = ?', ('tom',))
    existing_client = cursor.fetchone()

    if existing_client is None:
        cursor.execute('''
            INSERT INTO clients (username, password, first_name, last_name, gender, age)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('tom', 'sixseven', 'Tom', 'Benyon', 'male', 25))
        print("  Added client: Tom Benyon (username: tom)")
        conn.commit()

        cursor.execute('SELECT id FROM clients WHERE username = ?', ('tom',))
        tom_id = cursor.fetchone()[0]
    else:
        print("  Client 'tom' already exists - skipping")
        tom_id = existing_client[0]

    print("")

    # ============================================================
    # ADD SAMPLE WORKOUT DATA
    # ============================================================

    print("Adding workout logs for Tom...")

    # Workout 1
    cursor.execute('SELECT id FROM workout_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-11-24 07:30:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight) VALUES (?, ?, ?, ?, ?)',
            (tom_id, '2024-11-24 07:30:00', 2.5, 30, 135.0))
        print("  Added workout: Nov 24 - 2.5 miles, 30 push-ups, 135 lbs bench")
    else:
        print("  Workout Nov 24 already exists - skipping")

    # Workout 2
    cursor.execute('SELECT id FROM workout_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-11-27 06:45:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight) VALUES (?, ?, ?, ?, ?)',
            (tom_id, '2024-11-27 06:45:00', 3.0, 35, 140.0))
        print("  Added workout: Nov 27 - 3.0 miles, 35 push-ups, 140 lbs bench")
    else:
        print("  Workout Nov 27 already exists - skipping")

    # Workout 3
    cursor.execute('SELECT id FROM workout_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-01 08:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight) VALUES (?, ?, ?, ?, ?)',
            (tom_id, '2024-12-01 08:00:00', 2.0, 40, 145.0))
        print("  Added workout: Dec 1 - 2.0 miles, 40 push-ups, 145 lbs bench")
    else:
        print("  Workout Dec 1 already exists - skipping")

    # Workout 4
    cursor.execute('SELECT id FROM workout_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-04 07:15:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight) VALUES (?, ?, ?, ?, ?)',
            (tom_id, '2024-12-04 07:15:00', 3.5, 45, 150.0))
        print("  Added workout: Dec 4 - 3.5 miles, 45 push-ups, 150 lbs bench")
    else:
        print("  Workout Dec 4 already exists - skipping")

    # Workout 5
    cursor.execute('SELECT id FROM workout_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-07 06:30:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO workout_log (client_id, date_time, miles_run, push_up_count, bench_press_weight) VALUES (?, ?, ?, ?, ?)',
            (tom_id, '2024-12-07 06:30:00', 4.0, 50, 155.0))
        print("  Added workout: Dec 7 - 4.0 miles, 50 push-ups, 155 lbs bench")
    else:
        print("  Workout Dec 7 already exists - skipping")

    conn.commit()
    print("")

    # ============================================================
    # ADD SAMPLE NUTRITION DATA
    # ============================================================

    print("Adding nutrition logs for Tom...")

    # Nutrition 1
    cursor.execute('SELECT id FROM nutrition_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-11-24 12:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent) VALUES (?, ?, ?, ?, ?, ?)',
            (tom_id, '2024-11-24 12:00:00', 2200, 25, 50, 25))
        print("  Added nutrition: Nov 24 - 2200 cal (25% protein, 50% carbs, 25% fat)")
    else:
        print("  Nutrition Nov 24 already exists - skipping")

    # Nutrition 2
    cursor.execute('SELECT id FROM nutrition_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-11-27 12:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent) VALUES (?, ?, ?, ?, ?, ?)',
            (tom_id, '2024-11-27 12:00:00', 2400, 30, 45, 25))
        print("  Added nutrition: Nov 27 - 2400 cal (30% protein, 45% carbs, 25% fat)")
    else:
        print("  Nutrition Nov 27 already exists - skipping")

    # Nutrition 3
    cursor.execute('SELECT id FROM nutrition_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-01 12:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent) VALUES (?, ?, ?, ?, ?, ?)',
            (tom_id, '2024-12-01 12:00:00', 2100, 20, 55, 25))
        print("  Added nutrition: Dec 1 - 2100 cal (20% protein, 55% carbs, 25% fat)")
    else:
        print("  Nutrition Dec 1 already exists - skipping")

    # Nutrition 4
    cursor.execute('SELECT id FROM nutrition_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-04 12:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent) VALUES (?, ?, ?, ?, ?, ?)',
            (tom_id, '2024-12-04 12:00:00', 2500, 35, 40, 25))
        print("  Added nutrition: Dec 4 - 2500 cal (35% protein, 40% carbs, 25% fat)")
    else:
        print("  Nutrition Dec 4 already exists - skipping")

    # Nutrition 5
    cursor.execute('SELECT id FROM nutrition_log WHERE client_id = ? AND date_time = ?', (tom_id, '2024-12-07 12:00:00'))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent) VALUES (?, ?, ?, ?, ?, ?)',
            (tom_id, '2024-12-07 12:00:00', 2300, 30, 45, 25))
        print("  Added nutrition: Dec 7 - 2300 cal (30% protein, 45% carbs, 25% fat)")
    else:
        print("  Nutrition Dec 7 already exists - skipping")

    conn.commit()
    print("")

    # ============================================================
    # CREATE THE .ENV TEMPLATE FILE
    # ============================================================

    print("Checking for .env file...")

    if os.path.exists('.env'):
        print("  .env file already exists - skipping")
    else:
        with open('.env', 'w') as env_file:
            env_file.write('# OpenAI API Key\n')
            env_file.write('# Get your key from: https://platform.openai.com/api-keys\n')
            env_file.write('# Replace "your_api_key_here" with your actual key\n')
            env_file.write('OPEN_AI_ACCESS_KEY=your_api_key_here\n')
        print("  Created .env template file")
        print("  IMPORTANT: Edit .env and add your OpenAI API key!")

    print("")

    # Close the connection
    conn.close()

    print("Database setup complete!")
    print("")
    print("You can now run:")
    print("  python3 client_cli.py   - to use the client app")
    print("  python3 trainer_cli.py  - to use the trainer app")


# Run seed_database() when this file is executed directly
if __name__ == "__main__":
    seed_database()
