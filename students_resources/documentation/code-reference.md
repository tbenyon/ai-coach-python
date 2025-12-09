# Code Reference

This document explains all the files and methods in the example code.

---

## File Overview

| File | Purpose |
|------|---------|
| `db.py` | Database connection and setup |
| `trainer_service.py` | Database queries for trainer features |
| `client_service.py` | Database queries for client features |
| `trainer_cli.py` | Trainer command-line interface |
| `client_cli.py` | Client command-line interface |
| `ai_service.py` | OpenAI API integration |

---

## db.py

**Purpose:** Handles database connection and seeds sample data.

### Methods

#### `get_db_connection()`
Creates and returns a connection to the SQLite database.

- **Returns:** A database connection object
- **Used by:** All service files to connect to the database

```python
conn = get_db_connection()
cursor = conn.cursor()
# ... run queries ...
conn.close()
```

#### `seed_database()`
Sets up database tables and adds sample data. Safe to run multiple times.

- **Creates tables:** `clients`, `workout_log`, `nutrition_log`
- **Adds sample client:** Tom Benyon (username: `tom`, password: `sixseven`)
- **Adds sample data:** 5 workouts and 5 nutrition logs
- **Creates:** `.env` template file

**Run with:** `python3 db.py` (or `python db.py` on Windows)

---

## trainer_service.py

**Purpose:** Database operations for trainer features.

### Methods

#### `get_all_clients()`
Gets a list of all clients in the system.

- **Returns:** List of dictionaries containing client info
- **SQL:** `SELECT ... FROM clients ORDER BY id`

#### `get_client_by_id(client_id)`
Gets a single client's information.

- **Parameters:** `client_id` - The client's ID number
- **Returns:** Client dictionary if found, `None` if not found
- **SQL:** `SELECT ... FROM clients WHERE id = ?`

#### `get_recent_workouts(client_id)`
Gets all workouts for a client, newest first.

- **Parameters:** `client_id` - The client's ID number
- **Returns:** List of workout dictionaries
- **SQL:** `SELECT ... FROM workout_log WHERE client_id = ? ORDER BY date_time DESC`

---

## client_service.py

**Purpose:** Database operations for client features.

### Methods

#### `authenticate_client(username, password)`
Checks if login credentials are correct.

- **Parameters:** `username`, `password` - Login credentials
- **Returns:** Client dictionary if login successful, `None` if failed
- **SQL:** `SELECT ... FROM clients WHERE username = ? AND password = ?`

#### `add_workout_log(client_id, miles_run, push_up_count, bench_press_weight)`
Saves a new workout to the database.

- **Parameters:**
  - `client_id` - The client's ID
  - `miles_run` - Miles run (decimal)
  - `push_up_count` - Number of push-ups (integer)
  - `bench_press_weight` - Bench press weight in lbs (decimal)
- **Returns:** `True` if successful
- **SQL:** `INSERT INTO workout_log ...`

---

## trainer_cli.py

**Purpose:** Command-line interface for trainers.

**Run with:** `python3 trainer_cli.py` (or `python trainer_cli.py` on Windows)

### Methods

#### `main_menu()`
The main loop that displays the menu and handles user choices.

- Shows menu options
- Calls appropriate handler based on user input
- Runs until user chooses Exit

#### `handle_show_clients()`
Displays all clients as JSON.

- Calls `get_all_clients()` from trainer_service
- Prints results using `json.dumps()`

#### `handle_get_workouts()`
Displays a client's workouts.

- Asks user for client ID
- Validates input is a number
- Calls `get_recent_workouts()` from trainer_service
- Prints results as JSON

#### `generate_feedback(client_name, workouts_json)`
Builds an AI prompt and gets feedback.

- **Parameters:**
  - `client_name` - Client's first name
  - `workouts_json` - Workout data as JSON string
- **Returns:** AI response string, or `None` on error
- Builds prompt with client name and workout data
- Calls `call_ai()` from ai_service

#### `handle_generate_feedback()`
Handles the AI feedback menu option.

- Asks user for client ID
- Checks client exists using `get_client_by_id()`
- Fetches workouts and converts to JSON
- Calls `generate_feedback()` to get AI response
- Displays the feedback

---

## client_cli.py

**Purpose:** Command-line interface for clients.

**Run with:** `python3 client_cli.py` (or `python client_cli.py` on Windows)

### Global Variable

#### `current_user`
Stores the logged-in client's info. `None` when no one is logged in.

### Methods

#### `main_menu()`
The main loop that displays the menu and handles user choices.

- Shows Login or Logout based on `current_user` state
- Runs until user chooses Exit

#### `handle_login()`
Handles the login process.

- Asks for username and password
- Calls `authenticate_client()` from client_service
- Stores client info in `current_user` if successful

#### `handle_logout()`
Handles the logout process.

- Sets `current_user` to `None`

#### `handle_log_workout()`
Handles logging a new workout.

- Checks user is logged in
- Asks for miles run, push-ups, bench press weight
- Validates all inputs are numbers
- Calls `add_workout_log()` from client_service
- Shows confirmation message

---

## ai_service.py

**Purpose:** Handles communication with the OpenAI API.

### Methods

#### `load_api_key()`
Reads the API key from the `.env` file.

- **Returns:** API key string, or `None` if not found
- Manually parses `.env` file (no external packages needed)

#### `get_api_key()`
Gets and validates the API key.

- **Returns:** API key if valid, `None` if missing or placeholder
- Calls `load_api_key()`
- Checks key isn't still `your_api_key_here`

#### `call_ai(prompt)`
Sends a prompt to OpenAI and gets a response.

- **Parameters:** `prompt` - The text to send to the AI
- **Returns:** AI response string, or `None` on error
- Uses `urllib.request` to make HTTP POST request
- Sends to `api.openai.com/v1/chat/completions`
- Parses response: `result['choices'][0]['message']['content']`

---

## Database Tables

### clients
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Login username |
| password | TEXT | Login password |
| first_name | TEXT | Client's first name |
| last_name | TEXT | Client's last name |
| gender | TEXT | Client's gender |
| age | INTEGER | Client's age |

### workout_log
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| client_id | INTEGER | References clients.id |
| date_time | TEXT | When workout was logged |
| miles_run | REAL | Miles run |
| push_up_count | INTEGER | Number of push-ups |
| bench_press_weight | REAL | Bench press weight (lbs) |

### nutrition_log
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| client_id | INTEGER | References clients.id |
| date_time | TEXT | When nutrition was logged |
| calories | INTEGER | Total calories |
| protein_percent | INTEGER | % from protein |
| carbs_percent | INTEGER | % from carbs |
| fats_percent | INTEGER | % from fats |
