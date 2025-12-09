# Green Extension: Validate Nutrition Percentages

**Difficulty:** Easy (Small addition)

Add validation to make sure the nutrition percentages add up to exactly 100.

---

## Background

When logging nutrition, users enter three percentages:
- Protein percentage
- Carbs percentage
- Fats percentage

These should add up to 100% - but currently there's no check for this!

---

## Task

Open `client_cli.py` and find the `handle_log_nutrition` function.

After collecting all three percentages (but before saving to the database), add a check:

```python
# Check that percentages add up to 100
total = protein_percent + carbs_percent + fats_percent
if total != 100:
    print(f"Error: Percentages must add up to 100, but yours add up to {total}")
    return
```

---

## Where to Add It

Add the check after this line:
```python
    fats_percent = int(fats_input)
except ValueError:
    ...
```

And before the line that saves to the database:
```python
success = add_nutrition_log(...)
```

---

## Test It

1. Run `client_cli.py`
2. Login and try to log nutrition
3. Enter percentages that add up to 100 (e.g., 30, 40, 30) - should work
4. Enter percentages that don't add up to 100 (e.g., 30, 30, 30) - should show error

---

## Bonus

Can you make the error message more helpful by telling the user how much they're over or under?

For example: "Percentages add up to 90. You need 10 more to reach 100."
