# Haylee Paredes
# 10/17/24
# P3LAB
# Calculate coin combinations for given value

'''
# Regular Division
print(100/3)

# Floor Division
print(100//3)

#Modulus Division
print(100%3)

print(7%4)
'''

# Get money value from user
money = float(input("Enter the amount of money as a float: $"))

'''-------------------------------------------------------------------------'''
# Considering if the user put in 0.00
if money == 0:
    print("No change")
    
if money < 0:
    print("Ouch! You're in debt.")

'''-------------------------------------------------------------------------'''
# Check for debt
if money > 0:

    # Convert money to a whole number
    money = int(round(money * 100))

    # print(money)

    # Calculate the amount of $ in the money variable
    numDollars = money// 100
    '''print(f"Dollars: {numDollars}")'''

    # Remove the $ from the money variable
    money = money - (numDollars * 100)

    # Calculate the amount of Quarters in the money variable
    numQuart = money// 25
    '''print(f"Quarters: {numQuart}")'''

    # Remove the $ from the money variable
    money = money - (numQuart * 25)

    # Calculate the amount of Dimes in the money variable
    numDime = money// 10
    '''print(f"Dimes: {numDime}")'''

    # Remove the $ from the money variable
    money = money - (numDime * 10)

    # Calculate the amount of Nickels in the money variable
    numNick = money// 5
    '''print(f"Nickels: {numNick}")'''

    # Remove the $ from the money variable
    money = money - (numNick * 5)

    # Calculate the amount of Pennies in the money variable
    numPenn = money// 1
    '''print(f"Pennies: {numPenn}")'''

    # Remove the $ from the money variable
    money = money - (numPenn * 1)

else:
    numDollars = 0
    numQuart = 0
    numDime = 0
    numNick = 0
    numPenn = 0
    
'''-------------------------------------------------------------------------'''
# Print $ amount grammtically correct
if numDollars > 0:
    if numDollars == 1:
        print(f"{numDollars} dollar")
    else: # Variable is greater than one
        print(f"{numDollars} dollars")
        
'''-------------------------------------------------------------------------'''
# Print quarter amount grammtically correct
if numQuart > 0:
    if numQuart == 1:
        print(f"{numQuart} quarter")
    else: # Variable is greater than one
        print(f"{numQuart} quarters")
        
'''-------------------------------------------------------------------------'''
# Print dime amount grammtically correct
if numDime > 0:
    if numDime == 1:
        print(f"{numDime} dime")
    else: # Variable is greater than one
        print(f"{numDime} dimes")
        
'''-------------------------------------------------------------------------'''
# Print nickel amount grammtically correct
if numNick > 0:
    if numNick == 1:
        print(f"{numNick} nickel")
    else: # Variable is greater than one
        print(f"{numNick} nickels")
        
'''-------------------------------------------------------------------------'''
# Print penny amount grammtically correct
if numPenn > 0:
    if numPenn == 1:
        print(f"{numPenn} penny")
    else: # Variable is greater than one
        print(f"{numPenn} pennies")



