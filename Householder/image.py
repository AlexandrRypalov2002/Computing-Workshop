from math import *

def sign(a):
    if a < 0:
        return -1
    elif a > 0:
        return 1
    else:
        return -1

def back_to_one(t, s):
    for i in range(s):
        for j in range(s):
            if j == i:
                t[i][j] = 1
            else:
                t[i][j] = 0

def vector_diff(a, b, d):
    res = []
    for i in range(len(a)):
        res.append(a[i] + d*b[i])
    return res

def vector_mult_rational(a, r):
    res = []
    for i in range(len(a)):
        res.append(a[i]*r)
    return res

def vector_divide(a, div):
    res = []
    for i in range(len(a)):
        res.append(a[i]/div)
    return res

def matrix_mult_rational(m, r, s):
    for i in range(s):
        for j in range(s):
            m[i][j] = r*m[i][j]
    return m

def matrix_diff(t, h, s):
    for i in range(s):
        for j in range(s):
            t[i][j] = t[i][j] - h[i][j]
    return t

def matrix_mult(h, m, s):
    res = []
    for i in range(s):
        res.append([])
        for j in range(s):
            res[i].append(0)
    for i in range(s):
        for j in range(s):
            for k in range(s):
                res[i][j] += h[i][k]*m[k][j]
    return res

def matrix_mult_vector(t, f, s):
    res = [0]*s
    for i in range(s):
        for j in range(s):
            res[i] += t[i][j]*f[j]
    return res

def norm(a, s):
    n = 0
    for i in range(s):
        n += pow(a[i], 2)
    n = sqrt(n)
    return n

def get_m(w):
    matr = []
    for i in range(len(w)):
        matr.append([])
        for j in range(len(w)):
            matr[i].append(w[i]*w[j])
    return matr

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

def image_matrix(m, w, f, t, size):
    i = 0
    while i < size:
        e = []
        for k in range(size):
            if k == i:
                e.append(1)
            else:
                e.append(0)
        a = [0]*size
        for k in range(i, size):
            a[k] = m[k][i]
        d = sign(m[i][i])
        n = norm(a, size)
        e = vector_mult_rational(e, n)
        w = vector_diff(a, e, d)
        n_d = norm(w, size)
        w = vector_divide(w, n_d)
        h = get_m(w)
        h = matrix_mult_rational(h, 2, size)
        t = matrix_diff(t, h, size)
        m = matrix_mult(t, m, size)
        f = matrix_mult_vector(t, f, size)
        back_to_one(t, size)
        i += 1
    v = [m, f]
    return v

size = int(input())
matrix = []
free = []
t = []
w = [0]*size
answers = []
for i in range(size):
    t.append([])
    for j in range(size):
        if i == j:
            t[i].append(1)
        else:
            t[i].append(0)

for i in range(size):
    matrix.append(list(map(float, input().split())))
free = list(map(float, input().split()))

values = image_matrix(matrix, w, free, t, size)
matrix = values[0]
free = values[1]
count_x(matrix, free, answers, size)
print(*answers)