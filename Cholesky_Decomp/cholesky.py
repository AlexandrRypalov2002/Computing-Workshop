from math import sqrt

def count_x_back(m, f, a, s):
    j = 0
    for i in range(s):
        if j == 0:
            a.append(f[i]/m[i][j])
        else:
            for x in range(j):
                f[j] -= m[j][x]*a[x]
            a.append(f[i]/m[i][j])
        j += 1

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

def matrix_multiply(l, l_t, c, w):
    for i in range(w):
        for j in range(w):
            for k in range(w):
                c[i][j] += l[i][k] * l_t[k][j]

def check_symmetry(m, w):
    for i in range(w):
        for j in range(w):
            if j == i:
                continue
            elif m[i][j] == m[j][i]:
                continue
            else:
                return 0
    return 1

def sum(m, l, i):
    s = m[i][i]
    for j in range(i):
        s -= (l[i][j]*l[i][j])
    s = sqrt(s)
    return s

def cholesky_decomp(m, l, w):
    l[0][0] = sqrt(m[0][0])
    for j in range(1, w):
        l[j][0] = (m[j][0]/l[0][0])
    i = 1
    while i < w:
        l[i][i] = sum(m, l, i)
        if i != w - 1:
            for j in range(i+1, w):
                s = 0
                for p in range(i):
                    s += (l[i][p]*l[j][p])
                l[j][i] = (m[j][i] - s)/l[i][i]
        else:
            i += 1
            continue
        i += 1

def matrix_transposition(l, w):
    i = 0
    while i < w:
        for j in range(i, w):
            if j == i:
                continue
            else:
                l[j][i], l[i][j] = l[i][j], l[j][i]
        i += 1

w = int(input())
matrix = []
a_y = []
a_x = []
for i in range(w):
    matrix.append(list(map(float, input().split())))
free = list(map(float, input().split()))

f = check_symmetry(matrix, w)
if f == 0:
    print("Matrix is not symmetric")
else:
    l = [[0]*w for _ in range(w)]

    cholesky_decomp(matrix, l, w)
    count_x_back(l, free, a_y, w)
    matrix_transposition(l, w)
    count_x(l, a_y, a_x, w)
    print(*a_x)
