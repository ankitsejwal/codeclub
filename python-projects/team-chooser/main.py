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

    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print('Players left: ', players)

print(teamA)
print(teamB)
