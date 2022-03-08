from math import *

def print_matrix(m, size):
    for i in range(size):
        print(matrix[i])

def create_t(t, c, s, i, j):
    t[i][i] = c
    t[j][j] = c
    t[i][j] = s
    t[j][i] = (-1*s)

def t_back_to_one(t):
    for k in range(len(t)):
        for l in range(len(t)):
            if k == l:
                t[k][l] = 1
            else:
                t[k][l] = 0

def matrix_mult(t, m, s):
    res = []
    for i in range(s):
        res.append([])
        for j in range(s):
            res[i].append(0)
    for i in range(s):
        for j in range(s):
            for k in range(s):
                res[i][j] += t[i][k] * m[k][j]
    return res

def matrix_mult_vector(t, f, s):
    res = [0]*s
    for i in range(s):
        for j in range(s):
            res[i] += t[i][j]*f[j]
    return res

def spin_matrix(m, t, f, size):
    i = 0
    while i < (size-1):
        j = i+1
        for l in range(i, size-1):
            c = (m[i][i]/sqrt(m[i][i]**2 + m[l+1][i]**2))
            s = (m[l+1][i]/sqrt(m[i][i]**2 + m[l+1][i]**2))
            create_t(t, c, s, i, j)
            m = matrix_mult(t, m, size)
            f = matrix_mult_vector(t, f, size)
            t_back_to_one(t)
            j += 1
        i += 1
    values = [m, f]
    return values

def count_x(m, f, a, s):
    j = s-1
    for i in range(s, 0, -1):
        if j == s-1:
            if f[i-1] != 0 and m[i-1][j] == 0:
                print("Система несовместна")
                return
            elif f[i-1] == 0 and m[i-1][j] == 0:
                print("Система имеет бесконечное количество решений")
                return
            else:
                a.append(f[i-1]/m[i-1][j])
                j -= 1
        else:
            t = 0
            for x in range(s-1, i-1, -1):
                f[i-1] -= (m[i-1][x]*a[t])
                t += 1
            if f[i-1] != 0 and m[i-1][j] == 0:
                print("Система несовместна")
                return
            elif f[i-1] == 0 and m[i-1][j] == 0:
                print("Бесконечное множество решений")
                return
            a.append(f[i-1]/m[i-1][j])
            j -= 1

size = int(input())
matrix = []
free = []
t = []
answers = []
for i in range(size):
    t.append([])
    for j in range(size):
        if j == i:
            t[i].append(1)
        else:
            t[i].append(0)

for i in range(size):
    matrix.append(list(map(float, input().split())))
free = list(map(float, input().split()))

h = spin_matrix(matrix, t, free, size)
matrix = h[0]
free = h[1]
count_x(matrix, free, answers, size)
print(*answers)
