"""Модуль вычисления суммы знакочередующихся числовых рядов."""

import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000

log_val = -math.log10(MAX_EPS)
DIGITS = math.ceil(log_val)


def sign(n):
    """Возвращает знак слагаемого по его номеру."""
    if n % 2 == 0:
        return -1
    else:
        return 1


def term_sqplus(n):
    """Слагаемое ряда sqplus: 1 / (n^2 + 1)."""
    s = sign(n)
    denom = n ** 2 + 1
    result = s / denom
    return result


def term_third(n):
    """Слагаемое ряда third: 1 / (3 * n)."""
    s = sign(n)
    denom = 3 * n
    result = s / denom
    return result


FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - ..."),
}


def sum_by_terms(term_func, count):
    """Вычисляет сумму ряда по заданному количеству слагаемых."""
    result = 0
    for n in range(1, count + 1):
        value = term_func(n)
        result = result + value
    return result


def sum_by_eps(term_func, eps):
    """Вычисляет сумму ряда по заданной точности eps."""
    result = 0
    n = 0
    while True:
        n = n + 1
        value = term_func(n)
        result = result + value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")
