import math
import sys
import matplotlib.pyplot as plt
import os
from decimal import Decimal

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# Метод Эйлера
# Усовершенствованный метод Эйлера,
# Адмаса

# solve_ode([x0, x1, x2... xn], y0)

function_choice = 0


def solve_ode(x, y):
    return solve_ivp(f, [x[0], x[-1]], [y], t_eval=x).y[0]


def frange(x0, xn, step):
    current_value = x0
    while current_value < xn + step / 2:
        step = round(step, 5)
        yield round(current_value, 5)
        current_value += step


def f(x, y):
    if function_choice == 1:
        return x + y
    elif function_choice == 2:
        return x ** 2 - 2 * y
    else:
        return x + np.cos(3 * y / 5)


def next_y(x, y, h):
    return y + h * f(x, y)


def newton(x0, y0, xn, h):
    for i in frange(x0, xn, h):
        output = "{:.5f} {:.5f}".format(round(i, 5), round(y0, 5))
        y0 = y0 + h * f(i, y0, 1)
        print(output)


def runge_rule(y, h, p, eps):
    if (y ** h - y ** (h / 2)) / (2 ** p - 1) <= eps:
        return True
    else:
        return False


def euler(x0, y0, xn, h, eps):
    results_x, results_y, results_fn = np.array([]), np.array([]), np.array([])
    y = y0
    for i in frange(x0, xn, h):
        results_x = np.append(results_x, round(i, 5))
        results_y = np.append(results_y, round(y, 5))
        y = y + h * f(i, y)
    return results_x, results_y


def improved_euler(x0, y0, xn, h, eps):
    results_x, results_y, results_fn = np.array([]), np.array([]), np.array([])
    y = y0
    for i in frange(x0, xn, h):
        results_x = np.append(results_x, round(i, 5))
        results_y = np.append(results_y, round(y, 5))
        results_fn = np.append(results_y, round(f(i, y), 5))
        next_x = i + h
        y = y + (h / 2) * (f(i, y) + f(next_x, y + h * f(i, y)))
    return results_x, results_y, results_fn


def adams(x0, y0, xn1, h, eps):
    y = y0
    xn, yn, fn = improved_euler(x0, y, x0 + 4 * h, h, eps)
    print(xn)
    index = 3
    n = (xn1 - x0) / h
    while index < n - 1:
        predictor = yn[-1] + h / 24 * (55 * fn[-1] - 59 * fn[-2] + 37 * fn[-3] - 9 * fn[-4])
        corrector = yn[-1] + h / 24 * (9 * f(xn[-1] + h, predictor) + 19 * fn[-1] - 5 * fn[-2] + fn[-3])

        while abs(predictor - corrector) > eps:
            predictor = corrector
            corrector = yn[-1] + h / 24 * (9 * f(xn[-1] + h, predictor) + 19 * fn[-1] - 5 * fn[-2] + fn[-3])

        xn = np.append(xn, xn[-1] + h)
        yn = np.append(yn, corrector)
        fn = np.append(fn, f(xn[-1], yn[-1]))
        index += 1
    return xn, yn, fn

def main():
    global function_choice
    function_choice = int(input("Выберите функцию:\n1) y' = x + y\n2) y' = x ^ 2 - 2 * y\n3) y' = x + cos(3 * y / 5)\n"))
    y0 = float(input("Введите y0: "))
    x0 = float(input("Введите x0: "))
    xn = float(input("Введите правый интервал игтегрирования: "))
    h = float(input("Введите шаг: "))
    eps = float(input("Введите точность: "))
    print("Метод Эйлера\n")
    x_list = np.array([])
    y_list = np.array([])
    x_euler, y_euler = euler(x0, y0, xn, h, eps)
    # print(len(x_list))
    for i in range(len(x_euler)):
        output = "{:.5f} {:.5f}".format(round(x_euler[i], 5), round(y_euler[i], 5))
        print(output)
    print("Усовершенствованный метод Эйлера\n")
    x_euler_imp, y_euler_imp, fn_euler_imp = improved_euler(x0, y0, xn, h, eps)
    for i in range(len(x_euler_imp)):
        output = "{:.5f} {:.5f}".format(round(x_euler_imp[i], 5), round(y_euler_imp[i], 5))
        print(output)
    x_correct = np.linspace(x0, xn, 100)
    y_correct = solve_ode(x_correct, y0)
    print("Точное решение")
    for i in range(len(x_correct)):
        output = "{:.5f} {:.5f}".format(round(x_correct[i], 5), round(y_correct[i], 5))
        print(output)
    print("метод Адамса")
    x_adams, y_adams, fn_adams = adams(x0, y0, xn, h, eps)
    for i in range(len(x_adams)):
        output = "{:.5f} {:.5f}".format(round(x_adams[i], 5), round(y_adams[i], 5))
        print(output)

    plt.plot(x_euler, y_euler, label='Метод эйлера')  # эйлер
    plt.plot(x_euler_imp, y_euler_imp, label='Усовершенствованный метод эйлера')  # усоверш эйлер
    plt.plot(x_adams, y_adams, label='Адамс')  # усоверш эйлер
    plt.plot(x_correct, y_correct, label='Точное решение')
    print(len(x_euler), len(x_euler_imp), len(x_adams), len(x_correct))
    plt.title('Точное решение')
    plt.legend()
    plt.show()
    print("Эйлер; Усовершенствованный Эйлер; Адамс; Точное решение: ", y_euler[-1], y_euler_imp[-1], round(y_adams[-1], 5),
          round(y_correct[-1], 5))
#Эйлер; Усовершенствованный Эйлер; Адамс; Точное решение:  60.94827 61.9347 59.68443 57.43692

if __name__ == '__main__':
    main()
