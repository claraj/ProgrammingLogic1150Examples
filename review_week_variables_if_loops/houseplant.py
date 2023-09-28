# If statements 2 - Houseplants
#
# Ivy Plants like cool temperatures and shade.
# Jade Plants like cool temperature and sun.
# Begonia plants like warm temperatures and shade.
# Hibiscus Plants like warm temperatures and sun.

# Your user wants to choose a houseplant for their home.
#
# Ask if the user's home is warm or cool.
#
# Then, ask them if their home has sun, or shade inside.
#
# Use their answers to recommend one houseplant from the list above.

house_temperature = input('Is your home warm or cool? Enter "warm" or "cool" ')
sun_or_shade = input('Is your home sunny or shady? Enter "sun" or "shade" ')

if house_temperature == 'cool' and sun_or_shade == 'shade':
    print('A recommended plant is an Ivy plant')
elif house_temperature == 'cool' and sun_or_shade == 'sun':
    print('A recommended plant is a Jade plant')
elif house_temperature == 'warm' and sun_or_shade == 'shade':
    print('A recommended plant is a Begonia plant')
elif house_temperature == 'warm' and sun_or_shade == 'sun':
    print('A recommended plant is a Hibiscus plant')
else:
    print('Sorry, cannot recommend a plant. Try again and enter "warm" or "cool" \n'
          'for temperature, and "sun" or "shade" for sunny or shady')
