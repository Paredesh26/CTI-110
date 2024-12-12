# Haylee Paredes
# 11/19/24
# P5HW
# Use of loops, functions, and module import to complete a program


import random

# Function to create a character
def create_character(): # This (create_character) allows the user to enter in certain details for a character a user creates.
    name = input("Enter the character's name: ")
    level = int(input("Enter the character's level (1-10): "))
    strength = int(input("Enter the character's strength (1-100): "))
    health = int(input("Enter the character's health (1-100): "))
    inventory = ["Healing Potion", "Damage Booster"]  # Default inventory
    return {
        "name": name,
        "level": level,
        "strength": strength,
        "health": health,
        "max_health": health,
        "inventory": inventory,
    }

# Function to display a party
def display_party(party_name, party):
    print(f"\nParty: {party_name}")
    if not party:
        print("This party has no characters yet.")
    else:
        for character in party:
            print(
                f"Name: {character['name']}, Level: {character['level']}, "
                f"Strength: {character['strength']}, Health: {character['health']}, Inventory: {', '.join(character['inventory'])}"
            )

# Function to perform battle between two characters
def cross_party_battle(party1_name, character1, party2_name, character2):
    print(
        f"\nBattle begins between {character1['name']} from {party1_name} "
        f"and {character2['name']} from {party2_name}!"
    )

    while character1["health"] > 0 and character2["health"] > 0:
        # Character 1's turn
        print(f"\n{character1['name']}'s turn!")
        action = input("Choose an action: (1) Fight, (2) Use Item: ").strip()
        if action == "1":
            # Fight
            damage = int(character1["strength"] * random.uniform(0.5, 1.5))
            character2["health"] -= damage
            print(f"{character1['name']} attacks {character2['name']} for {damage} damage!")
        elif action == "2" and character1["inventory"]:
            # Use item
            print(f"Available items: {', '.join(character1['inventory'])}")
            item = input("Choose an item to use: ").strip()
            if item in character1["inventory"]:
                if item == "Healing Potion":
                    character1["health"] = min(character1["max_health"], character1["health"] + 30)
                    print(f"{character1['name']} uses a Healing Potion and restores 30 health!")
                elif item == "Damage Booster":
                    character1["strength"] += 10
                    print(f"{character1['name']} uses a Damage Booster and gains +10 strength!")
                character1["inventory"].remove(item)
            else:
                print("Invalid item selection. Turn skipped.")
        else:
            print("Invalid action. Turn skipped.")

        # Check if character2 is defeated
        if character2["health"] <= 0:
            print(f"{character2['name']} has been defeated!")
            character1["level"] += 1
            if character1["level"] > 10:
                character1["level"] = 10

            # Random strength increase capped at 15
            strength_increase = random.randint(1, 15)
            character1["strength"] += strength_increase
            print(f"{character1['name']} gains a level and is now level {character1['level']}!")
            print(f"{character1['name']} gains {strength_increase} strength points!")
            print(f"{character1['name']}'s strength increases to {character1['strength']}!")
            break

        # Character 2's turn
        print(f"\n{character2['name']}'s turn!")
        action = random.choice(["1", "2"])  # AI chooses randomly between fight or item usage
        if action == "1":
            # Fight
            damage = int(character2["strength"] * random.uniform(0.5, 1.5))
            character1["health"] -= damage
            print(f"{character2['name']} attacks {character1['name']} for {damage} damage!")
        elif action == "2" and character2["inventory"]:
            # Use item
            item = random.choice(character2["inventory"])
            if item == "Healing Potion":
                character2["health"] = min(character2["max_health"], character2["health"] + 30)
                print(f"{character2['name']} uses a Healing Potion and restores 30 health!")
            elif item == "Damage Booster":
                character2["strength"] += 10
                print(f"{character2['name']} uses a Damage Booster and gains +10 strength!")
            character2["inventory"].remove(item)

        # Check if character1 is defeated
        if character1["health"] <= 0:
            print(f"{character1['name']} has been defeated!")
            character2["level"] += 1
            if character2["level"] > 10:
                character2["level"] = 10

            # Random strength increase capped at 15
            strength_increase = random.randint(1, 15)
            character2["strength"] += strength_increase
            print(f"{character2['name']} gains a level and is now level {character2['level']}!")
            print(f"{character2['name']} gains {strength_increase} strength points!")
            print(f"{character2['name']}'s strength increases to {character2['strength']}!")
            break

    # Reset health after battle
    character1["health"] = character1["max_health"]
    character2["health"] = character2["max_health"]

