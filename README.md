# AI Coaching & Personal Training App

A Python teaching project designed for students aged 14-19 to learn database management and AI integration.

## Project Overview

This project teaches students how to build a personal training application that:
- Stores client workout and nutrition data in a SQLite database
- Uses AI to generate personalized coaching feedback
- Provides practical experience with databases, APIs, and Python programming

## Learning Objectives

Students will learn:
- Python programming fundamentals
- SQLite database operations (CREATE, INSERT, SELECT)
- Working with external APIs (OpenAI integration)
- Building a command-line application
- Prompt engineering for AI responses

## Technology Stack

- **Language**: Python 3.x (no pip installs required - uses built-in libraries only)
- **Database**: SQLite (built into Python)
- **AI Integration**: OpenAI API via urllib (built into Python)
- **Interface**: Command-line interface (CLI)

## Project Structure

```
python-ai-enrichment/
├── README.md
├── full-example-project/     # Complete working example (teacher reference)
└── students_resources/       # DISTRIBUTE TO STUDENTS
    ├── example_code/         # Starter code (copy this folder)
    ├── phase_01.md           # Setup and enable AI feedback
    ├── phase_02.md           # Add nutrition tracking (trainer)
    ├── phase_03.md           # Add nutrition to AI feedback
    ├── phase_04.md           # Extension tasks overview
    └── extensions/           # Additional challenges
        ├── green/            # Easy (guided)
        ├── amber/            # Medium (steps only)
        └── red/              # Hard (minimal guidance)
```

## Phased Learning Approach

Students progress through phases, building features incrementally:

### Phase 1: Getting Started
- Copy and run the starter code
- Explore the database and CLI apps
- Enable the AI feedback feature (uncomment code)

### Phase 2: Add Nutrition Tracking
- Add `get_recent_nutrition_logs` function to trainer service
- Add menu option to view nutrition logs
- Follow the workout pattern as a guide

### Phase 3: Enhance AI Feedback
- Modify the AI prompt to include nutrition data
- Pass nutrition data to the feedback generator

### Phase 4: Extensions
Choose from additional challenges at different difficulty levels:

| Difficulty | Description | Examples |
|------------|-------------|----------|
| **Green** | Guided with code snippets | Tweak AI prompt, show result counts, add age to prompt |
| **Amber** | Steps provided, no code | Add limit parameter, nutrition logging for client, feedback style choice |
| **Red** | Minimal guidance | Add new exercise type, date filtering, AI settings per client |

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key (provided by teacher)

### For Students

1. Copy the `students_resources` folder to your machine
2. Start with `phase_01.md` and follow the instructions
3. Progress through phases at your own pace
4. Try extension tasks when you finish the main phases

### For Teachers

- The `full-example-project/` folder contains the complete working implementation
- API keys should be distributed to students separately
- PDF versions of instructions can be generated (see Internal Tools below)

## Internal Tools

### Generate Instruction PDFs

Convert all markdown files in students_resources to PDF format.

This requires installing some Python packages. We use a "virtual environment" (venv) to keep these packages separate from your system Python:

```bash
# Create a virtual environment (only need to do this once)
python3 -m venv venv

# Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install the required packages (only need to do this once)
pip install markdown weasyprint

# Run the converter
python3 internal_tools/generate_instruction_pdfs.py
```

**Note:** Each time you open a new terminal to run the converter, you'll need to activate the venv again with `source venv/bin/activate` before running the script.

This will generate PDF versions alongside each markdown file in students_resources.
