# Haylee Paredes
# P4HW1
# 11/10/24
# Assess ability to edit and enhance exiting programs

'''
Get the integer to run the loop
Create a list for scores entered(Scores_list = [])
Iterate the for loop
Calculate the lowest score
Remove the lowest score with (.remove)
Calculate the average score sum/len, which is the sum divided by the length of the list
Use an if statement to find the letter grade of the average score
Display lowest score
Display the modified list
Display average scores
Display grade
'''
"----------------------------------------"
# Get integer to run the main for loop
Scores = int(input("How many scores do you want to enter? "))
"----------------------------------------"
# Create a list to hold valid inputs
Scores_list = []
"----------------------------------------"
# For loop to iterate Scores times
for ScoreNum in range(Scores):
    score = float(input(f"Enter score #{ScoreNum + 1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{ScoreNum + 1} again: "))
    # Once valid input is given, add it to a list
    Scores_list.append(score)
"----------------------------------------"
# Calculate lowest score
Lowest = min(Scores_list)
"----------------------------------------"
# Remove lowest score from list
Scores_list.remove(Lowest)
"----------------------------------------"
# Calculate average with length of scores (Or by how many scores entered in by user)
AvgScore = sum(Scores_list)/ len(Scores_list)
"----------------------------------------"
# Find letter grade of average
if AvgScore >= 90:
    grade = 'A'
elif AvgScore >= 80:
    grade = 'B'
elif AvgScore >= 70:
    grade = 'C'
elif AvgScore >= 60:
    grade = 'D'
else:
    grade = 'F'
"----------------------------------------"
# Display results
print()
print()
print("--------------Results-----------")
print(f"Lowest Score: {Lowest}")
print(f"Modified List: {Scores_list}")
print(f"Scores Average: {AvgScore:.2f}")
print(f"Grade: {grade}")
print("--------------------------------")
