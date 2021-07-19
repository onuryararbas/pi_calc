import math
import random

def distGiveCord(x,y):
    return math.sqrt((x**2) + (y**2))


def isInCirc(r):
    total = 0
    inCirc = 0

    for j in range(10000000):
        #random x and random y between negative radius and positive radius 
        xCord = random.uniform(-r,r)
        yCord = random.uniform(-r,r)
        # the chance of you hitting a circle of radius 1 inside of ...
        # ... a total square of side lengths 2x2 is pi/4 ...
        # ... we can use this to calculate pi.
        total += 1
        
        if(distGiveCord(xCord, yCord) <= r):
            inCirc += 1

        if j % 100 == 0:
            print("Iteration " + str(j) + ": " + str((inCirc/total)*4))
            

    print("final product: " + str((inCirc/total)*4))
        
    

isInCirc(2)

