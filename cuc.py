import random

wins = 0
games = 0 

def game():
    global wins
    global games
    ## AI's randomly generated move.
    x = random.randint(1,3)
    if x == 1:
     x = 'rock'
    elif x == 2:
     x = 'paper'
    elif x == 3:
     x = 'scissors'

## Asking for your move.
y = input("\n What's your move?:")
while y != 'rock' and y != 'paper' and y != 'scissors' and y != 'r' and y != 'p' and y != 's':
    print("\n Please pick a VALID move")
    y = input("\n What's your move?:")

##assigning your shortcut key to the move.
if y == 'r':
     y = 'rock'
elif y == 'p':
     y = 'paper'
elif y == 's':
     y = 'scissors'

## Checking who won.
if x == y:
    print("\n It's a tie")
    games = games + 1
elif x == 'rock' and y == 'scissors':
    print("\n You win!")
    games = games + 1
    wins = wins + 1
elif x == 'paper' and y == 'rock':
    print("\n You win!")
    games = games + 1
    wins = wins + 1
elif x == 'scissors' and y == 'paper':
    print("\n You win!")
    games = games + 1
    wins = wins + 1
else:
    print("\n You lose!")
    games = games + 1

game()
z = input("\n play again?")
while z != 'no' and z != 'n':
    game()
    z = input("\n Play again?")

ratio = 100*wins//games

print("\n You played ", games, "and won ", wins, "games.")

print("\n Your win ratio is ", ratio,)

input("\n Press Enter to Exit")