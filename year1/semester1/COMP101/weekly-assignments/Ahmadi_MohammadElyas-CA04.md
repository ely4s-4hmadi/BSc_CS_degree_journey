# Assignment 04 (Student Grading System)

This assignment focused on using **iteration, nested selection, and input validation** to process data for an unknown number of students. The goal was to calculate final grades based on coursework and test marks while applying late submission penalties.

---

## Task Summary
The program processes student submissions one by one. For each student, it:
- Automatically generates a student ID
- Accepts two grades:
  - Code grade (0–100)
  - Test grade (0–100)
- Accepts the number of days late (0–2)
- Calculates:
  - Raw grade (average of the two grades)
  - Final grade after late penalties
- Ensures the final grade never goes below zero
- Repeats for as many students as required

All inputs must be validated before processing.

---

## My Approach
I designed the program using a **while loop** to allow repeated processing of students. Inside this loop:
1. A student ID is auto-generated
2. A **for loop** is used to collect the two grades in a controlled way
3. Input validation ensures grades are integers within valid ranges
4. Late submission days are validated separately
5. The raw grade is calculated as an average
6. Late penalties are applied and the final grade is adjusted if needed
7. All relevant information is echoed clearly to the screen
8. The user is asked whether to process another student

The program degrades gracefully and continues running until the user chooses to stop.

---

## Concepts Used
- Sequence, selection, and iteration
- Nested loops (`while` inside `for`)
- Input validation using loops and conditions
- Arithmetic calculations and averaging
- Auto-generated identifiers
- Clear, structured output formatting
- Defensive programming (handling invalid input)

---

## Testing
The program was tested with:
- Valid and invalid grade inputs
- Boundary values (0 and 100)
- Different late submission scenarios (0, 1, and 2 days)
- Multiple students processed in one run
- Program termination using user input

All scenarios produced the expected results.

---

## Personal Notes
This assignment brought together everything covered so far in COMP101. It improved my confidence with **loops, validation, and program flow**, and showed how structured programming can handle real-world style problems without forcing the program to exit unexpectedly.
