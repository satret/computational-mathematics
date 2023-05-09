import math
import sys
import numpy as np
import matplotlib.pyplot as plt


def f(x, option):
    if option == 1:
        return 3 * x ** 3 - 8 * x ** 2 + 4 * x + 1
    elif option == 2:
        return x ** 2 + x - 10
    elif option == 3:
        return math.sin(x)
    else:
        return -0.38 * x ** 3 - 3.42 * x ** 2 + 2.51 * x + 8.75


def f1(x, y, system_optional):
    if system_optional == 1:
        return math.sin(y + 2) - x - 15
    else:
        return x - y - 7


def f2(x, y, system_optional):
    if (system_optional == 1):
        return y + math.cos(x - 2) - 0.5
    else:
        return x * y - 18


def derivative(x, option):
    dx = 0.000001
    return (f(x + dx, option) - f(x, option)) / dx


def phi_x(x, y, system_option):
    if system_option == 1:
        # return 0.5 - 0.3 * x ** 2 - 0.6 * y ** 2 + math.sin(x)
        return math.sin(y + 2) - 15
    else:
        # return 0.4 - 0.2 * x ** 2 - 0.3 * y ** 2
        return y + 7


def phi_y(x, y, system_option):
    if system_option == 1:
        # return 0.9 - 0.2 * x ** 2 - 0.4 * x * y + math.log(x)
        return -math.cos(x - 2) + 0.5
    else:
        # return 0.8 - 0.3 * x ** 2 - 0.2 * x * y
        return 18 / x


def derivative_x1(x, y, system_option):
    dx = 0.000001
    return (phi_x(x + dx, y, system_option) - phi_x(x, y, system_option)) / dx


def derivative_x2(x, y, system_option):
    dx = 0.000001
    return (phi_y(x + dx, y, system_option) - phi_y(x, y, system_option)) / dx


def derivative_y1(x, y, system_option):
    dy = 0.000001
    return (phi_x(x, y + dy, system_option) - phi_x(x, y, system_option)) / dy


def derivative_y2(x, y, system_option):
    dy = 0.000001
    return (phi_y(x, y + dy, system_option) - phi_y(x, y, system_option)) / dy


def lambda_func(a, b, option):
    return -1.0 / (max(derivative(a, option), derivative(b, option)))


def lambda1(a, b, option):
    return -1.0 / (max(derivative(a, option), derivative(b, option)))


def phi(x, a, b, option):
    return x + f(x, option) * lambda_func(a, b, option)


def phi_derivative(x, a, b, option):
    return 1 + lambda_func(a, b, option) * derivative(x, option)


def ans(a, b, task_number, option):
    count = 0
    step = 0.1
    i = a
    while i <= b - step:
        if f(i, option) * f(i + step, option) < 0:
            count += 1
            if task_number == 1:
                print(i, i + step)
        i += step
    return count


def half_division(a, b, eps, task_number, option):
    x = 3
    count = 1
    iter = 0
    if task_number == 1:
        print("N\ta\tb\tx\tf(a)\tf(b)\tf(x)\t|a-b|")

    while abs(f((a + b) / 2, option)) > eps or abs(a - b) > eps:
        iter += 1
        if f(a, option) * f((a + b) / 2, option) < 0:
            b = (a + b) / 2
            if task_number == 1:
                print(
                    f"{count}\t{round(a, 3)}\t{round(b, 3)}\t{round((a + b) / 2, 3)}\t{round(f(a, option), 3)}\t{round(f(b, option), 3)}\t{round(f(x, option), 3)}\t{round(abs(a - b), 3)}\t")
                count += 1
        else:
            a = (a + b) / 2
            if task_number == 1:
                print(
                    f"{count}\t{int(a * 1000) / 1000.0}\t{int(b * 1000) / 1000.0}\t{int(((a + b) / 2) * 1000) / 1000.0}\t{int((f(a, option)) * 1000) / 1000.0}\t{int(f(b, option) * 1000) / 1000.0}\t{int(f(x, option) * 1000) / 1000.0}\t{int(abs(a - b) * 1000) / 1000.0}\t")
                count += 1

    return round((a + b) / 2, 3), iter


