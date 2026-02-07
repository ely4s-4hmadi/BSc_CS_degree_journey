## Assignment 05 (prime calculator & ice-floe calculator)

### What this assignment is about
This assignment is split into two independent parts:

1. A **prime calculator** that checks whether a given integer is:
   - odd or even  
   - prime or not prime  

2. An **ice-floe calculator** that calculates:
   - the volume of two ice floes based on their dimensions  
   - the average volume of the two floes  

Both parts are implemented in a single Python file using a modular design, following the house style required for COMP101.

---

### How my solution works

#### 1. Prime Calculator
- Implemented as **one standalone function**
- Handles input, processing, and output internally
- Repeatedly:
  - asks the user for an integer  
  - determines if it is odd or even  
  - determines if it is prime or not  
- Continues running until the user chooses to exit
- Once exited, the program **automatically moves on** to the ice-floe calculator

#### 2. Ice Floe Calculator
Implemented using **three separate functions**:

- **Input function**  
  Collects length, breadth, and freeboard height for two ice floes.

- **Processing function**  
  - Calculates total thickness using the freeboard (freeboard × 9)  
  - Calculates the volume of each ice floe  
  - Computes the average volume

- **Output function**  
  Displays the individual volumes and the average volume with clear messaging.

The user can choose to run the ice-floe calculator multiple times or exit the program.

---

### Key concepts I practiced
- Procedural programming in Python  
- Writing modular code using functions  
- Separating input, processing, and output  
- Loop control and user interaction  
- Applying basic algorithms (prime checking)  
- Translating a real-world problem into structured code  

---

### Notes
This assignment helped reinforce the idea of being a **programmer, not just a coder**, by focusing on structure, clarity, and disciplined design rather than just getting an output.
