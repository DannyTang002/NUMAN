import math



def func(x):
    #return math.e**(math.sin(x)**3)+x**6-2*x**4-x**3-1
    #return x**3-x
    return math.atan(x)

def derivation(x):
    h = 0.00000005
    return (func(x+h)-func(x))/h

def double_derivation(x):
    h = 0.00000005
    return(derivation(x+h)-derivation(x))/h



def checkQuad(root):
    if(derivation(root)!=0):
        m = abs(double_derivation(root)/(2*derivation(root)))
        if(m>0):
            print("it converges quadratically")
        else:
            print("it converges linearly")

    print(root)


def newton(x0):
    xNext = 100
    initial = 0
    k = 0
    while(abs(xNext-initial)>=1e-6):
        k = k+1
        initial = x0
        if(derivation(initial)==0):
            break
        xNext = initial-(func(initial)/derivation(initial))
        x0 = xNext


    root = xNext
    checkQuad(root)
    return (xNext,k)



def newton_50Iteration(x0):
    xNext = 100
    for i in range(50):
        initial = x0
        if(derivation(initial)==0):
            break
        xNext = initial-(func(initial)/derivation(initial))
        x0 = xNext
        print(xNext)

    
newton(5)
#print(newton_50Iteration(0.4472135954999596))

