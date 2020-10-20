# CSC 217 - Assignment One - Dungeons & Dragons Character Creator
# Programmer: Connor McCloskey
# Date created: 6/11/2020
# Date of final update: 6/14/2020


# Write-up -------------------------------------------------------------------------------------------------------------
"""
For our first assignment, and to keep in line with my love of gaming/game development degree, I decided to create a
truncated Dungeons & Dragons character creator.

The player (user) will be presented with a menu corresponding to a variety of aspects used to build a D&D character.
Each option calls a corresponding function to help them create their character. The user will also have the option to
export this information to a text file for use elsewhere.
"""
# --------------------------------------------------------------------------------------------------------------------//


# Variables & Imports --------------------------------------------------------------------------------------------------
# Import random for dice rolls
import random

# Boolean for menu loops
done = False

# tuple for character name
name = ()

# empty string for class and character race
character_class = ""
character_race = ""

# dictionary for available character classes
classes = {"A": "Fighter",
           "B": "Barbarian",
           "C": "Bard",
           "D": "Cleric",
           "E": "Druid",
           "F": "Monk",
           "G": "Paladin",
           "H": "Ranger",
           "I": "Rogue",
           "J": "Sorcerer",
           "K": "Warlock",
           "L": "Wizard"}

# dictionary for available character races
races = {"A": "Human",
         "B": "Dwarf",
         "C": "Elf",
         "D": "Gnome",
         "E": "Half-Elf",
         "F": "Half-Orc",
         "G": "Tiefling",
         "H": "Tabaxi",
         "I": "Goliath",
         "J": "Aasimar",
         "K": "Firbolg",
         "L": "Goblin"}

# dictionaries for character stats and modifiers - Intelligence, Wisdom, Charisma, Constitution, Dexterity, and Strength
stats = {"INT": 0,
         "WIS": 0,
         "CHA": 0,
         "CON": 0,
         "DEX": 0,
         "STR": 0}
modifiers = {"INT": 0,
             "WIS": 0,
             "CHA": 0,
             "CON": 0,
             "DEX": 0,
             "STR": 0}

# Multi-line string for main menu
main_menu = """
Main Menu
Please enter your selection by inputting the corresponding letter with one of the below menu options:
A. Enter Character Name
B. Choose Character Class
C. Choose Character Race
D. Create Character Stats
E. Export to file
F. Print character information
G. Exit Program
"""
# --------------------------------------------------------------------------------------------------------------------//


# Functions ------------------------------------------------------------------------------------------------------------
# Function for creating the player's character's name
def char_name():
    # Print instructions to the player
    # Then prompt for inputting a first, middle, and last name
    # To give the player some creative agency, we'll allow them to enter a middle name and not a last name
    # They may have a narrative reason for this!
    print("""
Let's create a name for your character.
    
You will be prompted to enter a first, middle, and last name.
    
Only a first name is required. If you do not wish to give your character a middle or last name, 
enter NONE (all caps) when prompted.
    
Note that Dungeons & Dragons is a game based on storytelling and creativity - for that reason, we have left it
possible for a character to have a middle name with no last name. Has a demon stripped away your memory of it? 
Has your character forsworn the family name as a result of something in their past? It's up to you to create a
narrative reason for this! And, more than likely, to joke about it with your fellow players.\n
    """)
    # Get input from the player
    # For the middle and last name - check to see if the player has entered in the NONE command. If so, pass.
    # If they HAVE entered a middle name or last name, set a boolean to True so we can keep track of that info
    middle_bool = False
    last_bool = False

    first = input("Enter a first name: ")
    middle = input("Enter a middle name: ")
    if middle.upper() == "NONE":
        pass
    else:
        middle_bool = True
    last = input("Enter a last name: ")
    if last.upper() == "NONE":
        pass
    else:
        last_bool = True

    # Now, using the player info, determine the tuple that will be our player name
    if middle_bool is False:
        if last_bool is False:
            character_name = (first)
        elif last_bool is True:
            character_name = (first, last)
    elif middle_bool is True:
        if last_bool is False:
            character_name = (first, middle)
        elif last_bool is True:
            character_name = (first, middle, last)

    # Finally, return the player name
    # To print, we'll create a string variable that holds the tuple if the character has more than one name.
    # I found out that strings have a .join function in Python, which makes it easy to print a tuple with a space
    # as a delimiter
    if middle_bool or last_bool is True:
        x = ' '.join(character_name)
    else:
        x = character_name
    print("Your character's name is", x)
    return character_name


