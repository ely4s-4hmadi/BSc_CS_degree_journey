# Assignment 07 (Aircraft Revenue Simulator)

### What this assignment is about
This project is a commercial trial tool designed for airline management to perform **break-even analysis** on a new aircraft. The goal was to build a modular program that simulates flight revenue under two different scenarios:
1.  **Full Load**: Every seat is sold.
2.  **Part Load**: Seats are sold randomly using a generator.

The program takes user inputs for seat and lunch prices and generates a detailed "Dashboard" showing exactly how many flights it takes to cover the company's fixed costs.

---

### How my solution works

#### 1. The Seating Logic
I represented the first-class cabin as a **2D list (4 rows x 5 columns)**. 
* **Window vs. Aisle**: I wrote a function to identify window seats (the first and last rows), which cost twice as much as aisle seats.
* **Dynamic Revenue**: The simulator calculates revenue for each seat based on its position, then adds optional lunch income for every passenger on board.

#### 2. Break-Even Analysis
The core of the program is the break-even algorithm:
* **Formula**: I used the formula `Flights = Fixed Cost / Total Revenue`.
* **Fixed Costs**: The cost per flight is set as a global constant of **$15,000**.
* **Precision**: Since you can't fly a fraction of a flight, I used the `math.ceil()` function to always round the result up to the next whole number.

#### 3. Management Dashboard
Instead of just printing a list of numbers, the program outputs a user-friendly dashboard:
* **Visual Map**: For both scenarios, it prints a 2D seating plan (using `1` for sold and `0` for empty) so management can visualize the cabin load.
* **Financial Breakdown**: It displays window/aisle revenue splits, individual row totals, and the final break-even target.

---

### Key concepts I practiced
* **2D List Manipulation**: Managing a grid-like structure to represent physical seating.
* **Global Constants**: Using `FLIGHT_COST_TO_COMPANY` to handle fixed business data.
* **Math and Random Libraries**: Implementing `random.randint()` for simulation and `math.ceil()` for business logic.
* **Zip Function**: Using `zip()` to iterate through the seating layout and the "sold" flags simultaneously for efficient processing.
* **Advanced Formatting**: Creating a clean terminal interface using f-strings and alignment modifiers for a "dashboard" feel.

---

### Personal Notes
This project reinforced the importance of **modular design**. By separating the seating layout, the revenue math, and the display logic into different functions, I was able to run the same analysis for both a full flight and a random one without rewriting any code. It really shows how programming can be used to solve real-world financial problems.
