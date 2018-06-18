#!bin/python3

from random import choice

players = ["Harry", "Hermione", "Jue", "Patrick"]
print(players)

teamA = []

playerA = choice(players)
teamA.append(playerA)
players.remove(playerA)

teamB = []

playerB = choice(players)
teamB.append(playerB)
players.remove(playerB)

print('Players left: ', players)