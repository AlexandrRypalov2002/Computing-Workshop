from fractions import Fraction

def mult_matr(m, x, f, w):
    for i in range(w):
        s = 0
        for j in range(w):
            s += m[i][j]*x[j]
        f[i] = s

def swap_strings(m, f, str_1, str_2):
    m[str_1], m[str_2] = m[str_2], m[str_1]
    f[str_1], f[str_2] = f[str_2], f[str_1]

def gauss_method(m, f, size):
    i = 0
    j = 0
    while i < size:
        if m[i][j] == 0:
            for h in range(i, size):
                if m[h][j] != 0:
                    swap_strings(m, f, i, h)
                    break
        for a in range(i+1, size):
            div = m[a][j]/m[i][j]
            for w in range(size):
                m[a][w] -= (m[i][w]*div)
            f[a] -= (f[i]*div)
        i += 1
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

matrix = []
free = []
answers = []
w = int(input())

for i in range(w):
    matrix.append(list(map(Fraction, input().split())))
free = list(map(Fraction, input().split()))

gauss_method(matrix, free, w)
count_x(matrix, free, answers, w)