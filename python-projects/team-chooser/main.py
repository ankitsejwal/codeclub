#!bin/python3

from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

teamA = []
teamB = []

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

teamA_file = open('teamA.txt', 'w')
for player in teamA:
    teamA_file.writelines(player + '\n')

print(teamA)

teamB_file = open('teamB.txt', 'w')
for player in teamB:
    teamB_file.writelines(player + '\n')

print(teamB)
