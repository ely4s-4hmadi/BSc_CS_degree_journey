# Ahmadi_MohammadElyas  201792013  November2025   CA-06.py
# Generates alien names for film credits and solves an anagram puzzle for the starring role.

def get_actor_lists(): #This function provides the required actor name lists.
    # Required data for consistent assessment results:
    actor_given_list = ['raja', 'zion', 'yiting', 'hamza', 'ughur']
    actor_family_list = ['desu', 'hnab', 'jones', 'nyme', 'ppayi']
    return actor_given_list, actor_family_list


def generate_alien_name(given_name, family_name): #This function generates an alien name from a single actor's given and family names.
    # Logic: First 2 chars of family name + First 2 chars of given name.

    # Extract segments using slicing
    family_part = family_name[0:2]
    given_part = given_name[0:2]

    # Concatenate
    return family_part + given_part


def generate_star_alien_name(given_name, family_name): #This function processes all actor names in the lists to generate a corresponding list of alien names using the core algorithm.
    # Logic: First 2 chars of family name + First 3 chars of given name (reversed).

    family_part = family_name[0:2]
    given_part = given_name[0:3]

    # Reverse the given_part using a loop as per assignment preference for list/loop constructs
    given_part_reversed = ""
    for char in given_part:
        given_part_reversed = char + given_part_reversed

    return family_part + given_part_reversed


def process_actor_lists(given_list, family_list): #This function iterates through actor lists to create the list of alien names.
    alien_names = []

    for i in range(len(given_list)):
        name = generate_alien_name(given_list[i], family_list[i])
        alien_names.append(name)

    return alien_names


def derive_star_identity(alien_names):
    """
    THIS function solves the anagram puzzle to find the Star's real name.
    1. Extracts first 2 letters of every standard alien name.
    2. Rearranges them to form the Star's real name (Johnny Depp).
    3. Generates the Star's alien name using Algorithm 2.
    """
    # Extract the segment from each alien name: the first two letters
    segments = []
    for name in alien_names:
        segments.append(name[0:2])

    # Rearrange segments to form the star's names:
    # Given name:  'jo' + 'hn' + 'ny'
    star_given_raw = segments[2] + segments[1] + segments[3]
    # Family name: 'de' + 'pp'
    star_family_raw = segments[0] + segments[4]

    # Generate star's alien name
    star_alien_final = generate_star_alien_name(star_given_raw, star_family_raw)

    return star_given_raw, star_family_raw, star_alien_final


def display_enhanced_credits(given_list, family_list, alien_list, star_data): #This function displays the enhanced film credits, including the star derived from the optional task.

    s_given, s_family, s_alien = star_data
    star_full_name = f"{s_given.capitalize()} {s_family.capitalize()}"

    print("\n")
    print(f"{'The COMP101 Galactic Saga':^50}")
    print("-." * 27 + "-")

    # Star Credit
    print(f"The hidden Star is: {star_full_name} as: {s_alien.capitalize():^10}")
    print("-" * 55)

    print(f"{'SUPPORTING ACTOR':<25} | {'ALIEN CHARACTER':>25}")
    print("-" * 55)

    for i in range(len(given_list)):
        full_actor_name = f"{given_list[i].capitalize()} {family_list[i].capitalize()}"
        alien_name = alien_list[i].capitalize()
        print(f"{full_actor_name:<25} | {alien_name:>25}")

    print("-" * 55)


def main(): #Finally, this function (Main controller): loads data, processes names, and outputs results.
    """
    Finally,
    The main control function for the program execution.
    Initializes data, processes lists, and calls output functions.
    This ensures the program is fully modularised.
    """
    # Load actor lists
    actors_given, actors_family = get_actor_lists()

    # Process the standard alien names
    alien_names = process_actor_lists(actors_given, actors_family)

    # Solve the hidden anagram puzzle (optional enhancement)
    star_data = derive_star_identity(alien_names)

    # Display final enhanced credits
    display_enhanced_credits(actors_given, actors_family, alien_names, star_data)


# Standard call to the main function
if __name__ == "__main__":
    main()
