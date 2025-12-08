# Amber Extension: Add Limit Parameter to Queries

**Difficulty:** Medium (Steps provided, no code examples)

Currently, `get_recent_workouts` and `get_recent_nutrition_logs` return ALL records for a client. Add a `limit` parameter so users can control how many records to fetch.

---

## Goal

Modify the functions so they can be called like:
- `get_recent_workouts(client_id, limit=5)` - returns the 5 most recent workouts
- `get_recent_nutrition_logs(client_id, limit=3)` - returns the 3 most recent logs

The limit should be optional with a sensible default (e.g., 10).

---

## Steps

### Part 1: Modify the Service Functions

1. Add a `limit` parameter with a default value to `get_recent_workouts` in `trainer_service.py`

2. Update the SQL query to use `LIMIT ?` at the end

3. Add the limit value to the tuple of parameters passed to `cursor.execute()`

4. Repeat for `get_recent_nutrition_logs`

**Hint:** SQL `LIMIT` goes at the very end of the query:
```sql
SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ?
```

### Part 2: Update the CLI

1. In `handle_get_workouts`, ask the user how many workouts to display

2. Pass the limit to `get_recent_workouts`

3. Handle invalid input (what if they type "abc" instead of a number?)

4. Repeat for `handle_get_nutrition`

### Part 3: Update AI Feedback (Optional)

Consider: Should the AI feedback use a limit? What if a client has 100 workouts?

---

## Testing

1. Run the trainer app and request workouts with different limits
2. Verify you get the correct number of records
3. Test with a limit of 0 - what happens?
4. Test with a limit larger than the number of records - what happens?

---

## Questions to Consider

1. What's a sensible default limit? Why?

2. Should you validate the limit (e.g., prevent negative numbers)?

3. How does this change affect the AI feedback prompt? Is there too much data being sent?
