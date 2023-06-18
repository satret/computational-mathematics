import math
import sys
import matplotlib.pyplot as plt
import os

import numpy as np

def f(x, function_choice):
    if function_choice == 1:
        return np.sin(x)
    if function_choice == 2:
        return np.cos(x)
    if function_choice == 3:
        return x * x - 7 * x + 1


def fact(x):
    if x <= 1:
        return 1
    return x * fact(x - 1)


# Лагранж
def lagrange(arg, x, y):
    n = len(x)
    lagrange_result = 0.0
    for i in range(n):
        term = y[i]
        chisl = 1
        znam = 1
        for j in range(n):
            if i != j:
                chisl *= (arg - x[j])
                #term *= (arg - x[j]) / (x[i] - x[j])
                znam *= (x[i] - x[j])
        term *= chisl / znam
        lagrange_result += term
    return lagrange_result


def gaussian(arg, x, table):  # Многочлен Гаусса
    n = len(x)
    if len(table) % 2 == 0:
        parity = 1
    else:
        parity = 0
    j = len(table) // 2 - parity
    initial_j = j
    gaussian_result = table[j][0]
    h = abs(x[0] - x[1])
    t = (arg - x[j]) / h
    production_t = 1

    for i in range(1, n):
        if i % 2 == 1:
            if arg < x[initial_j]:
                production_t *= (t - i // 2)
                j -= 1
            else:
                production_t *= (t + i // 2)
        else:
            if arg < x[initial_j]:
                production_t *= (t + i // 2)
            else:
                production_t *= (t - i // 2)
                j -= 1
        gaussian_result += production_t * table[j][i] / fact(i)
    return gaussian_result


# Ньютон
def main():
    print("Выберите формат ввода")
    print("1) Ввод с файла\n2) Ввод с клавиатуры\n3) На основе выбранной функции")
    inp = int(input())
    if inp == 1:
        file_num = int(input("Выберите файл:\n1) test1.txt\n2) test2.txt\n3) test3.txt\n"))
        if file_num == 1:
            file = 'test1.txt'
        elif file_num == 2:
            file = 'test2.txt'
        else:
            file = 'test3.txt'
        with open(file, 'r') as file:
            x = list(map(float, file.readline().split()))
            y = list(map(float, file.readline().split()))
            n = len(x)
    elif inp == 2:
        print("Введите исходные данные x")
        x = [float(el) for el in input().split()]
        print("Введите исходные данные y")
        y = [float(el) for el in input().split()]
        n = len(x)
    else:
        print("Выберите функцию:\n1)sin(x)\n2)cos(x)\n3)x^2 - 7x + 1")

        function_choice = int(input())

        a = float(input("Введите границы функций (a): "))
        b = float(input("Введите границы функций (b): "))
        n = int(input("Введите количество точек: "))
        x = np.linspace(a, b, n)
        y = f(x, function_choice)
        print("x:", x)
        print("y:", y)
    if len(x) != len(set(x)):
        print("методы интерполяции не сработают")
        sys.exit()
    # Создание таблицы конечных разностей
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1])

    # Вывод таблицы разностей
    print("Таблица конечных разностей:")
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i + j < len(y):
                print(round(table[i][j], 4), end="\t")
        print()
    print("интервалы x: ", min(x), max(x))
    arg = float(input("Введите аргумент: "))
    lagrange_result = lagrange(arg, x, y)
    gaussian_result = gaussian(arg, x, table)
    print("Значение интерполяции по Лагранжу: ", lagrange_result)
    print("Значение интерполяции по Гауссу: ", gaussian_result)
    # step = abs(x[1] - x[0])
    # count = 0
    # for i in range(len(x) - 1):
    #     #print(x[i] - x[i+1])
    #     print(abs(abs(x[i]) - abs(x[i+1])) - step)
    #     if abs(abs(x[i]) - abs(x[i+1]) - step) <= 0.001:
    #
    #         count += 1
    #
    # if count + 1 == len(x):
    #     print("Шаг в входных данных одинаков, результаты методов схожи")
    # else:
    #     print("Шаг в входных данных разный, поэтому результат метода Гаусса расходится с методом Лагранжа")
    # print(count)
    interpolation_x = np.linspace(min(x), max(x), 100)
    interpolation_lagrange, interpolation_gaussian = np.zeros(100), np.zeros(100)
    for i, xi in enumerate(interpolation_x):
        interpolation_lagrange[i] = lagrange(xi, x, y)
        interpolation_gaussian[i] = gaussian(xi, x, table)

    plt.plot(x, y, 'o', label='Заданные точки')
    plt.plot(interpolation_x, interpolation_lagrange, label='Многочлен Лагранжа')
    plt.plot(interpolation_x, interpolation_gaussian, label='Многочлен Гаусса')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
