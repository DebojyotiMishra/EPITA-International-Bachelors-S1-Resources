## Rock, Paper, Scissors
import random
score = 0
game = 1
max_games = 3

while game <= max_games :

    player = None
    computer = random.choice(['rock', 'paper', 'scissors'])

    while player not in ['rock', 'paper', 'scissors'] :
        player = input(f"Player's move - Rock, Paper, Scissors:").lower()

    print(f"Computer played {computer}")

    if player == computer :
        print("It's a draw ! Replay.", end='\n\n')
        continue
    if (player == 'rock' and computer =='scissors') or (player == 'paper' and computer =='rock') or (player == 'scissors' and computer =='paper'):
        print(f"Player won the round {game}!", end='\n\n')
        score+=1
        game+=1
    else :
        print(f"Computer won the round {game}!", end='\n\n')
        score-=1
        game+=1

if score > 0 :
    print('Player won the ShiFuMi Game.')
else :
    print('Computer won the ShiFuMi Game.')

## Ball Movement
import os

width = 10
height = 10
ball_x = 5
ball_y = 5

while True:
    os.system('cls')

    for y in range(height):
        for x in range(width):
            if x == ball_x and y == ball_y:
                print("O", end="")
            else:
                print(".", end="")
        print()

    command = input("Enter direction (W/A/S/D) or Q to quit: ").upper()

    if command == "W" and ball_y > 0:
        ball_y -= 1
    elif command == "A" and ball_x > 0:
        ball_x -= 1
    elif command == "S" and ball_y < height - 1:
        ball_y += 1
    elif command == "D" and ball_x < width - 1:
        ball_x += 1
    elif command == "Q":
        print("Thanks for playing !")
        break