# Red Extension: Add a New Exercise Type

**Difficulty:** Hard (Minimal guidance)

Add a new exercise metric to the workout tracking system, such as `squats_count` or `plank_seconds`.

---

## Requirements

1. Add a new column to the `workout_log` table
2. Update the database seeder to include sample data for the new field
3. Update the service functions to include the new field
4. Update both CLIs to input/display the new field
5. Update the AI prompt to mention the new exercise type

---

## Hints

- You'll need to modify `db.py` to add the column
- Think about whether existing data should have a default value
- The SQL `ALTER TABLE` command can add columns to existing tables
- Consider: Is your new field required or optional?

---

## Bonus

Add multiple new exercise types and let users choose which ones to log.
