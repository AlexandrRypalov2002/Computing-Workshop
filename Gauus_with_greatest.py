from math import *
from fractions import *
import copy

def make_ed_matrix(e, size):
    for i in range(size):
        e.append([])
        for j in range(size):
            if j == i:
                e[i].append(1)
            else:
                e[i].append(0)

def print_matrix(m):
    for i in range(len(m)):
        print(m[i])

def find_greatest(m, i, j, g):
    n = 0
    for s in range(len(m[i])):
        if s < i:
            continue
        else:
            if abs(m[s][j]) > g:
                n = s
                g = m[s][j]
            else:
                continue
    return n

def swap_strings(m, f, str_1, str_2):
    m[str_1], m[str_2] = m[str_2], m[str_1]
    f[str_1], f[str_2] = f[str_2], f[str_1]

def gauss_method_extended(m, f, size): #c is (-1)**(n-1) where n is number of string exchanging
    global c
    i = 0
    j = 0
    low = -inf
    while i < size:
        if i != size-1:
            gr = find_greatest(m, i, j, low)
            if m[gr][j] == 0:
                i += 1
                j += 1
                continue
            if gr != i:
                swap_strings(m, f, i, gr)
                c *= -1
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
    #for i in range(s, 0, -1):
        #print("x_{0} is {1}".format(s-i+1, a[i-1]))

def count_det(m, w, c):
    d = 1
    for i in range(w):
        d *= m[i][i]
    return d*c

def find_back_matrix(m_b, m_back, a, e, w):
    i = 0
    while i < w:
        a.clear()
        m_c = copy.deepcopy(m_b)
        gauss_method_extended(m_c, e[i], w)
        count_x(m_c, e[i], a, w)
        for j in range(0, w, +1):
            m_back[j].append(a[-j - 1])
        i += 1

matrix = []
answers = []
matrix_back = []
w = int(input())
for i in range(w):
    matrix.append([])
    matrix_back.append([])
    matrix[i] = list(map(Fraction, input().split()))
free = list(map(float, input().split()))
matrix_b = copy.deepcopy(matrix)

ed = []
make_ed_matrix(ed, w)

c = 1
gauss_method_extended(matrix, free, w)
count_x(matrix, free, answers, w)
det = count_det(matrix, w, c)
if det == 0:
    print("Определитель матрицы равен 0, обратной матрицы не существует")
else:
    print("Определитель матрицы {0}".format(det))
    find_back_matrix(matrix_b, matrix_back, answers, ed, w)
    print("Обратная матрица:")
    print_matrix(matrix_back)

for i in range(w):
    matrix_back[i].clear()

#Gauss method for matrix from .txt file
f_matrix = []
f_free = []
f_answers = []
f_matrix_back = []
f_ed = []
with open(r'c:/Tests/test.txt', 'r') as f:
  for line in f:
    f_matrix.append(list(map(Fraction, line.split(' '))))
    f_matrix_back.append([])

t = len(f_matrix[0])
for i in range(len(f_matrix)):
    f_free.append(f_matrix[i][t-1])
    f_matrix[i].pop(t-1)
f_matrix_b = copy.deepcopy(f_matrix)

make_ed_matrix(f_ed, t-1)

c = 1
gauss_method_extended(f_matrix, f_free, t-1)
count_x(f_matrix, f_free, f_answers, t-1)
det = count_det(f_matrix, t-1, c)
if det == 0:
    print("Определитель равен 0, обратной матрицы не существует")
else:
    print("Определитель матрицы {0}".format(det))
    find_back_matrix(f_matrix_b, f_matrix_back, f_answers, f_ed, t-1)
    print("Обратная матрица:")
    print_matrix(f_matrix_back)