#!bin/python3

from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

# setting up empty lists
teamA = []
teamB = []
teamC = []

while len(players) > 0:

    playerA = choice(players)
    print(playerA)
    teamA.append(playerA)
    players.remove(playerA)
    print('Players left: ', players)

    if players == []:
        break

    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left: ', players)

    if players == []:
        break

    playerC = choice(players)
    teamC.append(playerC)
    players.remove(playerC)
    
# Saving results in text files
teamA_file = open('teamA.txt', 'w')
for player in teamA:
    teamA_file.writelines(player + '\n')

teamB_file = open('teamB.txt', 'w')
for player in teamB:
    teamB_file.writelines(player + '\n')

teamC_file = open('teamC.txt', 'w')
for player in teamC:
    teamC_file.writelines(player + '\n')

# Printing team results
print('TeamA: ', teamA)
print('TeamB: ', teamB)
print('TeamC: ', teamC)
