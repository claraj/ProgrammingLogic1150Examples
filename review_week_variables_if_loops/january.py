# For loops
#
# Write a loop that prints all the dates in January. So your program will print
#
# January 1
#
# January 2
#
# January 3
#
# ... more dates here ...
#
# January 30
#
# January 31

for day in range(1, 32):  # count from 1 to 31
    # numbers are where to start at, and 1 more than where to end at
    print('January ' + str(day))   # no need to modify loop counter. 

#
# for day in range(31):  # repeat 31 times
#     print('January ' + str(day + 1))  # add 1 to loop counter variable