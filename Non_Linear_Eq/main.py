from math import sin, cos

function_coefs = [1, -12, 41, -30]       # x**3 -12x**2 + 41x - 30 = 0
diff_1 = [3, -24, 41]                    # 3x**2 - 24x + 41
diff_2 = [6, -24]                        # 6x - 24

diff_dict = {1: diff_1, 2: diff_2}
iter_dict = {}

def count_function(x):
    res = 0
    for i in range(len(function_coefs)):
        res += function_coefs[i]*(pow(x, len(function_coefs) - i - 1))
    return res


def count_function_diff(x, n):          #for derivatives
    res = 0
    for i in range(len(diff_dict[n])):
        res += diff_1[i]*(pow(x, len(diff_dict[n]) - i - 1))
    return res


def Newton_Method(x_0, a, b, eps):
    n = 0
    if count_function(a)*count_function(b) < 0 and count_function(x_0)*count_function_diff(x_0, 2) < 0:
        while True:
            x_1 = x_0 - (count_function(x_0)/count_function_diff(x_0, 1))
            n += 1
            if abs(x_1 - x_0) < eps:
                iter_dict["Newton Method"] = n
                return x_1
            else:
                x_0 = x_1

def half_split(a, b, e):
    a_n = a
    b_n = b
    n = 0
    while True:
        c = (a_n + b_n) / 2
        if count_function(c) == 0:
            iter_dict["Half Split Method"] = n
            return c
        if count_function(a_n)*count_function(c) < 0:
            b_n = c
        elif count_function(c)*count_function(b_n) < 0:
            a_n = c
        n += 1
        if abs(a_n - b_n) < e:
            iter_dict["Half Split Method"] = n
            return (a_n + b_n)/2

def iteration_method(x_0, a, b, eps):
    n = 0
    while True:
        x_1 = x_0 - count_function(x_0)*3.3
        n += 1
        if abs(x_1 - x_0) < eps:
            iter_dict["Iteration Method"] = n
            return x_1
        x_0 = x_1

def relaxation_method(x_0, eps):
    n = 0
    while True:
        x_1 = x_0 - count_function(x_0) * 4.34
        n += 1
        if abs(x_1 - x_0) < eps:
            iter_dict["Relaxation Method"] = n
            return x_1
        x_0 = x_1

print("Enter x_0:")
x_0 = float(input())
print("Enter the cut:")
a, b = map(float, input().split())
print("Enter the margin:")
eps = float(input())

x_1 = Newton_Method(x_0, a, b, eps)
x_2 = half_split(a, b, eps)
x_3 = iteration_method(x_0, a, b, eps)
x_4 = relaxation_method(x_0, eps)
print(x_1, x_2, x_3, x_4)

print(iter_dict)