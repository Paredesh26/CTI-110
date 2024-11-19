# Haylee Paredes
# 11/01/24
# P4LAB2
# Tests knowledge of how to write code that displays information to users using loops


run_again = 'yes'

while run_again != "no":

# Get integer from user
    user_num = int(input("Enter an integer: "))

# Determine if the integer is positive or negative
    if user_num >= 0:
        
        # Display multiplication for that value and range (1-12)
        for item in range (1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
            
# If negative, the program tells the user it cannot accept it
    else:
        print("This program does not handle negative numbers")
        
# Ask the user to run again
    run_again = input("Would you like to run the program again? ")
    
# Loop has broken. User entered 'no'
print("Exiting program....")




