def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))

def subtract_vectors(vec1, vec2):
    return [x - y for x, y in zip(vec1, vec2)]

def norm(vector):
    return sum(x ** 2 for x in vector) ** 0.5




def clgs(A):
    m = len(A)
    n = len(A[0])
    Q = [[0] * n for _ in range(m)]
    R = [[0] * n for _ in range(n)]

    for j in range(n):
        y = [row[j] for row in A]
        for i in range(j):
            dot_product_val = dot_product(Q[i], y)
            R[i][j] = dot_product_val
            y = subtract_vectors(y, [x * dot_product_val for x in Q[i]])
        norm_y = norm(y)
        R[j][j] = norm_y
        Q = [[y[k] / norm_y if R[j][j] != 0 else 0 for k in range(m)] for _ in range(m)]

    return Q, R

def matrix_multiply(Q, R):
    m = len(Q)
    n = len(R[0])
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(R)):
                result[i][j] += Q[i][k] * R[k][j]
    return result

# Data points
data_points = [
    (0, 1, 3),
    (0, 1, 2),
    (1, 0, 3),
    (1, 0, 4),
    (1, 2, 6)
]

# Constructing the matrix A
A = [[1, x1, x2] for x1, x2, _ in data_points]

# Applying Classical Gram-Schmidt orthogonalization
Q, R = clgs(A)

# Multiply Q with R to get an approximation of A
A_approximation = matrix_multiply(Q, R)

# Print the approximation of A
print("Approximation of A:")
for row in A_approximation:
    print(row)