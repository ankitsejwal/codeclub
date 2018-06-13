from classes import *

targetPlanet = input("Type the name of a planet: ")
myPlanet = ourSolarSystem.getPlanet(targetPlanet)

# validating user input
if myPlanet is not None:
    moons = myPlanet.get_moons()
    if len(moons) > 0:
        print(moons)
    else:
        print(targetPlanet + ' has no moons!')
else:
    print(targetPlanet + ' is not a planet!')