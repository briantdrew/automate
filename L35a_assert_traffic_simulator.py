# this next is the intersection at market and 2nd street
# ns = north-south and ew = east west facing traffic
market_2nd = {'ns': 'green', 'ew': 'red'}

# function to switch the lights

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
#even though there is no bug, it's hard to catch in the above that one
# direction of traffic is yellow light while the other is green
# so we can use an assert like this...
# I assert that this statement always holds true and if not there is 
#something wrong so throw the assert exception so we can figure it out
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switchLights(market_2nd)