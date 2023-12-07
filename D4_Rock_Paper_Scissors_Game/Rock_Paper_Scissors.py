# Print welcome message.
print("Welcome! Lets play Rock-Paper-Scissors against this machine!\n")

#import applicable module
import random               # to generate random number for opponent choice
import ascii_art as art     # custom module to produce the rock-paper-scissors (RPS) ascii art

# Create list to compute RPS outcome based on our POV
outcome_rock     = ["Draw", "Lose", "Win"] #if we choose rock, the list shows opponent choice as [Rock, Paper, Scissors]
outcome_paper    = ["Win", "Draw", "Lose"]
outcome_scissors = ["Lose", "Win", "Draw"]

outcome_combined = [outcome_rock, outcome_paper, outcome_scissors]

# Generate our choice and opponent choice randomly
move_ours = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissors: \n"))
print("You have chosen:")
if   move_ours == 0   : art.print_rock()
elif move_ours == 1   : art.print_paper()
else                  : art.print_scissors()
print("\n")


move_opponent = random.randint(0,2)
print("Computer chose:")
if   move_opponent == 0   : art.print_rock()
elif move_opponent == 1   : art.print_paper()
else                      : art.print_scissors()
print("\n")


# Get the match outcome
outcome_match = outcome_combined[move_ours][move_opponent]

# Print the result
if   outcome_match == "Win"  : print("Congratulation! You won.")
elif outcome_match == "Lose" : print("Too bad! You have lost against this machine!")
else                         : print("Draw - restart the game. Let the best man/machine win.")