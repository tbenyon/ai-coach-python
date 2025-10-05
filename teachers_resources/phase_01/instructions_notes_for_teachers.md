# PHASE 1: Teacher Notes and Answer Key

## Question Answers

### Set 1: Understanding the Basics

**1. In `cli.py`, what does the line `from userService import add_user, get_user_by_email` do?**

**Answer:** This line imports two specific functions (`add_user` and `get_user_by_email`) from the `userService.py` file so they can be used in the `cli.py` file. This allows the CLI to use functionality defined in another file.

---

**2. In `db.py`, what is the name of the database file that the code connects to?**

**Answer:** `coaching_app.db` - This is specified in the `sqlite3.connect('coaching_app.db')` line in the `get_db_connection()` function.

---

**3. In `cli.py`, what happens when the user enters "3" in the main menu?**

**Answer:** The program prints "Goodbye!" and then breaks out of the while loop, which ends the program.

---

### Set 2: Understanding Functions and Flow

**1. In `cli.py`, the `handle_add_user()` function collects user input. Why is `int(age)` used when calling `add_user()` instead of just `age`?**

**Answer:** The `input()` function always returns a string. The `int()` function converts the age string to an integer (number) so it can be stored properly in the database as a numeric value rather than text.

---

**2. In `userService.py`, what does the `cursor.execute()` function do in the `add_user()` function?**

**Answer:** The `cursor.execute()` function executes the SQL INSERT statement, which adds a new row (user) to the users table in the database with the provided name, age, and email values.

---

**3. In `cli.py`, look at the `handle_get_user()` function. How does the code access the user's name and email from the database result?**

**Answer:** The code uses dictionary-style access with column names as keys: `user['name']` and `user['email']`. This is possible because the `row_factory` is set to `sqlite3.Row` in the `get_db_connection()` function in `db.py`, which allows accessing columns by their names instead of numeric indices.

---

### Set 3: Advanced Concepts

**1. Why do you think the database connection code was moved to a separate `db.py` file instead of being repeated in `userService.py`? What are the benefits of this approach?**

**Answer:** Moving the database connection code to a separate `db.py` file follows the DRY principle (Don't Repeat Yourself) and provides several benefits:
- **Code reusability:** The `get_db_connection()` function can be used by any file that needs a database connection, not just `userService.py`
- **Easier maintenance:** If we need to change the database name or connection settings, we only need to update one place
- **Consistency:** All connections will have the same configuration (like `row_factory = sqlite3.Row`)
- **Better organization:** Database-related code is separated from business logic, making the codebase easier to understand and navigate

---

**2. In `cli.py`, the main menu uses a `while True:` loop. Explain how the program exits this infinite loop when the user selects option 3.**

**Answer:** When the user enters "3", the code executes the `elif choice == "3":` block, which contains a `break` statement. The `break` keyword immediately exits the while loop, allowing the program to continue to the end and terminate. Without the `break`, the loop would continue forever (infinite loop).

---

**3. In `userService.py`, the SQL query uses `?` placeholders (e.g., `VALUES (?, ?, ?)`). Why do you think the code uses placeholders instead of directly inserting the values into the SQL string?**

**Answer:** Using placeholders (parameterized queries) is a security best practice that:
- **Prevents SQL injection attacks:** Malicious users could insert harmful SQL code through input fields if values were directly concatenated into the SQL string
- **Handles special characters properly:** The database driver automatically escapes special characters in the input
- **Improves code readability:** The SQL structure is clearer when separated from the data values

Example of the security issue:
```python
# DANGEROUS - vulnerable to SQL injection:
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

# SAFE - using placeholders:
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
```

---

## Teaching Tips

- **Set 1** focuses on basic Python syntax and program structure - these should be relatively straightforward for students who have basic Python knowledge
- **Set 2** requires students to understand data types, function parameters, and dictionary-like access patterns - may need more explanation
- **Set 3** covers important programming concepts (code organization/DRY principle, control flow, security) - these are more conceptual and may require discussion

## Common Student Misconceptions

1. **String vs Integer:** Students may forget that `input()` returns strings and wonder why conversion is needed
2. **Row Factory:** Students may be confused about how `user['name']` works and what `sqlite3.Row` does - explain that it's like converting a tuple into a dictionary
3. **Code Reusability:** Students may not immediately see the benefit of extracting `get_db_connection()` into a separate file - emphasize the DRY principle and how it makes future changes easier
4. **Break Statement:** Students may think the program ends at the print statement, not understanding the role of `break`
5. **Database Connections:** Students may not see the importance of closing connections since the program seems to work without it
