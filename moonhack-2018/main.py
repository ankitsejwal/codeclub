from classes import *

targetPlanet = input("Type the name of a planet: ")
capitalPlanet = targetPlanet.capitalize()
myPlanet = ourSolarSystem.getPlanet(capitalPlanet)

# validating user input
if myPlanet is not None:
    moons = myPlanet.get_moons()
    if len(moons) > 0:
        print(moons)
    else:
        print(capitalPlanet + ' has no moons!')
else:
    print(capitalPlanet + ' is not a planet!')