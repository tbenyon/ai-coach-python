# Red Extension: Date Range Filtering for Workouts

**Difficulty:** Hard (Steps provided, figure out the code yourself)

Add the ability to filter workouts by date range in the trainer app.

---

## Goal

When a trainer selects "Get recent workouts", they should be able to optionally filter by date range. For example, only show workouts from the last week.

---

## Requirements

1. Ask the user if they want to filter by date
2. If yes, ask for a start date and end date (format: YYYY-MM-DD)
3. Only return workouts within that date range
4. Handle invalid date inputs (show an error and ask again, or skip filtering)
5. If they don't want to filter, show all workouts as normal

---

## Steps

### Step 1: Modify the Service Function

Update `get_recent_workouts` in `trainer_service.py` to accept optional `start_date` and `end_date` parameters.

- These should have default values of `None`
- If both are `None`, return all workouts (current behaviour)
- If dates are provided, add a WHERE clause to filter by `date_time`

**Hint:** The dates in the database are stored as text in format "YYYY-MM-DD HH:MM:SS". SQL can compare date strings if they're in the right format.

### Step 2: Modify the Handler Function

Update `handle_get_workouts` in `trainer_cli.py`:

1. After getting the client ID, ask "Do you want to filter by date? (y/n)"
2. If yes, ask for the start date
3. Ask for the end date
4. Validate the dates are in the correct format
5. Pass the dates to `get_recent_workouts`

### Step 3: Handle Edge Cases

Think about:
- What if they enter an invalid date format?
- What if the start date is after the end date?
- What if no workouts match the date range?

---

## Testing

1. Run the trainer app
2. Get workouts for client 1 with no filter - should show all
3. Get workouts with a date range that includes some workouts
4. Get workouts with a date range that includes no workouts
5. Try entering an invalid date - what happens?

---

## Bonus

- Add preset options like "Last 7 days" or "Last 30 days"
- Show a message like "Found 3 workouts between 2024-12-01 and 2024-12-07"
