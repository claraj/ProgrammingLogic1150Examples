# If statements 3 - who won?
#
# Two teams play a game. Ask the user for team 1's score.  Ask the user for team 2's score.
#
# Use conditional statements to print a message that says "Team 1 won" or "Team 2 won" or "It was a tie"

team_1_score = int(input('What was team 1\'s score? '))
team_2_score = int(input('What was team 2\'s score '))

if team_1_score > team_2_score:  # team 1 scored more points than team 2
    print('Team 1 won!')
elif team_2_score > team_1_score: # team 2 score more points that team 1
    print('Team 2 won!')
else:  # this happens if team 1 score is the same as team 2 score
    print('It was a tie!')
