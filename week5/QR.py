def transpose(A):
    
    num_rows = len(A)
    num_cols = len(A[0])

    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = A[i][j]

    return transposed_matrix


def matrix_multiplication(A, B):
    rows1, cols1 = len(A), len(A[0])
    rows2, cols2 = len(B), len(B[0])
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += A[i][k] * B[k][j]

    return result

def leastSquaresQR(Q,R, b): 
    QT = transpose(Q)
    QTb = matrix_multiplication(QT,b)
  
    x = gaussian_elimination(R,QTb)
    print("hej")
    print(x)


def gaussian_elimination(A, b):
    n = len(A[0])  
    m = len(A)     
    for i in range(n):
        max_row = i
        for j in range(i+1, m):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        
        for j in range(i+1, m):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j][0] -= factor * b[i][0]

    
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            return None  
        x[i] = b[i][0] / A[i][i]
        for j in range(i):
            b[j][0] -= A[j][i] * x[i]

    return x
m =  8
N =3



def matrix_multiplication(A, B):
    rows1, cols1 = len(A), len(A[0])
    rows2, cols2 = len(B), len(B[0])
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += A[i][k] * B[k][j]

    return result


def QR(A):
    m, n = len(A), len(A[0])
    Q = [[0.0] * n for _ in range(m)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        y = [A[k][j] for k in range(m)]
        for i in range(j):
            R[i][j] = sum(Q[k][i] * y[k] for k in range(m))
            for k in range(m):
                y[k] -= R[i][j] * Q[k][i]
        R[j][j] = sum(y[k] ** 2 for k in range(m)) ** 0.5
        for k in range(m):
            Q[k][j] = y[k] / R[j][j]
    return Q, R
A = [[1,0,1],[1,0,1],[1,1,0],[1,1,0],[1,1,2]]
b = [[3],[2],[3],[4],[6]]
Q, R = QR(A)

leastSquaresQR(Q,R,b)



