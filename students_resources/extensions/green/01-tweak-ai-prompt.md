# Green Extension: Tweak the AI Prompt

**Difficulty:** Easy (Quick change)

Make the AI give more critical feedback instead of just being encouraging.

---

## Task

1. Open `trainer_cli.py`
2. Find the `generate_feedback` function
3. Look at the prompt text that gets sent to the AI
4. Change the prompt to ask for more direct, critical feedback

For example, you could change:
- "friendly and motivational" to "direct and critical"
- Add a line like "Don't be afraid to point out areas that need improvement"
- Ask it to "be honest about what they're doing wrong"

---

## Test Your Changes

1. Run the trainer app
2. Generate AI feedback for client 1
3. Compare the new feedback to what you got before - is it more critical?

---

## Experiment

Try different prompt changes and see how the AI responds differently. What happens if you ask it to be:
- Very strict?
- Like a drill sergeant?
- More focused on nutrition vs workouts?
