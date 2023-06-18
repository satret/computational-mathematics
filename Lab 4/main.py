import math
import sys
import matplotlib.pyplot as plt
import numpy as np


def f(x, a3, a2, a1, a0):
    return a3 * x ** 3 + a2 * x ** 2 + a1 * x + a0


def f_exp(x, a1, a0):
    return a1 * np.exp(a0 * x)


def f_log(x, a1, a0):
    return a0 * np.ma.log(x) + a1


def f_pow(x, a1, a0):
    return a1 * x ** a0


# Линейная апроксимация
def linear_approximation(x, y, n):
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    S = 0
    delta = 0
    for i in range(len(x)):
        SX += x[i]
        SXX += x[i] ** 2
        SY += y[i]
        SXY += x[i] * y[i]
    det = SXX * n - SX * SX
    det1 = SXY * n - SX * SY
    det2 = SXX * SY - SX * SXY
    a = round(det1 / det, 5)
    b = round(det2 / det, 5)
    P = []
    eps = []
    for i in range(len(x)):
        P.append(round(x[i] * a + b, 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2 / n
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta)
    return a, b, P, eps, S, delta


def correlation_coefficient(x, y, n):
    x_mean = 0
    y_mean = 0
    for i in range(n):
        x_mean += x[i]
        y_mean += y[i]
    x_mean = x_mean / n
    y_mean = y_mean / n
    numerator_sum = 0
    denominator_sum1 = 0
    denominator_sum2 = 0
    for i in range(n):
        numerator_sum += (x[i] - x_mean) * (y[i] - y_mean)
        denominator_sum1 += (x[i] - x_mean) ** 2
        denominator_sum2 += (y[i] - y_mean) ** 2
    r = round(numerator_sum / (math.sqrt(denominator_sum1 * denominator_sum2)), 5)
    return r


def square_approximation(x, y, n):
    x_sum = 0
    x_square = 0
    x_cube = 0
    x_fourth = 0
    y_sum = 0
    x_y = 0
    x_square_y = 0
    delta = 0
    for i in range(n):
        x_sum += x[i]
        x_square += x[i] ** 2
        x_cube += x[i] ** 3
        x_fourth += x[i] ** 4
        y_sum += y[i]
        x_y += x[i] * y[i]
        x_square_y += x[i] ** 2 * y[i]
    A = np.array([[n, x_sum, x_square],
                  [x_sum, x_square, x_cube],
                  [x_square, x_cube, x_fourth]])
    B = np.array([y_sum, x_y, x_square_y])
    a0, a1, a2 = np.linalg.solve(A, B)
    P = []
    eps = []
    S = 0
    for i in range(len(x)):
        P.append(round(a2 * x[i] ** 2 + x[i] * a1 + a0, 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2 / n
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta)
    return round(a2, 5), round(a1, 5), round(a0, 5), P, eps, S, delta


def cube_approximation(x, y, n):
    x_sum = 0
    x_square = 0
    x_cube = 0
    x_fourth = 0
    x_fifth = 0
    x_sixth = 0
    y_sum = 0
    x_y = 0
    x_square_y = 0
    x_cube_y = 0
    delta = 0
    for i in range(n):
        x_sum += x[i]
        x_square += x[i] ** 2
        x_cube += x[i] ** 3
        x_fourth += x[i] ** 4
        x_fifth += x[i] ** 5
        x_sixth += x[i] ** 6
        y_sum += y[i]
        x_y += x[i] * y[i]
        x_square_y += x[i] ** 2 * y[i]
        x_cube_y += x[i] ** 3 * y[i]
    A = np.array([[n, x_sum, x_square, x_cube],
                  [x_sum, x_square, x_cube, x_fourth],
                  [x_square, x_cube, x_fourth, x_fifth],
                  [x_cube, x_fourth, x_fifth, x_sixth]])
    B = np.array([y_sum, x_y, x_square_y, x_cube_y])  # Вектор (правая часть системы)
    a0, a1, a2, a3 = np.linalg.solve(A, B)
    P = []
    eps = []
    S = 0
    for i in range(len(x)):
        P.append(round(a3 * x[i] ** 3 + a2 * x[i] ** 2 + x[i] * a1 + a0, 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2 / n
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta)
    return round(a3, 5), round(a2, 5), round(a1, 5), round(a0, 5), P, eps, round(S, 5), delta


def exp_approximation(x, y, n):
    ln_y = []
    x_sum = 0
    x_square = 0
    ln_y_sum = 0
    ln_y_sum_x = 0
    delta = 0
    for i in range(n):
        if y[i] <= 0:
            print("Экспоненциальная аппроксимация невозможна.")
            print("Введите корректные данные входящие в ОДЗ")
            return 0, 0, 0, 0, 0, 0
        ln_y.append(math.log(y[i], math.e))
        x_sum += x[i]
        x_square += x[i] ** 2
        ln_y_sum += ln_y[i]
        ln_y_sum_x += ln_y[i] * x[i]
    print(x_sum, x_square, ln_y_sum_x, ln_y_sum)
    A = np.array([[x_square, x_sum],
                  [x_sum, n]])
    B = np.array([ln_y_sum_x, ln_y_sum])

    a0, a1 = np.linalg.solve(A, B)
    a1 = np.exp(a1)
    P = []
    eps = []
    S = 0
    for i in range(len(x)):
        P.append(round(a1 * np.exp(a0 * x[i]), 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2 / n
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta)
    return round(a1, 5), round(a0, 5), P, eps, S, delta


def log_approximation(x, y, n):
    ln_x = []
    ln_x_sum = 0
    ln_x_square = 0
    y_sum = 0
    y_sum_ln_x = 0
    delta = 0
    for i in range(n):
        if x[i] <= 0:
            print("Логарифмическая аппроксимация невозможна.")
            return 0, 0, 0, 0, 0, 0
        ln_x.append(math.log(x[i], math.e))
        ln_x_sum += ln_x[i]
        ln_x_square += ln_x[i] ** 2
        y_sum += y[i]
        y_sum_ln_x += y[i] * ln_x[i]
    print(ln_x_sum, ln_x_square, y_sum_ln_x, y_sum)
    A = np.array([[ln_x_square, ln_x_sum],
                  [ln_x_sum, n]])
    B = np.array([y_sum_ln_x, y_sum])  # Вектор (правая часть системы)
    a0, a1 = np.linalg.solve(A, B)
    P = []
    eps = []
    S = 0
    for i in range(len(x)):
        P.append(round(a0 * math.log(x[i], math.e) + a1, 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta / n)
    return round(a1, 5), round(a0, 5), P, eps, S, delta


def pow_approximation(x, y, n):
    ln_x = np.array([])
    ln_y = np.array([])
    delta = 0
    for i in range(n):
        if x[i] <= 0 or y[i] <= 0:
            print("Степенная аппроксимация невозможна.")
            return 0, 0, 0, 0, 0, 0
        ln_x = np.append(ln_x, math.log(x[i], math.e))
        ln_y = np.append(ln_y, math.log(y[i], math.e))

    A = np.array([  # Матрица (левая часть системы)
        [sum(ln_x ** 2), sum(ln_x)],
        [sum(ln_x), n]
    ])
    b = np.array([sum(ln_x * ln_y), sum(ln_y)])  # Вектор (правая часть системы)

    a0, a1 = np.linalg.solve(A, b)
    a1 = np.exp(a1)

    P = []
    eps = []
    S = 0
    for i in range(len(x)):
        P.append(round(a1 * x[i] ** a0, 5))
        eps.append(round(y[i] - P[i], 5))
        delta = delta + eps[i] ** 2 / n
    for i in range(n):
        S += round(eps[i] ** 2, 5)
    delta = np.sqrt(delta)
    return round(a1, 5), round(a0, 5), P, eps, S, delta


def main():
    print("Выберите формат ввода")
    print("1) Ввод с файла")
    print("2) Ввод с клавиатуры")
    inp = int(input())
    if inp == 1:
        print("Выберите файл для запуска: ")
        print("1) linear")
        print("2) square")
        print("3) cube")
        print("4) exp")
        print("5) log")
        print("6) pow")
        file_num = int(input())
        if file_num == 1:
            file = 'linear'
        elif file_num == 2:
            file = 'square'
        elif file_num == 3:
            file = 'cube'
        elif file_num == 4:
            file = 'exp'
        elif file_num == 5:
            file = 'log'
        elif file_num == 6:
            file = 'pow'
        else:
            print("Неправильный ввод, по умолчанию выбран файл exp")
            file = 'square'
        with open(file, 'r') as file:
            n = int(file.readline())
            x = list(map(float, file.readline().split()))
            y = list(map(float, file.readline().split()))
    else:
        print("Введите количество исходных данных (от 8 до 12)")
        n = int(input())
        print("Введите исходные данные x")
        x = [float(el) for el in input().split()]
        print("Введите исходные данные y")
        y = [float(el) for el in input().split()]
    print(x)
    print(y)
    s = []
    method_names = []
    x = np.array(x)
    y = np.array(y)
    max_x = max(x)
    max_y = max(y)
    min_y = min(y)
    min_x = min(x)
    right_edge = max_x + 2
    left_edge = min_x - 2
    print("")
    print("Линейная апроксимация")
    method_names.append("Линейная апроксимация")
    a, b, P, eps, S, delta = linear_approximation(x, y, n)
    print("Коэффициенты: ", a, b)
    print("Значения P: ", ' '.join(map(str, P)))

    print("Значения eps: ", ' '.join(map(str, eps)))
    print("Мера отклонения S: ", S)
    print("среднеквадратическое отклонение: ", delta)
    s.append(delta)

    x_graph = np.linspace(left_edge, right_edge, 100)
    y_graph = f(x_graph, 0, 0, a, b)
    plt.plot(x_graph, y_graph)
    plt.scatter(x, y, color='red', marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Линейная апроксимация")
    plt.show()

    print("коэфициент корреляции: ", correlation_coefficient(x, y, n))
    print("")
    print("Квадратичная апроксимация")
    method_names.append("Квадратичная апроксимация")
    a2, a1, a0, P, eps, S, delta = square_approximation(x, y, n)
    print("Коэффициенты: ", a2, a1, a0)
    print("Значения P: ", ' '.join(map(str, P)))

    print("Значения eps: ", ' '.join(map(str, eps)))
    print("Мера отклонения S: ", S)
    print("среднеквадратическое отклонение: ", delta)
    s.append(delta)

    x_graph = np.linspace(left_edge, right_edge, 100)
    y_graph = f(x_graph, 0, a2, a1, a0)
    plt.plot(x_graph, y_graph)
    plt.scatter(x, y, color='red', marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Квадратичная апроксимация")
    plt.show()

    print("")
    print("Кубическая апроксимация")
    method_names.append("Кубическая апроксимация")
    a3, a2, a1, a0, P, eps, S, delta = cube_approximation(x, y, n)
    print("Коэффициенты: ", a3, a2, a1, a0)
    print("Значения P: ", ' '.join(map(str, P)))

    print("Значения eps: ", ' '.join(map(str, eps)))
    print("Мера отклонения S: ", S)
    print("среднеквадратическое отклонение: ", delta)
    s.append(delta)

    x_graph = np.linspace(left_edge, right_edge, 100)
    y_graph = f(x_graph, a3, a2, a1, a0)
    plt.plot(x_graph, y_graph)
    plt.scatter(x, y, color='red', marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Кубичсекая апроксимация")
    plt.show()

    print("")
    print("Экспоненциальная апроксимация")
    method_names.append("Экспоненциальная апроксимация")
    a1, a0, P, eps, S, delta = exp_approximation(x, y, n)
    if a1 == 0:
        print("Экспоненциальная аппроксимация невозможна.")
    else:
        print("Коэффициенты: ", a1, a0)
        print("Значения P: ", ' '.join(map(str, P)))
        print("Значения eps: ", ' '.join(map(str, eps)))
        print("Мера отклонения S: ", S)
        print("среднеквадратическое отклонение: ", delta)
        s.append(delta)

        x_graph = np.linspace(left_edge, right_edge, 100)
        y_graph = f_exp(x_graph, a1, a0)
        plt.plot(x_graph, y_graph)
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Экспоненциальная апроксимация")
        plt.show()


    print("")
    print("Логарифмическая апроксимация")
    method_names.append("Логарифмическая апроксимация")
    a1, a0, P, eps, S, delta = log_approximation(x, y, n)
    if a1 == 0:
        print("Логарифмическая аппроксимация невозможна")
    else:
        print("Коэффициенты: ", a1, a0)
        print("Значения P: ", ' '.join(map(str, P)))

        print("Значения eps: ", ' '.join(map(str, eps)))
        print("Мера отклонения S: ", S)
        print("среднеквадратическое отклонение: ", delta)
        s.append(delta)

        y_graph = np.zeros(100)
        x_graph = np.linspace(0, right_edge, 100)  # Пример: значения от 1 до 10 с шагом 0.1
        # for i in range(n):
        #     y_graph[i] = f_log(x[i], a1, a0)
        y_graph = f_log(x_graph, a1, a0)
        # y_graph = a0 * np.log(x_graph) + a1
        plt.plot(x_graph, y_graph)
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Логарифмическая апроксимация")
        plt.show()


    print("")
    print("Степенная апроксимация")
    method_names.append("Степенная апроксимация")
    a1, a0, P, eps, S, delta = pow_approximation(x, y, n)
    if a1 == 0:
        print("Экспоненциальная аппроксимация невозможна.")
    else:
        print("Коэффициенты: ", a1, a0)
        print("Значения P: ", ' '.join(map(str, P)))
        print("Значения eps: ", ' '.join(map(str, eps)))
        print("Мера отклонения S: ", S)
        print("среднеквадратическое отклонение: ", delta)
        s.append(delta)

        y_graph = np.zeros(100)
        x_graph = np.linspace(0, right_edge, 100)
        y_graph = f_pow(x_graph, a1, a0)
        plt.plot(x_graph, y_graph)
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Степенная апроксимация")
        plt.show()


    min_mera = s[1]
    min_index = 1
    print(s)
    for i in range(len(s)):
        if s[i] < min_mera:
            min_mera = s[i]
            min_index = i
    print("Лучшая апроксимация у метода ", method_names[min_index], " среднеквадратическое отклонение равна: ", min_mera)


if __name__ == '__main__':
    main()
