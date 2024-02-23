import math
import numpy as np
import matplotlib.pyplot as plt

num_points = 10

def f(x):
    return np.e**(-x**2)

def chebyshev(k):
    return math.cos((k * math.pi) / num_points)

x = [chebyshev(k) for k in range(num_points)]

xe = [-1+2*i/num_points for i in range(num_points)]
y = [f(xi) for xi in x]

def lagrangeBasis(xk, x, k):
    basis = [(xk - x[i]) / (x[k] - x[i]) for i in range(num_points) if k != i and (x[k] - x[i]) != 0]
    return np.prod(basis, axis=0) * y[k]

def interpolate(xk, x):
    basis = [lagrangeBasis(xk, x, k) for k in range(num_points)]
    return np.sum(basis, axis=0)

interpolated_values = [interpolate(xi, x) for xi in x]
interpolated_values_eq = [interpolate(xi, xe) for xi in xe]

plt.plot(x, y, 'bo', label='Original Points')


cheberror = [f(x[i]) - interpolated_values[i] for i in range(num_points)]
eqError = [f(xe[i]) - interpolated_values_eq[i] for i in range(num_points)]
print(len(cheberror))
plt.plot(x,cheberror ,'r-', label = 'chebyshev error')
plt.plot(x,eqError ,'r-', label = 'chebyshev error')



plt.plot(x, interpolated_values, 'r-', label='Interpolated Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lagrange Interpolation with Chebyshev Nodes')
plt.show()
