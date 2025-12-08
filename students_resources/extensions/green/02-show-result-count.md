# Green Extension: Show Result Count

**Difficulty:** Easy (Code provided)

Show how many results were found before displaying the data.

---

## Task 1: Add Count to Workouts

Open `trainer_cli.py` and find the `handle_get_workouts` function.

Find these lines near the end:

```python
workouts = get_recent_workouts(client_id)
print(json.dumps(workouts, indent=2))
```

Change them to:

```python
workouts = get_recent_workouts(client_id)
print(f"Found {len(workouts)} workout(s):")
print(json.dumps(workouts, indent=2))
```

### Test It

1. Run the trainer app
2. Get workouts for client 1
3. You should see "Found 5 workout(s):" before the data

---

## Task 2: Do the Same for Nutrition

Now apply the same pattern to `handle_get_nutrition`.

Find where it prints the nutrition data and add a count message before it.

### Test It

1. Get nutrition logs for client 1
2. You should see "Found X nutrition log(s):" before the data
