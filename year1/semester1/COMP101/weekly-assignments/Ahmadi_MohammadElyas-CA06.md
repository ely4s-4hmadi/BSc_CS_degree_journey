# Assignment 06 (The Galactic Saga)

### What this assignment is about
[cite_start]This project was all about practicing **list processing** and **string manipulation** in Python[cite: 2]. [cite_start]The goal was to take a list of real-world actor names and automatically generate "Alien" stage names for a film's credits using specific algorithms[cite: 2].

[cite_start]I also tackled an optional enhancement: solving a hidden anagram within the generated names to reveal the "Secret Star" of the film[cite: 1, 2].

---

### How my solution works

#### 1. Alien Name Generator
[cite_start]I built a system that takes two lists—given names and family names—and processes them through a modular pipeline[cite: 1, 2]:
* [cite_start]**The Core Algorithm**: It extracts the first two characters of the family name and the first two characters of the given name[cite: 1, 2].
* [cite_start]**Concatenation**: It joins these segments to create a unique, 4-letter alien name (for example, "raja desu" becomes "Dera")[cite: 1, 2].
* [cite_start]**Modular Design**: Each step is handled by a dedicated function to keep the logic clean and maintainable[cite: 1, 2].

#### 2. The Anagram & Star Reveal
[cite_start]The most interesting part of this assignment was the "Hidden Star" logic. Here’s how I handled it:
* [cite_start]**Identity Discovery**: I wrote a function to pull specific two-letter segments from the standard alien names.
* [cite_start]**Anagram Solving**: By rearranging those segments in a specific order, I derived the identity of the hidden star (**Johnny Depp**).
* [cite_start]**Advanced Algorithm**: For the star's alien name, I used a more complex rule: combining the first two letters of the family name with the **first three letters of the given name—reversed**[cite: 1, 2].

#### 3. Enhanced Credit Display
[cite_start]Instead of a simple list, I formatted the final output to look like an actual film credit roll. [cite_start]I used string formatting to align columns for "Supporting Actor" and "Alien Character" so the output looks professional in the terminal.

---

### Key concepts I practiced
* [cite_start]**List Iteration**: Using loops to process multiple datasets simultaneously[cite: 1, 2].
* [cite_start]**String Slicing**: Mastering the `[0:2]` and `[0:3]` syntax to pull exactly the characters I needed.
* [cite_start]**Reversing Logic**: I implemented a manual loop to reverse strings, which helped me understand how characters are manipulated step-by-step[cite: 1, 2].
* [cite_start]**Modular Programming**: Ensuring the program is fully modularized with argument and parameter passing between functions[cite: 2].

---

### Notes
This assignment really emphasized the importance of being a **programmer, not just a coder**. [cite_start]By breaking the "Star Identity" and "Alien Name" logic into separate, discreet functions, the code became much easier to manage[cite: 1, 2]. It’s a fun script that follows structured design principles rather than just focusing on the final output.
