###   System:
#     x + x*(y**3) = 9
#     x*y + x*(y**2) = 6
import numpy as np
from math import sqrt

iter = []

def Jacobi(x):
    Jac_matr = [[1+x[1]**3, 3*x[0]*x[1]],
                [x[1]+x[1]**2, x[0]+2*x[0]*x[1]]]
    return np.linalg.inv(Jac_matr)

def matrix_mult_vector(jac, x):
    res = []
    for i in range(len(x)):
        a = 0
        for j in range(len(x)):
            a += jac[i][j]*x[j]
        res.append(a)
    return res

def vector_diff(x_1, x_2):
    res = [0]*len(x_1)
    for i in range(len(x_1)):
        res[i] = x_1[i] - x_2[i]
    return res


def check_to_stop(x_1, x_2, eps):
    res = []
    for i in range(len(x_1)):
        a = abs(x_1[i] - x_2[i])
        res.append(a)
    if max(res) <= eps:
        return True
    else:
        return False

def norm(x_1, x_2):
    res = vector_diff(x_1, x_2)
    a = 0
    for i in range(len(res)):
        a += res[i]**2
    return sqrt(a)

def simple_iteration(x, eps):
    n = 0
    while True:
        Jac_matr = [[(1 + x[1] ** 3), (3 * x[0] * x[1])],
                    [(x[1] + x[1] ** 2), (x[0] + 2 * x[0] * x[1])]]
        J = np.linalg.inv(Jac_matr)

        for i in range(len(J[0])):
            for j in range(len(J[i])):
                J[i][j] *= 0.9

        f = [x[0] + x[0] * x[1] ** 3 - 9, x[0] * x[1] + x[0] * x[1] ** 2 - 6]
        x_new = vector_diff(x, matrix_mult_vector(J, f))
        if norm(x, x_new) < eps:
            iter.append(n)
            return x_new
        else:
            x = x_new
            n += 1

def Newton_method(x, e):
    n = 0
    while True:
        f = [x[0] + x[0]*x[1]**3 - 9, x[0]*x[1] + x[0]*x[1]**2 - 6]
        x_new = vector_diff(x, matrix_mult_vector(Jacobi(x), f))
        if norm(x, x_new) < eps:
            iter.append(n)
            return x_new
        else:
            x = x_new
            n += 1

print("Enter the margin:")
eps = float(input())
print("Enter the start vector:")
x = list(map(float, input().split()))

ans = simple_iteration(x, eps)
print(*ans)

ans_1 = Newton_method(x, eps)
print(*ans_1)

print("SI - {0} iterations; NM - {1} iterations".format(iter[0], iter[1]))