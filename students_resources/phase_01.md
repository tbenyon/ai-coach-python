# Phase 1: Getting Started

In this phase, you'll set up your fitness tracking application and explore how it works.

## Running the Application

### Trainer App

Run `trainer_cli.py` and try these options:
- **Option 1**: View all clients
- **Option 2**: Get recent workouts for a client (try client ID: 1)

### Client App

Run `client_cli.py` and try these options:
- **Option 1**: Login (username: `tom`, password: `sixseven`)
- **Option 2**: Log a new workout

---

## Tasks

### Task 1: Enable AI Feedback

The trainer app has an AI feedback feature that's currently disabled. Let's turn it on!

1. Open `trainer_cli.py`

2. Find the `main_menu()` function

3. Look for the commented-out lines that mention "Generate AI feedback":
   ```python
   #         print("3. Generate AI feedback")
   ```
   and
   ```python
   #         elif choice == "3":
   #             handle_generate_feedback()
   ```

4. Uncomment these lines by removing the `#` symbols

5. Update the menu numbers - Exit should now be option 4

6. Run `trainer_cli.py` again and try option 3 to generate AI feedback for a client

---

## Questions

Take a moment to explore the code and answer these questions:

1. **In `db.py`**: What does `conn.row_factory = sqlite3.Row` do? Why is it useful?

2. **In `trainer_service.py`**: What does `cursor.fetchall()` return? How is it different from `cursor.fetchone()`?

3. **In `trainer_cli.py`**: What does `json.dumps(data, indent=2)` do? Why do we use it?

4. **In `ai_service.py`**: What happens if the API key is missing?

5. **In `client_cli.py`**: Why do we use `global current_user` at the start of some functions?
