# Troubleshooting

If something goes wrong while you're running the app, look for the error message below and follow the matching fix. If you don't see your error here, ask your teacher.

---

## `sqlite3.OperationalError: no such column: <name>`

**Example you might see:**

```
sqlite3.OperationalError: no such column: comment
```

**What it means:** Your `coaching_app.db` file was created with an older version of the database. The code has since been updated to use a new column (in the example above, `comment`), but your database doesn't know about it yet.

This usually happens when:
- You were given a pre-seeded database in a zip file that's a bit out of date
- You ran `db.py` once, then the schema in `db.py` was updated later
- You completed an extension that added a column but didn't re-seed

**How to fix it:**

1. Delete the existing database file:

   On Mac/Linux:
   ```
   rm coaching_app.db
   ```

   On Windows:
   ```
   del coaching_app.db
   ```

2. Re-create the database by running the seeder:
   ```
   python3 db.py
   ```

3. Run your app again — the error should be gone.

> ⚠ Re-seeding will wipe any workouts or nutrition logs you've added yourself. The sample data for Tom will come back.

---

## `sqlite3.OperationalError: no such table: <name>`

**Example you might see:**

```
sqlite3.OperationalError: no such table: clients
```

**What it means:** The database file exists but doesn't have the tables yet. You probably haven't run the seeder.

**How to fix it:** Run the seeder:

```
python3 db.py
```

---

## `ModuleNotFoundError: No module named 'openai'` (or `'dotenv'`)

**What it means:** Python doesn't have the libraries the AI feature needs.

**How to fix it:** Install them:

```
pip install openai python-dotenv
```

(If `pip` doesn't work, try `pip3`.)

---

## "OPENAI API KEY NOT FOUND" message when you generate AI feedback

**What it means:** The app can't find your OpenAI key.

**How to fix it:**

1. Open the `.env` file in your `example_code` folder
2. Replace `your_api_key_here` with the API key your teacher gave you
3. Save the file and run the app again

If there's no `.env` file at all, run `python3 db.py` once — it'll create the template for you.
