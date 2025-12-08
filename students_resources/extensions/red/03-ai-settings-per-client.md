# Red Extension: AI Settings Per Client

**Difficulty:** Hard (Design and implement yourself)

Create a system that lets trainers store different AI feedback settings for each client.

---

## Goal

Different clients might need different coaching styles. Create a way for trainers to configure how AI feedback is generated for each client.

---

## Requirements

### Database

Create a new `ai_settings` table that stores:
- `client_id` - which client these settings are for
- `feedback_length` - short, medium, or long
- `include_workouts` - whether to include workout data (yes/no)
- `include_nutrition` - whether to include nutrition data (yes/no)
- `writing_style` - e.g., "friendly", "direct", "motivational", "drill sergeant"
- `custom_notes` - free text that gets appended to the prompt (e.g., "This client is training for a marathon" or "Focus on protein intake")

### Service Functions

Create functions to:
- Get settings for a client
- Save/update settings for a client
- Handle clients that don't have settings yet (use sensible defaults)

### CLI Changes

Add menu options to:
- View current AI settings for a client
- Edit AI settings for a client

### Feedback Generation

Modify `generate_feedback` to:
- Load the client's AI settings
- Adjust the prompt based on feedback_length
- Only include workout/nutrition data if the settings say to
- Use the writing_style in the prompt
- Append any custom_notes to the prompt

---

## Things to Think About

- What should happen if a client has no settings saved yet?
- How will you handle the different feedback lengths in the prompt?
- Where should the custom_notes appear in the prompt?
- Should there be a way to reset settings to defaults?

---

## Suggested Steps

1. Add the table creation to `db.py`
2. Add some sample settings in the seeder
3. Create service functions for getting/saving settings
4. Add the menu options to view and edit settings
5. Modify the feedback generation to use the settings
6. Test with different configurations

---

## Bonus Ideas

- Add a "preview prompt" option that shows what the AI prompt will look like without actually calling the AI
- Let trainers save "setting templates" they can apply to multiple clients
- Add a setting for preferred AI response language
