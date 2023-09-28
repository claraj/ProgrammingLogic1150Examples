""" To be a blood donor in the US, you need to be 16 or older, and weigh at least 110 lbs.

There are other requirements which we will ignore for this program. """


def main():
    age = int(input('Please enter your age, in years: '))
    weight = int(input('Please enter your weight, to the nearest pound: '))

    eligible = check_donor_eligibility(age, weight)

    if eligible:
        print('You are eligible to donate blood, please check for any other requirements '
              'and get more information at https://www.redcrossblood.org/')
    else:
        print('You are not eligible at this time, please visit https://www.redcrossblood.org/ for more information.')


def check_donor_eligibility(age, weight):
    # Decide if a person with this height and weight is eligible and return True or False to indicate eligibility

    if age >= 16 and weight >= 110:   # age must be greater or equal to 16  AND  weight must be greater or equal to 110
        return True  # return the value True to indicate eligibility. Whatever code calls this function can access this value.
    else:
        # too young, or weight too low
        # check reasons for not being eligible, print specific message(s)
        if age < 16:
            print('You are too young, please consider donating blood when you are 16.')
        if weight < 110:
            print('Your weight is too low, for the health and safety of donors, they must weigh at least 110lbs.')
        return False  # return the value False to indicate in-eligibility. Whatever code calls this function can access this value.


main()  # don't forget!
