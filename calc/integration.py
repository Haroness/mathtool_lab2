"""Модуль численного интегрирования методом левых прямоугольников."""

import math

MAX_STEPS = 100000
DIGITS = 4


def f_ratio(x):
    """Подынтегральная функция ratio: x / (x + 1)."""
    denom = x + 1
    result = x / denom
    return result


def f_root(x):
    """Подынтегральная функция root: sqrt(x^2 + 1)."""
    under_root = x ** 2 + 1
    result = math.sqrt(under_root)
    return result


FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def integrate(func, a, b, steps):
    """Вычисляет интеграл методом левых прямоугольников."""
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        y = func(x)
        area = y * dx
        result = result + area
    return result
