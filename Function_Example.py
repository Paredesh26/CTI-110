# Create some user dedfined functions

# Defined a non-value rerturning funtion
def my_animal(name, sound, pound_food):
    print(f"The {name} make a '{sound}' noise!")
    print(f"The {name} eats {pound_food} pound of food a day.")
    print(f"The {name} eats {(pound_food * 7):.2f} pound of food a week.")
# -----------------------------------------------------------------------
def getName():
    name = input("Enter your name: ")
    return name + " *******"
# -----------------------------------------------------------------------
def displayName(first):
    lastName = input("Enter your name: ")
    fullName = first + " " + lastName
    return fullName
# -----------------------------------------------------------------------
# Create a main function - all logic goes here
def main():
    print("The main function is executing!")
    print()
    # Call the my_animal funtion
    my_animal("Lion", "rarwwwwr", 20.5)
    print()
    my_animal("Mouse", "ekekekekkk", 0.2)
# -----------------------------------------------------------------------
    # Call the value-returning function
    myName = getName()
    print(myName)
    print()
    print(displayName(myName))
# -----------------------------------------------------------------------
# Call the main function
if __name__ == "__main__":
    main()
