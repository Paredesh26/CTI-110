# Haylee Paredes
# 09/26/24
# P1HW2
# Create a program that does basic math on numbers.

print("----This program calculates and displays travel expenses.----")
print()
print()

# Get budget value (as an integer) from the user
budget_num = int(input("Enter Budget: "))

print()

# Get travel place from the user
traDes = input("Enter your travel destination: ")

print()

# Get gas value (as an integer) from the user
gas_num = int(input("How much do you think you will spend on gas? "))

print()

# Get accomHotel value (as an integer) from the user
accomHotel_num = int(input("How much will you need for accomodation/hotel? "))

print()

# Get food value (as an integer) from the user
food_num = int(input("How much do you think you will spend on food? "))


print()
print("----Travel Expenses----")
print()

# Display the location and the travel budget
print("Location:", traDes)
print("Initial Budget:", budget_num)

print()

# Display the values for fuel, accomodation, and food
print("Fuel:", gas_num)
print("Accomodation:", accomHotel_num)
print("Food:", food_num)

# Add expenses together
expTotal = gas_num + accomHotel_num + food_num

# Subtract the budget and the expenses
travTotal = budget_num - expTotal

# Display the remaining balance 
print()
print("Remaining balance:", travTotal)
