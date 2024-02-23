import math


def x0(x1,x2,x3):
    x = [
        x1**2-2*x1+x2**2-x3+1,
        x1*x2**2-x1-3*x2+x2*x3+2,
        x1*x3**2-3*x3+x2*x3**2+x1*x2
    ]
    return x

def jacobian(x1,x2,x3):
    x = [
        [2*x1 - 2, 2*x2, -1],
        [x2**2 - 1, 2*x1*x2 - 3 + x3, x2],
        [x3**2+x2, x3**2 + x1, 2*x1*x3 + 2*x2*x3 - 3]
    ]
    return x 





def solve_linear_system(matrix, vector):
    n = len(vector)
    solution = [0.0] * n  
    
    
    for i in range(n):
        max_index = i
        for k in range(i+1, n):
            if abs(matrix[k][i]) > abs(matrix[max_index][i]):
                max_index = k
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
        vector[i], vector[max_index] = vector[max_index], vector[i]
        
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            vector[k] -= factor * vector[i]
    
    for i in range(n - 1, -1, -1):
        solution[i] = vector[i]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
        solution[i] /= matrix[i][i]

    return solution



def newton_method(x1, x2, x3, tol=1e-6):
    xn = [x1, x2, x3]
    r = [1, 1, 1] 
    for i in range(6):
        e = math.sqrt(sum((rn - xn_val) ** 2 for rn, xn_val in zip(r, xn)))
        f0 = x0(*xn)
        if math.sqrt(sum(val**2 for val in f0)) < tol:
            break
        j0 = jacobian(*xn)
        print(j0)
        dx = solve_linear_system(j0, [-val for val in f0])
        print(dx)
        xn = [xn[i] + dx[i] for i in range(len(xn))]
        ek = math.sqrt(sum((rn - xn_val) ** 2 for rn, xn_val in zip(r, xn)))
        print(ek/e)
    return xn

x1 = 1
x2 = 2
x3 = 3

root = newton_method(x1, x2, x3)
print("Root:", root)
