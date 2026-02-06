# Week 02 – Assignment 02 (Lunar Rover Navigation)

This assignment builds on the basics from the first week and introduces **selection (if–else)** alongside sequence. The goal was to simulate the movement of a rover on the Moon and determine whether it can reach its target destination based on battery constraints.

---

## Task Summary
The program simulates a rover travelling at a fixed speed and battery usage rate. The user provides:
- An angle of travel (0–90 degrees)
- A time of travel in seconds

Using these inputs, the program calculates the rover’s final position and battery status, then determines whether:
- The destination is reached
- There is enough battery to return
- The rover must wait to recharge
- The battery runs out before reaching the destination

---

## My Approach
I followed a clear, step-by-step design:
1. Read the input angle and travel time
2. Convert the angle from degrees to radians using the `math` library
3. Calculate total distance travelled
4. Compute horizontal and vertical movement using trigonometric functions
5. Calculate battery usage and remaining battery
6. Use selection statements to determine the rover’s final status

The program outputs both the **inputs (echoed back)** and the **results**, making it easy to follow the rover’s situation.

---

## Concepts Used
- Sequence and selection constructs
- User input and numeric calculations
- Importing and using the `math` module
- Trigonometry (`sin`, `cos`, degree-to-radian conversion)
- Conditional logic for decision-making
- Output formatting with f-strings
- Inline comments and structured testing

---

## Testing
A detailed **test table** is included at the end of the file using triple-quoted comments.  
Multiple scenarios were tested, including:
- Successful destination with enough battery to return
- Destination reached but insufficient battery for return
- Battery depletion before reaching the destination
- Edge cases such as angles of 0 and 90 degrees

All test cases produced the expected results.

---

## Personal Notes
This assignment helped me understand how **decision-making logic** affects program flow. It also reinforced the importance of clear output and testing when simulating real-world systems, even with simple control structures.
