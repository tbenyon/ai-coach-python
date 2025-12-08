# Phase 3: Adding Nutrition to AI Feedback

In this phase, you'll enhance the AI feedback feature to include nutrition data, giving clients more comprehensive coaching advice.

---

## Task 1: Update the generate_feedback Function

Open `trainer_cli.py` and find the `generate_feedback` function.

**Current version:**
```python
def generate_feedback(client_name, workouts_json):
```

**Change it to accept nutrition data:**
```python
def generate_feedback(client_name, workouts_json, nutrition_json):
```

---

## Task 2: Update the Docstring

Update the docstring to document the new parameter:

```python
def generate_feedback(client_name, workouts_json, nutrition_json):
    """
    Build a prompt and call the AI to generate feedback.

    Args:
        client_name: The client's first name
        workouts_json: JSON string of recent workouts
        nutrition_json: JSON string of recent nutrition logs

    Returns:
        The AI's feedback as a string, or None if there was an error
    """
```

---

## Task 3: Update the AI Prompt

Find the prompt string inside `generate_feedback` and update it to include nutrition data:

```python
    # Build the prompt for the AI
    prompt = f"""You are a friendly fitness coach giving feedback to {client_name}.

Here are their recent workouts:
{workouts_json}

Here are their recent nutrition logs:
{nutrition_json}

Please provide brief, encouraging feedback on their progress.
Comment on their workout consistency and suggest improvements.
Also review their nutrition and suggest any changes.
Keep the feedback friendly and motivational.
Keep it under 150 words."""
```

---

## Task 4: Update handle_generate_feedback

Find the `handle_generate_feedback` function and update it to fetch and pass nutrition data.

**Find this section:**
```python
    # Get recent workouts as JSON
    workouts_json = json.dumps(get_recent_workouts(client_id), indent=2)

    # Generate feedback using AI
    feedback = generate_feedback(client['first_name'], workouts_json)
```

**Change it to:**
```python
    # Get recent workouts and nutrition as JSON
    workouts_json = json.dumps(get_recent_workouts(client_id), indent=2)
    nutrition_json = json.dumps(get_recent_nutrition_logs(client_id), indent=2)

    # Generate feedback using AI
    feedback = generate_feedback(client['first_name'], workouts_json, nutrition_json)
```

---

## Test Your Changes

1. Run `python3 trainer_cli.py`
2. Select the AI feedback option
3. Enter client ID: 1
4. The AI should now give feedback on BOTH workouts AND nutrition!

---

## Questions

1. Why do we use `json.dumps()` to convert the data before sending it to the AI?

2. What would happen if we passed the raw list of dictionaries instead of a JSON string?

3. Look at the prompt carefully. How does changing the prompt text affect the AI's response?

4. Try modifying the prompt to ask for different kinds of feedback. What changes do you notice?
