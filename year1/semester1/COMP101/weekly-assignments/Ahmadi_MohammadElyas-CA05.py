# Ahmadi_MohammadElyas   201792013   November2025   CA05.py
# Calculates if an integer is odd/even and prime/not, then calculates the volume and average volume of two ice floes.

# --- Prime Calculator Function ---
def prime_calculator_function(): # This function is a single stand-alone function that handles I/P, processing, and O/P.
    # asking the user to run the prime calculator. If run, it repeatedly takes an integer input, checks if it's odd/even and prime/not, and outputs the result until the user chooses to exit.

    run_prime = input("Do you want to run the prime calculator function? (Y/N): ").upper()

    while run_prime == 'Y':
        number = int(input("Please enter an integer to check if it is even/odd and prime/not: "))

        # Processing: Odd or Even
        if number%2 == 0:
            odd_even = "even"
        else:
            odd_even = "odd"

        # Processing: Prime or Not Prime
        is_prime = True

        # 0 and 1 are not prime
        if number <= 1:
            is_prime = False
        # 2 is the only even prime number
        elif number == 2:
            is_prime = True
        # Check for factors from 2 up to the square root of the number

        # We start checking from 2 up to the (number-1)
        else:
            i = 2
            while i < number:
                if number % i == 0:
                    is_prime = False
                # Check the next number only if it's still considered prime to avoid excessive checks
                i = i + 1

        # Output the result
        if is_prime:
            prime_status = "prime"
        else:
            prime_status = "not prime"

        print(f"Input: {number}. It is {odd_even} and it is {prime_status}.")

        # Prompt user if they want to input again
        run_prime = input("Do you want to input another integer? (Y/N): ").upper()

    # If user does not want to run or chooses to exit the loop
    print("Exiting prime_calculator_function. Starting the ice-floe calculator immediately.")


# --- Ice Floe Calculator Functions ---

# Function 1 of 3: Input
def ice_floe_input():  # Function captures three integers (length, breadth, freeboard height) for two separate ice floes, and returns the six values as a single tuple.

    print("\n--- Ice Floe 1 Input ---")
    length1 = int(input("Enter length of top surface area for Floe 1 (in meters): "))
    breadth1 = int(input("Enter breadth of top surface area for Floe 1 (in meters): "))
    freeboard1 = int(input("Enter height of freeboard for Floe 1 (in meters): "))

    print("\n--- Ice Floe 2 Input ---")
    length2 = int(input("Enter length of top surface area for Floe 2 (in meters): "))
    breadth2 = int(input("Enter breadth of top surface area for Floe 2 (in meters): "))
    freeboard2 = int(input("Enter height of freeboard for Floe 2 (in meters): "))

    # Return all 6 inputs
    return (length1, breadth1, freeboard1, length2, breadth2, freeboard2)


# Function 2 of 3: Process/Calculate
def ice_floe_process(data): #This function accepts the input data, calculates the volume for each floe, and calculates the average of the two volumes.
    """ Main knowledge we need for the calculations:
    - The freeboard is the top 1/9th of the floe's height.
    - The draft (below the waterline) is the remaining 8/9ths.
    - So, The total thickness of the sea-ice floe is 9/9ths.
    - Total Thickness = Freeboard / (1/9) = Freeboard * 9
    Volume = Length * Breadth * Total Thickness
    """

    length1, breadth1, freeboard1, length2, breadth2, freeboard2 = data

    # Calculate Total Thickness (TT) for Floe 1: TT = Freeboard*9
    thickness1 = freeboard1 * 9
    # Calculate Volume for Floe 1: Volume = Length * Breadth * TT
    volume1 = length1 * breadth1 * thickness1

    # Calculate Total Thickness (TT) for Floe 2
    thickness2 = freeboard2 * 9
    # Calculate Volume for Floe 2
    volume2 = length2 * breadth2 * thickness2

    # Calculate the average volume of the two floes
    average_volume = (volume1+volume2)/2

    # Return the individual volumes and the average volume
    return (volume1, volume2, average_volume)


# Function 3 of 3: Output
def ice_floe_output(volumes_data):  # This function accepts the individual volumes and the average volume and outputs them with suitable messaging.

    volume1, volume2, average_volume = volumes_data

    print("\n--- Ice Floe Volume Results ---")
    print(f"Volume of Ice Floe 1: {volume1} m^3")
    print(f"Volume of Ice Floe 2: {volume2} m^3")
    print(f"Average Volume of the two Ice Floes: {average_volume} m^3")
    # No return is required.


# --- Main Function ---
def main():
    # Controls the overall operation, starting with the prime calculator and then the ice-floe calculator suite.
    prime_calculator_function()

    # STARTING THE ICE-FLOE CALCULATOR

    # 1. Ask the user initially if they want to execute the ice-floe calculator
    run_ice_floe = input("\nDo you want to execute the ice-floe calculator? (Y/N): ").upper()

    # 2. Enter the while loop *only* if the initial answer was 'Y'
    while run_ice_floe == 'Y':
        # --- EXECUTE THE CALCULATOR SUITE ---
        # First Function: Input
        input_data = ice_floe_input()

        # Second Function: Process
        volumes_data = ice_floe_process(input_data)

        # Third Function: Output
        ice_floe_output(volumes_data)

        run_ice_floe = input("Do you wish to run the ice-floe functions again? (Y/N): ").upper()
        # If the user enters 'N' here, the loop condition (while run_ice_floe == 'Y') will be false, and the loop will exit.

    # When the loop finishes (i.e., run_ice_floe is not 'Y')
    print("\nExiting the Ice Floe Calculator. Program finished.")


# Standard call to the main function
if __name__ == "__main__":
    main()