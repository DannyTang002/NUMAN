import math 

def function(x):
    return x**3+4*x+6


def bisectionSearch(x0, x1):
    k = 0
    while abs(x0-x1) >= 1e-8:
        k=k+1
        mid = (x0+x1)/2
        f = function(mid)
        if abs(f)<=1e-8 :
            return (mid,k)
        elif f*function(x0)<0:
            x1=mid
        else: 
            x0=mid




result = bisectionSearch(-2,-1)

print(result)