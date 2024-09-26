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

print("Location:", traDes)
print("Initial Budget:", budget_num)

print()

print("Fuel:", gas_num)
print("Accomodation:", accomHotel_num)
print("Food:", food_num)

expTotal = gas_num + accomHotel_num + food_num
travTotal = budget_num - expTotal

print()
print("Remaining balance:", travTotal)
