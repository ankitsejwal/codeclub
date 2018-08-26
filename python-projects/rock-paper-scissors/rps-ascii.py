#!bin/python3

from random import randint

player = input('rock (r), paper (p) or scissor (s)? ')

chosen = randint(1, 3)
if chosen == 1:
    computer = 'r'
    print('O', end=" ")
elif chosen == 2:
    computer = 'p'
    print('___', end=" ")
else:
    computer = 's'
    print('>8', end=" ")

# if player and computer select same item
if computer == player:
    print('DRAW!')
else:
    if player == 'r':
        print('vs O')
        if computer == 'p':
            print('Computer win') 
        else: 
            print('You win')

    if player == 'p':
        print('vs ___')
        if computer == 's':
            print('Computer win') 
        else:
            print("You win")

    if player == 's':
        print('vs >8')
        if computer == 'r':
            print("Computer win") 
        else:
             print("You win")