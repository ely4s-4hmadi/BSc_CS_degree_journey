# Assignment 03 (Cat Age Calculator)

This assignment focused on using **nested selection (if / elif / else)** to control program flow based on user input. The task was to calculate a cat’s age in **human years** for specific life stages using a menu-driven program.

---

## Task Summary
The program presents a main menu where the user can:
- Calculate the human-equivalent age for a **Junior cat** (in months)
- Calculate the human-equivalent age for a **Prime cat** (in years)
- Exit the program

Based on the selected option, the program prompts for a specific age, applies the correct formula, and displays the result.

---

## My Approach
I structured the program using a clear **menu-based design**:
1. Display the main menu
2. Read the user’s option and normalise it using `.lower()`
3. Use selection and **nested selection** to handle:
   - Junior cat age calculation
   - Prime cat age calculation
   - Exit option
   - Invalid menu choices
4. Validate that the entered age matches the allowed values
5. Apply the correct formula and display the result
6. Exit the program with a clear message

The program runs once per execution, as required.

---

## Concepts Used
- Sequence and nested selection constructs
- Menu-driven program design
- User input and type conversion
- Validation using conditional logic
- Arithmetic calculations
- Clear output formatting
- Inline comments and structured testing

---

## Testing
A detailed **test table** is included at the end of the file using triple-quoted comments.  
The tests cover:
- Valid Junior and Prime age boundaries
- Lower and upper boundary cases
- Invalid ages and invalid menu options
- Case-insensitive menu input
- Normal program exit

All expected outputs matched the actual results.

---

## Personal Notes
This assignment helped me practise **structured decision-making** using nested selection. It reinforced how important clear program flow and thorough testing are, even in relatively small programs.
