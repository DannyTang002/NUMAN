import math

L = [[1,0,0],
     [1,2,0],
     [1,2,3]]

U = [[1,2,3],
     [0,2,3],
     [0,0,3]]

vector = [1,2,3]

def forwardSub(L,vector):

    x = [0,0,0]
    for i in range(len(L)):
        tmp = vector[i]
        for j in range(len(L)):
            tmp-= L[i][j]*x[j]
        x[i]=tmp/L[i][i]

    return x

def backwardSub(U, vector):
    x = [0, 0, 0]
    for i in reversed(range(len(U))):
        tmp = vector[i]
        for j in range(i+1, len(U)):
            tmp -= U[i][j] * x[j]
        x[i] = tmp / U[i][i]

    return x
    

    





print(forwardSub(L,vector))
print(backwardSub(U,vector))



