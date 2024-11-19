# Haylee Paredes
# 10/17/24
# P3HW1
# Access understanding of lists & branching 

# Allow user to give lsit items
mod1 = float(input("Enter a grade for Module 1: "))
mod2 = float(input("Enter a grade for Module 2: "))
mod3 = float(input("Enter a grade for Module 3: "))
mod4 = float(input("Enter a grade for Module 4: "))
mod5 = float(input("Enter a grade for Module 5: "))
mod6 = float(input("Enter a graed for Module 6: "))

# Empty list
num_list = []

# Add variables to the list
num_list.append(mod1)
num_list.append(mod2)
num_list.append(mod3)
num_list.append(mod4)
num_list.append(mod5)
num_list.append(mod6)

# Create a list with variables
num_list = [mod1, mod2, mod3, mod4, mod5, mod6]

average = sum(num_list)/len(num_list)

# Using functions with list
print()
print("----------Results-----------")

print(f"Lowest Grade: {min(num_list)}")
print(f"Highest Grade: {max(num_list)}")
print(f"Sum of Grades: {sum(num_list)}")
print(f"Average: {average:.2f}")

print("----------------------------")

# Branching to determine the letter grade
letGrad = ""

if average >= 90:
    letGrad = "A"

elif average >= 80:
    letGrad = "B"
    
elif average >= 70:
    letGrad = "C"

elif average >= 60:
    letGrad = "D"

else:
    letGrad = "F"

print()
print(f"Your grade is: {letGrad}")
