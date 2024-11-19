# Haylee Paredes
# 10/24/24
# P4HW2
# Assess students ability to edit and enhance exiting programs


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