# Function to choose the player character's class. The player is presented with a menu corresponding to our
# dictionary of available classes (declared under Variables & Imports). We then return the corresponding letter
# for use in other functions
def char_class():
    # Print menu and instructions
    print("""
Class Menu
    
Your character's class determines what kind of abilities your character has. Will you be a spell-slinging wizard?
A singing bard? A stealthy rogue? Maybe you'll be the classic sword-wielding fighter! The choice is yours...
    
Please enter your selection by inputting the corresponding letter with one of the below menu options:
A. Fighter
B. Barbarian
C. Bard
D. Cleric
E. Druid
F. Monk
G. Paladin
H. Ranger
I. Rogue
J. Sorcerer
K. Warlock
L. Wizard
""")
    # Loop to get player input
    while not done:
        class_input = input("Enter your choice now: ")

        # To quickly determine if the player's input is valid, we'll check the input against the acceptable range
        # of ASCII codes. Valid answers would be greater than or equal to 65 and less than or equal to 76, in this case
        # If it's valid, return class_input. Else, return a warning and prompt another input.
        class_input = class_input.upper()
        if (ord(class_input) >= 65) and (ord(class_input) <= 76):
            print("Your character's class is:", classes[class_input])
            return classes[class_input]
        else:
            print("Invalid input. Please be sure to use single letters that correspond with a menu item.")


# Function for choosing the player character's race
# This functions exactly like the character's class, so no surprises here
def char_race():
    # Print menu and instructions
    print("""
Race Menu

The worlds of D&D are full of many peoples. Will you be one of the hardy humans? The scaly dragonborns?
The demon-spawn tieflings? Or perhaps something else...

Please enter your selection by inputting the corresponding letter with one of the below menu options:
A. Human
B. Dwarf
C. Elf
D. Gnome
E. Half-Elf
F. Half-Orc
G. Tiefling
H. Tabaxi
I. Goliath
J. Aasimar
K. Firbolg
L. Goblin
""")
    # Loop to get player input
    while not done:
        race_input = input("Enter your choice now: ")

        # To quickly determine if the player's input is valid, we'll check the input against the acceptable range
        # of ASCII codes. Valid answers would be greater than or equal to 65 and less than or equal to 76, in this case
        # If it's valid, return class_input. Else, return a warning and prompt another input.
        race_input = race_input.upper()
        if (ord(race_input) >= 65) and (ord(race_input) <= 76):
            print("Your character's race is:", races[race_input])
            return races[race_input]
        else:
            print("Invalid input. Please be sure to use single letters that correspond with a menu item.")


# This function acts as rolling a d6 (six-sided die) using the random library
def d6():
    # roll between 1 and 6 (7 non-inclusive)
    roll = random.randrange(1, 7)
    return roll


# This function is called by the char_stats function to generate character stats
def generate_stat():
    # List to hold the dice rolls
    stat_list = []

    # roll a d6 4 times (0, 1, 2, 3)
    times_rolled = 0
    while times_rolled < 4:
        roll = d6()
        stat_list.append(roll)
        times_rolled += 1

    # sort the list of stats
    stat_list.sort()

    # Pop the lowest from the sorted stat_list
    stat_list.pop(0)

    # Total stat equal to all of the values in stat_list added together
    stat = sum(stat_list)

    # Return the stat
    return stat


# This function is called by char_stats to generate character ability modifiers
# Calculate modifier - take in a stat, subtract 10, divide by 2 (rounded down), return result
def generate_mod(stat):
    stat = stat - 10
    mod = int(stat / 2)
    return mod


# Function for generating character stats
# We'll pass in the modifiers dictionary above (passed by reference since they're dictionaries) to modify those as well
def char_stats(stats, modifiers):

    # Print instructions to the player
    print("""
In D&D, your character has a variety of stats that determine what you can do and how well you can do it.
These stats fall into six categories: Intelligence, Wisdom, Charisma, Constitution, Dexterity, and Strength.

These stats are generated by rolling a six-sided die four times, discarding the lowest score, and adding together
the remaining numbers. Depending on what this score is, an ability modifier will be assigned to that stat. This is done
by subtracting 10 from the stat, then dividing by 2.

This program will now generate your stats and ability modifiers using this method...
""")

    # Generate scores and modifiers for each stat, add them to the passed in dictionaries
    INT = generate_stat()
    INT_mod = generate_mod(INT)
    stats["INT"] = INT
    modifiers["INT"] = INT_mod
    print("Your intelligence score is:", stats["INT"])
    print("Your intelligence modifier is:", modifiers["INT"])
    print("\n")

    WIS = generate_stat()
    WIS_mod = generate_mod(WIS)
    stats["WIS"] = WIS
    modifiers["WIS"] = WIS_mod
    print("Your wisdom score is:", stats["WIS"])
    print("Your wisdom modifier is:", modifiers["WIS"])
    print("\n")

    CHA = generate_stat()
    CHA_mod = generate_mod(CHA)
    stats["CHA"] = CHA
    modifiers["CHA"] = CHA_mod
    print("Your charisma score is:", stats["CHA"])
    print("Your charisma modifier is:", modifiers["CHA"])
    print("\n")

    CON = generate_stat()
    CON_mod = generate_mod(CON)
    stats["CON"] = CON
    modifiers["CON"] = CON_mod
    print("Your constitution score is:", stats["CON"])
    print("Your constitution modifier is:", modifiers["CON"])
    print("\n")

    DEX = generate_stat()
    DEX_mod = generate_mod(DEX)
    stats["DEX"] = DEX
    modifiers["DEX"] = DEX_mod
    print("Your dexterity score is:", stats["DEX"])
    print("Your dexterity modifier is:", modifiers["DEX"])
    print("\n")

    STR = generate_stat()
    STR_mod = generate_mod(STR)
    stats["STR"] = STR
    modifiers["STR"] = STR_mod
    print("Your strength score is:", stats["STR"])
    print("Your strength modifier is:", modifiers["STR"])
    print("\n")


