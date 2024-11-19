# Haylee Paredes
# 10/08/24
# P2HW1
# Assess the ability to edit and enhance exiting programs

print("----This program calculates and displays travel expenses.----")
print()

# Get budget value (as an integer) from the user
budget_num = float(input("Enter Budget: "))

print()

# Get travel place from the user
traDes = input("Enter your travel destination: ")

print()

# Get gas value (as an integer) from the user
gas_num = float(input("How much do you think you will spend on gas? "))

print()

# Get accomHotel value (as an integer) from the user
accomHotel_num = float(input("How much will you need for accomodation/hotel? "))

print()

# Get food value (as an integer) from the user
food_num = float(input("How much do you think you will spend on food? "))

print()
print("-----------Travel Expenses-----------")

print(f"{'Location:':<20}{traDes}")
print(f"{'Initial Budget:':<20}${budget_num:,.2f}")
print(f"{'Fuel:':<20}${gas_num:,.2f}")
print(f"{'Accomodation:':<20}${accomHotel_num:,.2f}")
print(f"{'Food:':<20}${food_num:,.2f}")

print("-------------------------------------")

expTotal = gas_num + accomHotel_num + food_num
travTotal = budget_num - expTotal

print()
print(f"{'Remaining balance:':<20}${travTotal:,.2f}")