def chord(a, b, eps, option):
    x = a
    x_old = b
    iter = 0
    while (abs(f(x, option)) > eps or abs(x - x_old) > eps) and iter < 1000:
        x_old = x
        x = (a * f(b, option) - b * f(a, option)) / (f(b, option) - f(a, option))
        iter += 1
        if f(x, option) * f(a, option) < 0:
            b = x
        else:
            a = x
    return round(x, 3), iter


def newton(a, eps, option):
    x = a
    x_old = 0
    iter = 0
    while (abs(f(x, option)) > eps or abs(x - x_old) > eps) and iter < 1000:
        x_old = x
        x = x - f(x, option) / derivative(x, option)
        iter += 1
    return round(x, 3), iter


def secant(a, b, eps, task_number, option):
    x0 = a
    x1 = a + eps
    x2 = x1 - ((x1 - x0) / (f(x1, option) - f(x0, option))) * f(x1, option)
    count = 1
    iter = 0
    if task_number == 1:
        print("N", "x_k-1", "x_k", "x_k+1", "f(x_k+1)", "|x_k+1 - x_k|", "\t")
    while abs(f(x2, option)) > eps and iter < 1000:
        x2 = x1 - ((x1 - x0) / (f(x1, option) - f(x0, option))) * f(x1, option)
        x0 = x1
        x1 = x2
        iter += 1
        if task_number == 1:
            print(count, round(x0, 3), round(x1, 3), round(x2, 3), round(f(x2, option), 3), round(abs(x2 - x1), 3),
                  "\t")
            count += 1
    return round(x2, 3), iter


def simpleIteration(a, b, eps, task_number, option):
    x = a
    xn = phi(x, a, b, option)
    count = 1
    iter = 0
    print("", phi_derivative(a, a, b, option), phi_derivative(b, a, b, option), "lambda: ", lambda_func(a, b, option))
    if task_number == 1:
        print("N", "x_k", "x_k+1", "f(x_k+1)", "|x_k+1 - x_k|", "\t")
    if abs(phi_derivative(a, a, b, option)) >= 1 or abs(phi_derivative(b, a, b, option)) >= 1:
        print("the method does not add up")
    else:
        while (abs(f(x, option)) > eps or abs(xn - x) > eps) and iter < 1000:
            iter += 1
            x = xn
            xn = phi(x, a, b, option)
            print(xn)
            if task_number == 1:
                print(count, round(x, 3), round(xn, 3), round(f(xn, option), 3), round(abs(xn - x), 3), "\t")
                count += 1
        return round(xn, 3), iter


def simpleIterationForSystem(a, b, eps, system_option):
    max_xx = 0
    max_xy = 0
    max_yx = 0
    max_yy = 0
    iter = 0

    for i in range(1, 100):
        for j in range(1, 100):
            i_val = 0.01 * i
            j_val = 0.01 * j

            if derivative_x1(i_val, j_val, system_option) > max_xx:
                max_xx = derivative_x1(i_val, j_val, system_option)
            if derivative_x2(i_val, j_val, system_option) > max_yx:
                max_yx = derivative_x2(i_val, j_val, system_option)
            if derivative_y1(i_val, j_val, system_option) > max_xy:
                max_xy = derivative_y1(i_val, j_val, system_option)
            if derivative_y2(i_val, j_val, system_option) > max_yy:
                max_yy = derivative_y2(i_val, j_val, system_option)

    if abs(max_xx) < 1 or abs(max_xy) < 1 or abs(max_yx) < 1 or abs(max_yy) < 1:
        x0 = a
        y0 = b
        print(x0, y0)
        x1 = phi_x(x0, y0, system_option)
        y1 = phi_y(x0, y0, system_option)

        #while (abs(x1 - x0) >= eps and abs(y1 - y0) >= eps):
        while abs(f1(x1, y1, system_option)) >= eps and abs(f2(x1, y1, system_option)) >= eps:
            x0 = x1
            y0 = y1
            x1 = phi_x(x0, y0, system_option)
            y1 = phi_y(x0, y0, system_option)
            iter += 1
            print(x1, y1, "Подствленные значения", f1(x1, y1, system_option), f2(x1, y1, system_option))
    else:
        print("Решение не сходится")
    print(f1(x1, y1, system_option), f2(x1, y1, system_option))
    return round(x1, 3), round(y1, 3), iter