# Export the character sheet to a file for the player to use
def export():
    # Create a new file for each character based on the character's name
    # Includes exception handling for the file
    # First, create a variable that holds the condensed version of the character's name based on the length of the
    # tuple
    if type(name) is tuple:
        x = ' '.join(name)
    else:
        x = name
    try:
        file = x + ".txt"
        character_file = open(file, "w")
    except IOError:
        print("WARNING - unable to open or create character file.")
        return

    # Print the character's attributes to the file
    print("Name:", x, "\n", file=character_file)
    print("Race:", character_race, "\n", file=character_file)
    print("Class:", character_class, "\n", file=character_file)
    print("Stats:", file=character_file)
    print("Intelligence:", stats["INT"], file=character_file)
    print("Wisdom:", stats["WIS"], file=character_file)
    print("Charisma: ", stats["CHA"], file=character_file)
    print("Constitution:", stats["CON"], file=character_file)
    print("Dexterity:", stats["DEX"], file=character_file)
    print("Strength:", stats["STR"], "\n", file=character_file)
    print("Modifiers:", file=character_file)
    print("Intelligence:", modifiers["INT"], file=character_file)
    print("Wisdom:", modifiers["WIS"], file=character_file)
    print("Charisma: ", modifiers["CHA"], file=character_file)
    print("Constitution:", modifiers["CON"], file=character_file)
    print("Dexterity:", modifiers["DEX"], file=character_file)
    print("Strength:", modifiers["STR"], file=character_file)

    # Close the file and let the player know that it's done
    character_file.close()
    print("Character sheet exported to file.")


# Print the character's information to the console
def print_character():
    # Print name, based on if name is a tuple (in other words, if the character has a middle and/or last name)
    if type(name) is tuple:
        x = ' '.join(name)
    else:
        x = name
    print("Your character's name is", x, "\n")
    # Print race
    print("Your character is a(n)", character_race, "\n")
    # Print class
    print("Your character's class is", character_class, "\n")
    # Print stats
    print("Your character's stats are:")
    print("Intelligence:", stats["INT"])
    print("Wisdom:", stats["WIS"])
    print("Charisma: ", stats["CHA"])
    print("Constitution:", stats["CON"])
    print("Dexterity:", stats["DEX"])
    print("Strength:", stats["STR"], "\n")
    # Print modifiers
    print("Your character's ability modifiers are:")
    print("Intelligence:", modifiers["INT"])
    print("Wisdom:", modifiers["WIS"])
    print("Charisma: ", modifiers["CHA"])
    print("Constitution:", modifiers["CON"])
    print("Dexterity:", modifiers["DEX"])
    print("Strength:", modifiers["STR"], "\n")


# Function to quit the program!
def exit_program():
    quit(0)
# --------------------------------------------------------------------------------------------------------------------//


# Main program ---------------------------------------------------------------------------------------------------------
print("Welcome to the 2020 McCloskey Quick Dungeons & Dragons Character Creator!")
while not done:
    print(main_menu)
    player_input = input("Enter your selection now: ")
    if player_input.lower() == "a":
        name = char_name()
    elif player_input.lower() == "b":
        character_class = char_class()
    elif player_input.lower() == "c":
        character_race = char_race()
    elif player_input.lower() == "d":
        char_stats(stats, modifiers)
    elif player_input.lower() == "e":
        export()
    elif player_input.lower() == "f":
        print_character()
    elif player_input.lower() == "g":
        exit_program()
    else:
        print("Invalid input. Please be sure to use single letters that correspond with a menu item.")
# --------------------------------------------------------------------------------------------------------------------//
