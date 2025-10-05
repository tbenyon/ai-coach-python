# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python teaching project** for students aged 14-19 to learn database management and AI integration. The codebase is structured to support phase-based learning with separate materials for teachers and students.

**Critical:** This is educational software. Code should be beginner-friendly, well-commented, and demonstrate best practices suitable for students learning Python.

## Repository Architecture

The repository uses a **dual-track structure** separating teacher and student materials:

- **`teachers_resources/`**: Complete solutions, answer keys, and lesson plans for each phase. Contains `instructions_notes_for_teachers.md` files with answers to student questions.
- **`students_resources/`**: Starter code, instructions, and exercises for students. Students copy files from here to their working directory.
- **`experimentation/`**: Testing directory (gitignored) for validating code before distribution to students.
- **`internal_tools/`**: Utility scripts for course management (e.g., PDF generation).

**Phase structure**: Each phase (phase_01, phase_02, etc.) contains an `example_code/` directory with working implementations and an `instructions.md` file with tasks and questions.

## Code Architecture Patterns

### Database Layer
All phases use a standardized database connection pattern:

```python
# db.py - Centralized connection management
def get_db_connection():
    conn = sqlite3.connect('coaching_app.db')
    conn.row_factory = sqlite3.Row  # Enable named column access
    return conn
```

**Important**: Always use `sqlite3.Row` for row factory to enable dictionary-style column access (`user['name']` instead of `user[0]`). This is a teaching pattern to demonstrate readable code.

### Service Layer Pattern
Business logic is separated into service files (e.g., `userService.py`, `ai_service.py`) that:
- Import `get_db_connection()` from `db.py`
- Handle database operations with proper connection cleanup
- Use parameterized queries (`?` placeholders) for SQL injection prevention

### CLI Pattern
Command-line interfaces follow a consistent structure:
- Menu-driven with numbered options
- Handler functions for each operation (e.g., `handle_add_user()`)
- Input validation with user-friendly error messages
- Uses `while True` loop with `break` for exit

### AI Integration (Phase 2+)
OpenAI integration pattern:
- API key stored in `.env` file (`OPEN_AI_ACCESS_KEY`)
- `ai_service.py` validates key presence and shows clear error if missing
- Uses `python-dotenv` for environment variable management

## Common Development Commands

### Setup for Phase 1
```bash
# Run database seeder
python3 students_resources/phase_01/example_code/seed_database.py

# Run CLI application
python3 students_resources/phase_01/example_code/cli.py
```

### Setup for Phase 2 (AI features)
```bash
# Navigate to phase 2 example code
cd teachers_resources/phase_02/example_code

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install openai python-dotenv

# Create .env file with OpenAI key
echo "OPEN_AI_ACCESS_KEY=your_key_here" > .env

# Run application
python3 cli.py
```

### Internal Tools
```bash
# Generate PDFs from instruction markdown files
pip3 install markdown weasyprint
python3 internal_tools/generate_instruction_pdfs.py
```

## Development Guidelines

### When Creating Student Materials
1. **File naming**: Use snake_case (e.g., `user_service.py`, not `userService.py`) for new files. Existing files use camelCase for historical reasons.
2. **Comments**: Include docstrings and inline comments explaining concepts for beginners.
3. **Error handling**: Always show user-friendly error messages, not raw exceptions.
4. **Questions**: When adding questions to `instructions.md`, also add answers to `teachers_resources/phase_XX/instructions_notes_for_teachers.md`.

### When Modifying Database Code
- Always close database connections with `conn.close()`
- Use `conn.commit()` for INSERT/UPDATE/DELETE operations
- Maintain the `db.py` connection pattern for consistency across phases

### When Adding New Phases
1. Create parallel directories in `teachers_resources/` and `students_resources/`
2. Include `example_code/` subdirectory with working implementation
3. Create `instructions.md` (students) and `instructions_notes_for_teachers.md` (teachers)
4. Follow the existing pattern: db.py → service files → cli.py

## Environment Configuration

- `.env` files are gitignored and must contain `OPEN_AI_ACCESS_KEY` for AI features
- Virtual environments (`venv/`) are gitignored
- Database files (`coaching_app.db`) in `students_resources/` are gitignored
- `__pycache__/` and `*.pyc` files are gitignored

## Key Dependencies

- **Python 3.x**: Core language
- **sqlite3**: Built-in database (no installation needed)
- **openai**: For AI feedback generation (Phase 2+)
- **python-dotenv**: Environment variable management
- **markdown + weasyprint**: PDF generation (internal tools only)
