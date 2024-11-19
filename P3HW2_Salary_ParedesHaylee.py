# Haylee Paredes
# 10/24/24
# P3HW2
# Assess student understanding of decision structures

'''
Input: Get name as a string
Input: Get the hours worked as an integer
Input: Get the pay as a float

Output: Display employee name

If hours worked is greater than 40:
    Calculate any Overtime hours worked by subtracting 40 hours from hours worked
    Calculate Overtime pay (OT hours * (pay rate * 1.5))
    Calculate reg. pay (40 * reg. pay rate)
    Calculate gross pay by adding reg. pay and Overtime pay
    
else (employee worked 40 or less hours):
    overtime hours = 0
    overtime pay = 0
    calculate reg. pay by multiplying orginal hours worked by reg. pay rate

Output:
    Diplay total hours worked
    Display reg. pay rate
    Display overtime hours worked
    Display overtime pay (Overtime pay is 1.5 times reg. pay)
    Display pay for reg. hours worked at reg. pay rate
    Display gross pay - both peg. pay and overtime pay
'''

# Get user name
EmployName = input("Enter employee's name: ")

# Get users hours worked
Hours = int(input("Enter number of hours worked: "))

# Get users pay rate
PayRate = float(input("Enter employee's pay rate: "))

print("-" * 50)

'''------------------------------------------------'''

# Display employee's name
print("Employee name: ", EmployName)

'''------------------------------------------------'''

print()

'''------------------------------------------------'''

# Calculate overtime

if Hours < 40:
    OT = 0.00

elif Hours > 40:
    OT = Hours - 40

# Calculate reg. pay

if Hours < 40:
    RegPay = Hours * PayRate
    
elif Hours > 40:
    RegPay = 40 * PayRate

# Calculate Overtime pay 
OTPay = OT * (PayRate * 1.5)

#Calculate gross pay
GP = OTPay + RegPay

'''------------------------------------------------'''
 
# Display hours worked, pay rate, overtime, overtime pay, reghour pay, and gross pay.
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")

print("-" * 80)


# Display the values for hours worked, pay rate, overtime, overtime pay, reghour pay, and gross pay.
print(f"{Hours:<15}${PayRate:<10,.2f}{OT:<10,.2f}${OTPay:<15,.2f}${RegPay:<15,.2f}${GP}")

