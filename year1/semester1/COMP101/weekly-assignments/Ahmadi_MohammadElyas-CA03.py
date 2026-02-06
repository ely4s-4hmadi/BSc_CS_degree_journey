# Ahmadi_MohammadElyas  201792013  October2025  CA03.py
# Program to calculate a cat's age in human years    (only for Junior and Prime cats)

# showing the main menu to the user
print("Main Menu")
print("A. Junior Cat age in months 8,12,18,24")
print("B. Prime Cat age in years 3,4,5,6")
print("X. Exit Program")

# get user input and convert it to lowercase for consistency
option = input("Enter your option: ").lower()

#junior Cat age calculation
if option == "a":
    age = int(input("Enter the cat’s age in months (8, 12, 18, 24): "))

    #validate the entered age for Junior category
    if age == 8 or age == 12 or age == 18 or age == 24:
        print(f"The cat’s age in human years is approximately {age+3}.") #Formula for Junior cats: human age = the cat's age plus 3
        print("Thanks for using the Cat's_age_in_human_years_calculator program. ")
    else:
        print("invalid age entered.")

#prime Cat age calculation
elif option == "b":
    age = int(input("Enter the cat’s age in years (3, 4, 5, 6): "))

    #validate the entered age for Prime category
    if age in range(3, 7):
        print(f"The cat’s age in human years is approximately {4*age +16}.")  #Formula for Prime cats: human age = four times the cat's age plus 16
        print("Thanks for using the Cat's_age_in_human_years_calculator program. ")
    else:
        print("invalid value entered.")

#exit program option
elif option == "x":
    print("Exiting program. Goodbye!")

#handle invalid menu options
else:
    print("Invalid option entered! Enter either A, B or X.")


"""
Test Table:
Option | Input (Cat’s Age) |          Expected Output            |           Actual Output             |         Comment
----------------------------------------------------------------------------------------------------------------------------------
   A   |     8             | The cat’s age in human years is 11. | The cat’s age in human years is 11. | Okay - lower boundary
   A   |    12             | The cat’s age in human years is 15. | The cat’s age in human years is 15. | Okay
   A   |    18             | The cat’s age in human years is 21. | The cat’s age in human years is 21. | Okay
   A   |    24             | The cat’s age in human years is 27. | The cat’s age in human years is 27. | Okay - upper boundary
   a   |    12             | The cat’s age in human years is 15. | The cat’s age in human years is 15. | Okay 
   A   |     6             | Invalid age entered.                | Invalid age entered.                | Out of range
   A   |    10             | Invalid age entered.                | Invalid age entered.                | Out of range
   A   |    25             | Invalid age entered.                | Invalid age entered.                | Out of range
   A   |     0             | Invalid age entered.                | Invalid age entered.                | Out of range
   A   |    20.5           | Invalid age entered.                | error                               | Input must be an integer
   A   |    -1             | Invalid age entered.                | Invalid age entered.                | Out of range
-----------------------------------------------------------------------------------------------------------------------------------
   B   |     3             | The cat’s age in human years is 28. | The cat’s age in human years is 28. | Okay - lower boundary
   B   |     4             | The cat’s age in human years is 32. | The cat’s age in human years is 32. | Okay
   B   |     5             | The cat’s age in human years is 36. | The cat’s age in human years is 36. | Okay
   B   |     6             | The cat’s age in human years is 40. | The cat’s age in human years is 40. | Okay - upper boundary
   b   |     5             | The cat’s age in human years is 36. | The cat’s age in human years is 36. | Okay
   B   |     2             | Invalid age entered.                | Invalid age entered.                | Out of range
   B   |     4.5           | Invalid age entered.                | error                               | Input must be an integer
   B   |     0             | Invalid age entered.                | Invalid age entered.                | Out of range
   B   |     7             | Invalid age entered.                | Invalid age entered.                | Out of range
   B   |    -1             | Invalid age entered.                | Invalid age entered.                | Out of range
-------------------------------------------------------------------------------------------------------------------------------------------
   X   |     —             | Exiting program. Goodbye!           | Exiting program. Goodbye!           | Exit case - normal termination
   x   |     —             | Exiting program. Goodbye!           | Exiting program. Goodbye!           | Exit case - normal termination
--------------------------------------------------------------------------------------------------------------------------------------------
   Z   |     —             | Invalid option entered!             | Invalid option entered! Enter either A, B or X. | Invalid option test (nonexistent choice)
   1   |     —             | Invalid option entered!             | Invalid option entered! Enter either A, B or X. | Invalid option test (numeric input)
----------------------------------------------------------------------------------------------------------------------------------------------
"""
