# Amber Extension: Add Nutrition Logging to the Client App

**Difficulty:** Medium (Steps provided, no full code examples)

In this task, you'll add the ability for clients to log their nutrition. You'll follow the same pattern used for workout logging.

---

## Before You Start

Look at how workout logging works in the client app:

1. **In `client_service.py`**: Find the `add_workout_log` function
2. **In `client_cli.py`**: Find the `handle_log_workout` function and where it's called in the menu

Study these carefully - you'll be creating similar code for nutrition!

---

## Task Overview

You need to:
1. Add an `add_nutrition_log` function to `client_service.py`
2. Add a `handle_log_nutrition` function to `client_cli.py`
3. Add a menu option to log nutrition
4. Import the new function

---

## Step 1: Add the Service Function

Open `client_service.py` and add a function called `add_nutrition_log`.

Look at `add_workout_log` as your example - follow the same pattern.

**Here's the SQL query you'll need:**

```sql
INSERT INTO nutrition_log (client_id, date_time, calories, protein_percent, carbs_percent, fats_percent)
VALUES (?, ?, ?, ?, ?, ?)
```

**Your function should accept these parameters:**
- `client_id` - The ID of the client
- `calories` - Total calories consumed
- `protein_percent` - Percentage from protein (0-100)
- `carbs_percent` - Percentage from carbohydrates (0-100)
- `fats_percent` - Percentage from fats (0-100)

---

## Step 2: Update the Import

In `client_cli.py`, add `add_nutrition_log` to the import statement at the top.

---

## Step 3: Add the Handler Function

In `client_cli.py`, add a function called `handle_log_nutrition`.

Look at `handle_log_workout` as your example - follow the same pattern.

**Your function should:**
1. Check if someone is logged in (return early if not)
2. Print a heading like "--- Log Nutrition ---"
3. Ask for calories (as a whole number)
4. Ask for protein percentage (as a whole number)
5. Ask for carbs percentage (as a whole number)
6. Ask for fats percentage (as a whole number)
7. Handle invalid input for each (what if they type "abc"?)
8. Call `add_nutrition_log` with the current user's ID and the values
9. Print a confirmation message showing what was logged

---

## Step 4: Add the Menu Option

In the `main_menu()` function, update the menu:

1. Add a print statement for nutrition logging
2. Add an elif block to handle the choice
3. Update the Exit option number

**The menu should now be:**
```
1. Login/Logout
2. Log workout
3. Log nutrition
4. Exit
```

---

## Test Your Changes

1. Run `python3 client_cli.py`
2. Login (username: `tom`, password: `sixseven`)
3. Select option 3 to log nutrition
4. Enter some test values
5. Use the trainer app to verify the data was saved!

---

## Bonus Challenge

Can you add validation to make sure the percentages add up to 100?
