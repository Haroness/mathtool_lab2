"""Модуль решения квадратных и линейных уравнений."""

import math

MAX_VALUE = 10000


def check_coefficients(coefficients):
    """Проверяет коэффициенты на допустимый диапазон и корректность."""
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")

    a = coefficients["A"]
    b = coefficients["B"]
    if a == 0 and b == 0:
        raise ValueError("это не уравнение")


def solve(a, b, c):
    """Решает линейное или квадратное уравнение."""
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d > 0:
            root_d = math.sqrt(d)
            x1 = (-b + root_d) / (2 * a)
            x2 = (-b - root_d) / (2 * a)
            return "квадратное", d, [x1, x2]
        elif d == 0:
            x = (-b) / (2 * a)
            return "квадратное", d, [x]
        else:
            return "квадратное", d, []
    else:
        x = (-c) / b
        return "линейное", None, [x]
