import math 

def func(x): 
    return math.cos(x)**2

def pointfixed(x):
    k = 0
    for i in range(200):
        x = func(x)

    return x



print(pointfixed(0.5))