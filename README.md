# AI Coaching & Personal Training App

A Python teaching project designed for students aged 14-19 to learn database management and AI integration.

## Project Overview

This mini project teaches students how to build a personal training application that:
- Stores client workout data in a SQLite database
- Uses AI to generate personalized coaching feedback
- Provides practical experience with databases, APIs, and Python programming

## Learning Objectives

Students will learn:
- Python programming fundamentals
- SQLite database operations (CREATE, INSERT, SELECT, UPDATE)
- Working with external APIs (AI agent integration)
- Data validation and error handling
- Building a command-line application

## Technology Stack

- **Language**: Python 3.x
- **Database**: SQLite
- **AI Integration**: API agent for generating feedback
- **Interface**: Command-line interface (CLI)

## Features

- Client profile management
- Workout logging (exercises, sets, reps, weight)
- Progress tracking over time
- AI-generated coaching feedback based on workout data
- Performance analytics and insights

## Project Structure

```
python-ai-enrichment/
├── README.md
├── teachers_resources/  # Teaching materials for each phase
├── students_resources/  # Student materials for each phase (DISTRIBUTE TO STUDENTS)
├── experimentation/     # Testing directory (NOT for students)
└── seed_database.py     # Database setup script
```

## Teaching Approach

The project is divided into phases, with dedicated resources for teachers and students:

### For Teachers:
- **teachers_resources/**: Lesson plans, solutions, assessment criteria for each phase
- **experimentation/**: Directory for testing code before distribution (gitignored)
- Teachers should only provide students with the **students_resources/** directory

### For Students:
- **students_resources/**: Contains all materials students need for each phase
  - Instructions
  - Starter code files
  - Resources and examples
- Students will copy files from `students_resources/` to their own working directory when completing activities

## Getting Started

### Prerequisites

- Python 3.x
- pip3 (Python package manager)
- OpenAI API key

### Installation

1. Install required dependencies:

```bash
pip3 install openai python-dotenv
```

2. Create a `.env` file in your project directory and add your OpenAI API key:

```
OPEN_AI_ACCESS_KEY=your_api_key_here
```

## Usage

*To be added: How to run and use the application*

## Educational Notes

This project is designed as a structured teaching activity where students can:
1. Understand real-world application development
2. Practice problem-solving with practical constraints
3. Experience integrating multiple technologies
4. Build something tangible and useful

## Internal Tools (For Teachers)

### Generate Instruction PDFs

A utility script to convert all instruction markdown files to PDF format:

```bash
# Install dependencies
pip3 install markdown weasyprint

# Run the converter
python3 internal_tools/generate_instruction_pdfs.py
```

This will:
- Recursively search for all files starting with `instruction` and ending with `.md`
- Generate PDF versions in the same directory as the markdown files
- Provide a summary of conversion results


## Phases

### Phase 1
#### Provided Code
- CLI Main Menu
- Users Service
  - Get user
  - Add user

#### Tasks
- Run the seeder
- Run the CLI app
  - Add a user
  - View that user by email

### Phase 2
1. Add option to list all users
    - You'll want to add a new method to userService.py to get all users
    - Then add a new option to the CLI to call that method and display the results




### Phase Workouts
#### Provided Functionality
- Log a workout (always the same 3 exercise hard coded)
- Get AI feedback on the workouts

#### Tasks
- Write a tool to list all workouts

- Extensions
  - Get AI feedback on the last 3 workouts
  - Dates
    - Start storing dates for workouts
    - Allow users to log for different dates
    - 
      - Allo
      - 