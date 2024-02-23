import math

def jacobi():
   
    x0 = [0,0,0,0,0,0]
    x = [0,0,0,0,0,0]
   

    n = len(A)

    norm = 0

    for o in range(6):
        for i in range(n): 
            sum_term = sum(A[i][j] * x0[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_term) / A[i][i]
        x0 = x
        norm = math.sqrt(sum(x0[i]**2 for i in range(n)))

    print(x)

def gaussSeidel(A,b):

    n = len(A)
    x = [0,0,0,0]
  
    for k in range(10000000000):
        for i in range(n): 
            d = b[i]
            for j in range(n):
                if(j!=i):
                    d-=A[i][j]*x[j]
            x[i] = d/A[i][i]
        norm = math.sqrt(sum(x[i]**2 for i in range(n)))
    print(x)
    

    

A = [[3,1,-1],
     [2,4,1],
     [-1,2,5]]

bA = [4,1,1]


B=[[1,1.0001],
   [1.0001,1]]
C=[[1.0001,1],
   [1,1.0001]]
bb = [2,3]

#jacobi()
gaussSeidel(C,bb)
        
            

