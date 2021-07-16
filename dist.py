import math
def distGiveCord(x,y):
    return math.sqrt((x**2) + (y**2))

def isInCirc(r,x,y):
    inCirc = 0
    total = 0
    for x in range(10000):
        ++total
        if(distGiveCord(x,y) == r):
            ++inCirc
    rat = inCirc/total
    # rat currently solves for pi/4
    print(rat*4)

