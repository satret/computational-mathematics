import math
import scipy
from scipy.integrate import quad

# функция для вычисления значений функции
def func(x, function):
    if function == 1:
        return math.sin(x)  # пример функции, можно изменить
    elif function == 2:
        return 3 * x ** 3 - 4 * x * x + 5 * x - 16
    else:
        return math.sqrt(x)
def f(x):
    return math.sin(x)

# метод прямоугольников
def rect_method(a, b, n, type, function):
    h = (b - a) / n
    integral = 0.0
    if type == 1:
        method = 'left'
    elif type == 2:
        method = 'right'
    else:
        method = 'middle'
    for i in range(n):
        if method == 'left':
            integral += func(a + i * h, function)
        elif method == 'right':
            integral += func(a + (i + 1) * h, function)
        elif method == 'middle':
            integral += func(a + (i + 0.5) * h, function)
    integral *= h
    return integral


# метод трапеций
def trapezoidal_method(a, b, n, function):
    h = (b - a) / n
    integral = 0.5 * (func(a, function) + func(b, function))
    for i in range(1, n):
        integral += func(a + i * h, function)
    integral *= h
    return integral


# метод Симпсона
def simpson_method(a, b, n, function):
    h = (b - a) / n
    integral = func(a, function) + func(b, function)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x, function)
        else:
            integral += 4 * func(x, function)
    integral *= h / 3
    return integral


# правило Рунге для оценки погрешности
def runge_rule(s, t, p):
    return abs((s - t) / (2 ** p - 1))


def main():
    # пользовательский ввод
    print("Выберите функцию для интегрирования:")
    print("1. sin(x)")
    print("2. 3 * x ** 3 - 4 * x * x + 5 * x - 16")
    print("3. sqrt(x)")
    function = int(input("Номер функции: "))
    print("1. Метод прямоугольников")
    print("2. Метод трапеций")
    print("3. Метод Симпсона")
    method = int(input("Введите номер метода: "))
    if method == 1:
        print("Выберите тип метода:")
        print("1. Левые прямоугольники")
        print("2. Правые прямоугольники")
        print("3. Средние прямоугольники")
        type = int(input("Введите тип метода:"))
    # можно добавить другие функции
    a = float(input("Введите левую границу интегрирования: "))
    b = float(input("Введите правую границу интегрирования: "))
    eps = float(input("Введите желаемую точность: "))

    n = 4
    # вычисление точного значения интеграла (для вычислительной реализации)
    #exact_integral = quad(func, a, b)[0]
    # вычисление интеграла различными методами с помощью цикла и правила Рунге
    integral, prev_integral = 0.0, 0.0
    i = 0
    while True:
        i += 1
        prev_integral = integral
        if method == 1:
            integral = rect_method(a, b, n, type, function)
        elif method == 2:
            integral = trapezoidal_method(a, b, n, function)
        else:
            integral = simpson_method(a, b, n, function)
        error = runge_rule(integral, prev_integral, 2)
        if error < eps:
            break
        n *= 2

    # вывод результатов
    exact_integral, error = quad(func, a, b, args=(function,))
    print("Точное значение интеграла: ", round(exact_integral, 5))
    print("Значение интеграла: ", round(integral, 5))
    print("Число разбиений интервала: ", n)
    print("Относительная погрешность: ", round(abs((integral - exact_integral) * 100 / exact_integral), 5), "%")


if __name__ == '__main__':
    main()
