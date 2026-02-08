# Assignment 06 (The Galactic Saga)

### What this assignment is about
This project was all about practicing **list processing** and **string manipulation** in Python. The goal was to take a list of real-world actor names and automatically generate "Alien" stage names for a film's credits using specific algorithms.

I also tackled an optional enhancement: solving a hidden anagram within the generated names to reveal the "Secret Star" of the film.

---

### How my solution works

#### 1. Alien Name Generator
I built a system that takes two lists—given names and family names—and processes them through a modular pipeline:
* **The Core Algorithm**: It extracts the first two characters of the family name and the first two characters of the given nameite.
* **Concatenation**: It joins these segments to create a unique, 4-letter alien name (for example, "raja desu" becomes "Dera").
* **Modular Design**: Each step is handled by a dedicated function to keep the logic clean and maintainable.

#### 2. The Anagram & Star Reveal
The most interesting part of this assignment was the "Hidden Star" logic. Here’s how I handled it:
* **Identity Discovery**: I wrote a function to pull specific two-letter segments from the standard alien names.
* **Anagram Solving**: By rearranging those segments in a specific order, I derived the identity of the hidden star (**Johnny Depp**).
* **Advanced Algorithm**: For the star's alien name, I used a more complex rule: combining the first two letters of the family name with the **first three letters of the given name—reversed**.

#### 3. Enhanced Credit Display
Instead of a simple list, I formatted the final output to look like an actual film credit roll. I used string formatting to align columns for "Supporting Actor" and "Alien Character" so the output looks professional in the terminal.

---

### Key concepts I practiced
* **List Iteration**: Using loops to process multiple datasets simultaneously.
* **String Slicing**: Mastering the `[0:2]` and `[0:3]` syntax to pull exactly the characters I needed.
* **Reversing Logic**: I implemented a manual loop to reverse strings, which helped me understand how characters are manipulated step-by-step.
* **Modular Programming**: Ensuring the program is fully modularized with argument and parameter passing between functions.

---

### Personal Notes
This assignment really emphasized the importance of being a **programmer, not just a coder**. By breaking the "Star Identity" and "Alien Name" logic into separate, discreet functions, the code became much easier to manage. It’s a fun script that follows structured design principles rather than just focusing on the final output.