def main():
    step = 0.2
    eps = None
    left = -100.0
    right = 100.0
    sol = 0
    task_number = 1
    option = None
    system_option = None
    first = 4
    method_number = None

    print("FIRST TASK")
    print("calculations:")
    # i = -100
    # while i <= 100:
    #     i += 0.2
    #     if f(i, first) * f(i + step, first) < 0:
    #         if sol == 0:
    #             print("left solution:", half_division(i, i + step, 0.01, task_number, first))
    #             sol += 1
    #         elif sol == 1:
    #             print("middle solution:", secant(i, i + step, 0.01, task_number, first))
    #             sol += 1
    #         else:
    #             print("right solution:", simpleIteration(i, i + step, 0.01, task_number, first))
    #             print()
    #             break
    # print("1) 3x*x*x-8*x*x+4*x+4")
    # print("2) x*x + x - 10")
    # print("3) sin(x)")
    # #option = int(input("enter the function:"))
    # if option > 3 or option < 1:
    #     print("vvedite correct znach")
    #     sys.exit()
    # print("decision isolation intervals:")
    # print(ans(left, right, task_number, option))
    # print("1) half division")
    # print("2) secant")
    # print("3) simple iteration")
    # method_number = int(input("enter the method:"))
    # print("enter intervals and accuracy:")
    # a, b, eps = map(float, input().split())
    # task_number = 2
    # print("SECOND TASK")
    # if ans(a, b, task_number, option) == 0:
    #     print("There are no solutions on the entered segment")
    # elif ans(a, b, task_number, option) > 1:
    #     print("there is more than one solution on the introduced segment")
    # else:
    #     if method_number == 1:
    #         print("half division:")
    #         x, iter = half_division(a, b, eps, task_number, option)
    #         print("решение:", x, "значение функции в корне", f(x, option), " число итераций:", iter)
    #     elif method_number == 2:
    #         print("secant:")
    #         x, iter = secant(a, b, eps, task_number, option)
    #         print("решение:", x, "значение функции в корне", f(x, option), " число итераций:", iter)
    #     else:
    #         print("simple iteration:")
    #         x, iter = simpleIteration(a, b, eps, task_number, option)
    #         print("решение:", x, "значение функции в корне", f(x, option), " число итераций:", iter)
    #     x = np.linspace(-2, 5, 100)
    #     plt.plot(x, f(x, option))
    #     plt.grid()
    #     # plt.axhline(y=0, color='k')
    #     plt.show()
    # print("SECOND TASK")
    # print("1) 0.5 - 0.3 * x * x - 0.6 * y * y + sin(x)")
    # print("0.9 - 0.2 * x * x - 0.4 * x * y + log(x)")
    # print("2) 0.4 - 0.2 * x * x - 0.3 * y * y")
    # print("0.8 - 0.3 * x * x - 0.2 * x * y")
    print("1) sin(y + 2) - x - 15")
    print("y + cos(x - 2) - 0.5")
    print("2) x - y - 7")
    print("x * y - 18")
    system_option = int(input("enter the functions number:"))
    # print("simpleIterationForSystem:", simpleIterationForSystem(1, 1, 0.01, system_option))
    x, y, iter = simpleIterationForSystem(10, 0, 0.01, system_option)

    print("Решения:", x, y, "Итерации: ", iter)
    x = np.linspace(-50, 50, 100)
    if (system_option == 1):
        x = np.linspace(-10, 10, 1000)
        plt.plot(x, np.sin(x) + x - 15)
        plt.plot(x, -np.cos(x) + 0.5)
        plt.grid()
        # plt.axhline(y=0, color='k')
        plt.show()
    else:
        plt.plot(x, x - 7)
        plt.plot(x, 18 / x)
        plt.grid()
        # plt.axhline(y=0, color='k')
        plt.show()


if __name__ == '__main__':
    main()
