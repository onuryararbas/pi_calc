import math
import random

def distGiveCord(x,y):
    return math.sqrt((x**2) + (y**2))


def isInCirc(r):
    total = 0
    inCirc = 0

    for j in range(10000000):
        #random x and random y between -1 and 1
        xCord = random.uniform(-1,1)
        yCord = random.uniform(-1,1)
        #the chance of you hitting a circle of radius 1 inside of a total square of side lengths 2x2 is pi/4
        # we can use this to calculate pi.
        total += 1
        
        if(distGiveCord(xCord, yCord) <= r):
            inCirc += 1
            

    print((inCirc/total)*4)
        
    

isInCirc(1)

