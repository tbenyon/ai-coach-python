# Amber Extension: Let Users Choose Feedback Style

**Difficulty:** Medium (Steps provided, no code examples)

Let the trainer choose whether they want friendly/supportive feedback or more direct/critical feedback.

---

## Goal

Before generating AI feedback, ask the trainer what style they want. Then modify the prompt to match their choice.

---

## Steps

### Step 1: Modify handle_generate_feedback

In `trainer_cli.py`, find `handle_generate_feedback`.

After checking that the client exists, but before generating feedback:
1. Ask the user to choose a feedback style
2. Show options like: "1. Friendly and supportive" and "2. Direct and critical"
3. Get their choice and validate it

### Step 2: Modify generate_feedback

Update the `generate_feedback` function to accept a new parameter for the style choice.

### Step 3: Update the Prompt

Inside `generate_feedback`, change the prompt text based on the style:
- If friendly: keep phrases like "encouraging", "friendly", "motivational"
- If direct: use phrases like "direct", "critical", "honest about areas needing improvement"

### Step 4: Update the Function Call

In `handle_generate_feedback`, pass the user's style choice to `generate_feedback`.

---

## Test Your Changes

1. Generate feedback with the friendly option
2. Generate feedback with the direct option
3. Compare the two - are they noticeably different?

---

## Bonus

Add a third option like "Drill sergeant mode" with a very different tone!
