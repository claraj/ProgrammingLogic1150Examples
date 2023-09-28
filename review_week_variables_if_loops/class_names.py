# For loops 3
#
# Ask for the number of classes you are taking. Save in an integer variable.
#
# Create an empty string called class_names
#
# Write a for loop that asks for each class name.
#
# Add each class name to the class_names string, followed by a '\n' newline character.
#
# And the end of the loop, print the class_names string.  Here's example output from the program:
#
# How many classes are you taking? 3
# Enter the name of a class: Programming Logic
# Enter the name of a class: Information Technology Concepts
# Enter the name of a class: Preparing for IT
# Here are your classes:
#
# Programming Logic
# Information Technology Concepts
# Preparing for IT

classes = int(input('How many classes are you taking: '))

class_names = ''  # empty string

for class_name in range(classes):
    name = input('Enter the name of a class you are taking: ')
    class_names = class_names + name + '\n'

print('Thank you, here are the classes you are taking: \n')
print(class_names)
