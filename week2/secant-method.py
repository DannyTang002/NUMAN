import math

def func(x):
    return math.e**x+math.sin(x)-4

def secantMethod(x0,x1):
    f = 0
    while(abs(x1-x0)>1e-6):
        f = (func(x1)*(x1-x0))/(func(x1)-func(x0))
        x0 = x1
        x1 = x1-f
    return x1


print(secantMethod(1,2))