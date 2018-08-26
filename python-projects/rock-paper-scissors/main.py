#!bin/python3

from random import randint

player = input('rock (r), paper (p) or scissor (s)? ')

chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(player, 'vs', computer)

if computer == player:
    print('DRAW!')
else:
    if player == 'r':
        if computer == 'p':
            print('Computer win') 
        else: 
            print('You win')
    if player == 'p':
        if computer == 's':
            print('Computer win') 
        else:
            print("You win")
    if player == 's':
        if computer == 'r':
            print("Computer win") 
        else:
             print("You win")