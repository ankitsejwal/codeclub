from classes import *

targetPlanet = input("Type the name of a planet: ")
myPlanet = ourSolarSystem.getPlanet(targetPlanet)

# validating user input
if myPlanet is not None:
    print(myPlanet)
else:
    print(targetPlanet + ' is not a planet!')