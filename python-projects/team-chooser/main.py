#!bin/python3

from random import choice

players = ["Harry", "Hermione", "Jue", "Patrick"]
print(players)

teamA = []

playerA = choice(players)
teamA.append(playerA)
players.remove(playerA)
print('Players left: ', players)