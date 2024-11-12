# Create some user dedfined functions

# Defined a non-value rerturning funtion
def my_animal(name, sound, pound_food):
    print(f"The {name} make a {sound} noise!")
    print(f"The {name} eats {pound_food} pound of food a day.")
    print(f"The {name} eats {pound_food * 7} pound of food a week.")

# Create a main function - all logic goes here
def main():
    print("The main function is executing!")
    print()
    # Call the my_animal funtion
    my_animal("Lion", "rarwwwwr", 20.5)

# Call the main function
if __name__ == "__main__":
    main()