def main():
    parties = {}  # Dictionary to store parties
    print("Create some characters!")
    print("Let's create some party members too!")
    
    while True:
        print("\nMenu:") # Create a menu for the user to enter in the option they would like to choose.
        print() 
        print("1. Add a new party")
        print("2. Add a character to a party")
        print("3. Display all parties")
        print("4. View a single party")
        print("5. Battle between two parties")
        print("6. Exit")
        print()
        choice = input("Choose an option: ") # Allow the user to be able to enter in the option they would like to choose.
        print()

        # Add choice options (1-6).
        
        if choice == "1": # By adding an if statement we can create options for the user to choose from.
            party_name = input("Enter the name of the new party: ")
            # Adding another if statement, we can let the user know if their party already exists or if offically created.
            if party_name in parties:
                # This displays to the user that the party name they entered in already exists.
                print(f"Party '{party_name}' already exists!")
            else:
                # This creates an empty list that is added to when a user creates a party. 
                parties[party_name] = []
                # This displays to the user that their party was created successfully.
                print(f"Party '{party_name}' created successfully!")
        
        elif choice == "2": # The 2nd choose allows the user add a character to a party by using an if statement.
            party_name = input("Enter the name of the party to add a character to: ")
            # This if statement adds characters to parties or lets the user know if their party doesn't exist and needs to create a party.
            if party_name in parties:
                # This brings up the character creation section so the user can enter in a character.
                character = create_character()
                # This lets the user know that their character was added to that party.
                parties[party_name].append(character)
                # This displays to the user that the character was added to the party.
                print(f"Character '{character['name']}' added to party '{party_name}'.")
            else:
                # This displays to the user that the party they entered does not exist.
                print(f"Party '{party_name}' does not exist. Please create it first.")
        
        elif choice == "3":
            if not parties:
                # This displays to the user that no parties have been created.
                print("No parties have been created yet.")
            else:
                # This displays all the parties that have been created by the user.
                for party_name, party in parties.items():
                    display_party(party_name, party)
        
        elif choice == "4": # This will allow the user to view one party they choose.
            party_name = input("Enter the name of the party you want to view: ")
            # This diplays the party name if the party already exists and displays the characters in the party.
            if party_name in parties:
                display_party(party_name, parties[party_name])
            else:
                # This displays to the user that the party they entered does not exist.
                print(f"Party '{party_name}' does not exist.")
        
        elif choice == "5":
            if len(parties) < 2:
                print("You need at least two parties to perform a battle.")
            else:
                # Ensure existing characters have max_health
                for party in parties.values():
                    for character in party:
                        if "max_health" not in character:
                            character["max_health"] = character["health"]

                # Display all parties
                print("Available parties:")
                for i, party_name in enumerate(parties.keys()):
                    print(f"{i + 1}. {party_name}")

                # Select two parties
                party1_index = int(input("Select the first party (number): ")) - 1
                party2_index = int(input("Select the second party (number): ")) - 1

                if 0 <= party1_index < len(parties) and 0 <= party2_index < len(parties):
                    party1_name = list(parties.keys())[party1_index]
                    party2_name = list(parties.keys())[party2_index]

                    # Select one character from each party
                    print(f"\nSelect a character from {party1_name}:")
                    for i, character in enumerate(parties[party1_name]):
                        print(f"{i + 1}. {character['name']} (Level {character['level']})")

                    char1_index = int(input("Enter the number of the character: ")) - 1

                    print(f"\nSelect a character from {party2_name}:")
                    for i, character in enumerate(parties[party2_name]):
                        print(f"{i + 1}. {character['name']} (Level {character['level']})")

                    char2_index = int(input("Enter the number of the character: ")) - 1

                    if (
                        0 <= char1_index < len(parties[party1_name])
                        and 0 <= char2_index < len(parties[party2_name])
                    ):
                        char1 = parties[party1_name][char1_index]
                        char2 = parties[party2_name][char2_index]

                        cross_party_battle(party1_name, char1, party2_name, char2)


        # This ends the program.
        elif choice == "6":
            print("Game is ending, goodbye!")
            break

        # This restarts the program.
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
        
