import math
import numpy as np
import matplotlib.pyplot as plt


num_points = 50

def f(x):
    return np.e**(-x**2)


x = [-1+2*i/num_points for i in range(num_points)]
y = [f(xi) for xi in x]



def lagrangeBasis(xk, y, k):
    basis = [(xk - x[i]) / (x[k] - x[i]) for i in range(num_points) if k != i]
    return np.prod(basis, axis=0) * y[k]

def interpolate(xk, y):
    basis = [lagrangeBasis(xk, y, k) for k in range(num_points)]
    return np.sum(basis, axis=0)

interpolated_values = [interpolate(xi, y) for xi in x]
print(interpolated_values)
plt.plot(x, y, 'bo', label='Original Points')
plt.plot(x, interpolated_values, 'r-', label='Interpolated Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lagrange Interpolation')
plt.show()