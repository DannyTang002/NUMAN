import math 
def func1(x):
    return (2*x+2)**(1/3)

def func2(x):  
    return math.log(7-x)

def func3(x):
    return math.log(4-math.sin(x))


def derivate(x,choice):
    h=1e-8
    value = 0
    if choice==1:
        value = (func1(x+h)-func1(x))/h
    elif choice==2:
        value = (func2(x+h)-func2(x))/h
    else:
        value = (func3(x+h)-func3(x))/h
    return value


def pointfixed(x):
    k = 0
    while abs(func2(x)-x)>=1e-8:
        if derivate(x,2)<1:
            print("this shit is converging")
        k=k+1
        x=func2(x)

    return (k,x)

print(pointfixed(5))