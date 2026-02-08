# Ahmadi_MohammadElyas  201792013  December2025   CA-07.py
"""This program simulates how much money an aircraft makes on each flight (full and part load), works out window/aisle seat revenue,
    adds optional lunch income, and shows how many flights are needed to break even"""

import random
import math

# Global Constant (Fixed cost to the company)
FLIGHT_COST_TO_COMPANY = 15000



def create_seating_layout(): #This function only creates seating layout (2D list)
    return [
        [1, 5, 9, 13, 17],
        [2, 6, 10, 14, 18],
        [3, 7, 11, 15, 19],
        [4, 8, 12, 16, 20]
    ]


def is_window_seat(seat_number): #This function determine if seat is a window seat or aisle

    seat_layout = create_seating_layout() #To ALL the function to get the 2D list of seats
    combined_list = seat_layout[0] + seat_layout[-1] #To concatenate the first row (index 0) and the last row (index -1)

    return seat_number in combined_list


def generate_random_seating(): #This function generates part load (Random 0s or 1s)
    """A 2D list of flags (1=sold, 0=empty) for part-load."""
    seats = create_seating_layout()
    part_load = []

    for row in seats:
        new_row = []
        for _ in row:
            sold = random.randint(0, 1)
            new_row.append(sold)
        part_load.append(new_row)

    return part_load


def calculate_revenue(flags, seat_numbers, window_price, lunch_price): #This function calculates the revenue for any seating plan
    aisle_price = window_price // 2
    total_window_sold = 0
    total_aisle_sold = 0
    window_revenue = 0
    aisle_revenue = 0
    total_seats_sold = 0
    row_revenues = []
    total_revenue = 0

    for flag_row, seat_row in zip(flags, seat_numbers):
        row_total = 0
        for sold_flag, seat_number in zip(flag_row, seat_row):
            if sold_flag == 1:
                total_seats_sold += 1

                if is_window_seat(seat_number):
                    total_window_sold += 1
                    seat_rev = window_price
                    window_revenue += seat_rev
                else:
                    total_aisle_sold += 1
                    seat_rev = aisle_price
                    aisle_revenue += seat_rev

                row_total += seat_rev

        row_revenues.append(row_total)
        total_revenue += row_total

    lunch_revenue = 0
    if lunch_price > 0:
        lunch_revenue = total_seats_sold * lunch_price

    total_revenue += lunch_revenue

    return total_window_sold, window_revenue, total_aisle_sold, aisle_revenue, row_revenues, lunch_revenue, total_revenue


def generate_full_load_flags(): #Full load = every seat is sold
    layout = create_seating_layout()
    flags = []

    for row in layout:
        flags.append([1] * len(row))
    return flags


def print_seating_map(map_2d, title=""): #This function will print the 2D seating map
    print(f"\n{title}")
    print(" (Cockpit is to the left, Rows 1-4)")
    print("|Row | C1 | C2 | C3 | C4 | C5 |")
    print("|----|----|----|----|----|----|")

    for i, row in enumerate(map_2d):
        row_str = f"| {i + 1:<2} |"
        for seat in row:
            row_str += f" {seat}  |"
        print(row_str)


def calculate_break_even(total_revenue): #This function is for break-even calculation and round it up using math library
    if total_revenue <= 0:
        return "N/A (No Revenue)"

    flights = FLIGHT_COST_TO_COMPANY / total_revenue
    return math.ceil(flights)


def display_analysis(scenario_name, w_count, w_rev, a_count, a_rev, row_rev, lunch_rev, total_rev, flights_be, flags_2d,
                     window_price): #This function is only to make a dashboard that displays all required output for a single scenario.

    print("\n==================================================")
    print(f"      AIRCRAFT REVENUE DASHBOARD: {scenario_name}")
    print("==================================================\n")

    print("**Seat Revenue Summary:**")
    print(f"{'Total Window Seats Sold:':<25}{w_count:<5} Revenue: ${w_rev}")
    print(f"{'Total Aisle Seats Sold:':<25}{a_count:<5} Revenue: ${a_rev}")

    if lunch_rev > 0:
        print(f"{'Total Lunch Revenue:':<25}${lunch_rev}")
    print("-" * 50)

    print("**Individual Revenue by Row:**")
    for i, rev in enumerate(row_rev, start=1):
        print(f"  Row {i:<2}: ${rev}")
    print("-" * 50)

    print(f"\n{'Cost to company of the flight:':<25}${FLIGHT_COST_TO_COMPANY}")
    print(f"{'Total revenue for the flight:':<25}${total_rev}")

    print(f"\n**Flights needed to break-even (Rounded Up):** {flights_be}")

    if lunch_rev > 0:
        plan_title = f"{scenario_name} SEATING PLAN (1=Sold, 0=Empty)"
        print_seating_map(flags_2d, plan_title)
    print("\n" + "=" * 50)



def main(): #Finally, main function (core progam flow), it handles user input and runs both the Full Load and Part Load analyses.

    #inputs:
    window_price = int(input("Enter window seat price (≤ 100, integer): "))
    lunch_price = int(input("Enter lunch price (≤ 25, optional, 0 if none): "))

    seat_numbers = create_seating_layout()

    #full load analysis
    full_flags = generate_full_load_flags()
    results = calculate_revenue(full_flags, seat_numbers, window_price, lunch_price)
    full_be = calculate_break_even(results[6])

    display_analysis("FULL LOAD", *results, full_be, full_flags, window_price)

    #part load analysis (single run average)
    part_flags = generate_random_seating()
    results2 = calculate_revenue(part_flags, seat_numbers, window_price, lunch_price)
    part_be = calculate_break_even(results2[6])

    display_analysis("PART LOAD (Random Single Run Average)", *results2, part_be, part_flags, window_price)


#Standard call to the main function
if __name__ == "__main__":
    main()