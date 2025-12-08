# Phase 2: Adding Nutrition Tracking to the Trainer App

In this phase, you'll add the ability for trainers to view a client's nutrition logs.

The database already has a `nutrition_log` table with sample data. You just need to add the code to query and display it!

---

## Task 1: Add the Service Function

Open `trainer_service.py` and add a new function called `get_recent_nutrition_logs`.

Look at the `get_recent_workouts` function as an example - your new function will follow the same pattern.

**Here's the SQL query you'll need:**

```sql
SELECT id, client_id, date_time, calories, protein_percent, carbs_percent, fats_percent
FROM nutrition_log
WHERE client_id = ?
ORDER BY date_time DESC
```

---

## Task 2: Import the Function in the CLI

Open `trainer_cli.py` and update the import statement at the top:

**Change this:**
```python
from trainer_service import get_all_clients, get_client_by_id, get_recent_workouts
```

**To this:**
```python
from trainer_service import get_all_clients, get_client_by_id, get_recent_workouts, get_recent_nutrition_logs
```

---

## Task 3: Add the Handler Function

In `trainer_cli.py`, add a new function called `handle_get_nutrition`.

Look at `handle_get_workouts` as an example - your function will follow the same pattern.

Your function should:
1. Print a heading like "--- Recent Nutrition Logs ---"
2. Ask the user for a client ID
3. Handle invalid input (what if they type "abc"?)
4. Call `get_recent_nutrition_logs` with the client ID
5. Print the results as JSON

---

## Task 4: Add the Menu Option

In the `main_menu()` function, add the nutrition option to the menu.

You'll need to:
1. Add a new print statement for the nutrition option
2. Add an `elif` block to handle the choice
3. Update the other option numbers accordingly

The menu should now look like:
```
1. Show list of clients
2. Get recent workouts
3. Get recent nutrition logs
4. Generate AI feedback
5. Exit
```

---

## Test Your Changes

1. Run `python3 trainer_cli.py`
2. Select option 3 (Get recent nutrition logs)
3. Enter client ID: 1
4. You should see the nutrition data displayed as JSON

---

## Questions

1. Look at the `get_recent_nutrition_logs` function. What does `ORDER BY date_time DESC` do?

2. What would happen if you passed a client_id that doesn't exist?

3. Compare `get_recent_workouts` and `get_recent_nutrition_logs`. What's similar? What's different?
