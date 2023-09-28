# While loops 2
#
# Write a program that asks the user for a 4-letter department code,
# for example ENGL or MATH or ITEC or SPAN or WEBI.
# Use a while loop to validate that the code is exactly 4 letters.
# If it is, print a 'thank you for the data' message.

department_code = input('Enter the 4-letter department code: ')

# repeat while the input is INVALID
while len(department_code) != 4:  # condition is true if data is INvalid
    # Ask the user to re-enter data
    department_code = input('Error, please try again. Enter the 4-letter department code: ')
    # loop should end as soon as user enters valid data

# once valid data is entered, print a thank you message
print('Thank you, you entered ' + department_code)