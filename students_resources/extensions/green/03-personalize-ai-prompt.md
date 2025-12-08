# Green Extension: Personalize the AI Prompt

**Difficulty:** Easy (Small change)

Add the client's age to the AI prompt so the feedback is more personalized.

---

## Background

Look at `handle_generate_feedback` in `trainer_cli.py`. Notice that it already fetches the client's information:

```python
client = get_client_by_id(client_id)
```

This `client` dictionary contains `age` - but we're not using it in the prompt!

---

## Task

Open `trainer_cli.py` and find the `generate_feedback` function.

Look at the prompt string. Currently it starts like:

```python
prompt = f"""You are a friendly fitness coach giving feedback to {client_name}.
```

Change it to include age. For example:

```python
prompt = f"""You are a friendly fitness coach giving feedback to {client_name}, who is {age} years old.
```

You'll also need to:
1. Add `age` as a parameter to the `generate_feedback` function
2. Pass it in when calling `generate_feedback` from `handle_generate_feedback`

---

## Test It

1. Run the trainer app
2. Generate feedback for client 1
3. The AI should now give age-appropriate advice!

---

## Experiment

Try changing how you phrase it in the prompt:
- "who is 25 years old"
- "a 25 year old client"
- "aged 25"

Does the AI respond differently?
