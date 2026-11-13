"""Модуль вычисления показателей числовой последовательности."""

import math

MAX_COUNT = 20
MAX_VALUE = 10000


def count_val(values):
    """Количество чисел в последовательности."""
    n = len(values)
    return n


def sum_val(values):
    """Сумма чисел последовательности."""
    result = 0
    for value in values:
        result = result + value
    return result


def mean_val(values):
    """Среднее арифметическое чисел последовательности."""
    s = sum_val(values)
    n = len(values)
    result = s / n
    return result


def sum_squares_val(values):
    """Сумма квадратов чисел последовательности."""
    result = 0
    for value in values:
        sq = value ** 2
        result = result + sq
    return result


def rms_val(values):
    """Среднее квадратическое чисел последовательности."""
    s_sq = sum_squares_val(values)
    n = len(values)
    avg_sq = s_sq / n
    result = math.sqrt(avg_sq)
    return result


def dev_squares_sum(values):
    """Сумма квадратов отклонений от среднего арифметического."""
    mean_value = mean_val(values)
    result = 0
    for value in values:
        diff = value - mean_value
        sq_diff = diff ** 2
        result = result + sq_diff
    return result


def variance_val(values):
    """Дисперсия последовательности."""
    s_dev = dev_squares_sum(values)
    n = len(values)
    result = s_dev / n
    return result


def sko_val(values):
    """Среднеквадратическое отклонение (СКО)."""
    disp = variance_val(values)
    result = math.sqrt(disp)
    return result


def std_dev_val(values):
    """Стандартное отклонение последовательности."""
    n = len(values)
    if n < 2:
        return None
    s_dev = dev_squares_sum(values)
    avg_dev = s_dev / (n - 1)
    result = math.sqrt(avg_dev)
    return result


def min_val(values):
    """Наименьшее значение в последовательности."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def max_val(values):
    """Наибольшее значение в последовательности."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def pos_count_val(values):
    """Количество положительных чисел."""
    result = 0
    for value in values:
        if value > 0:
            result = result + 1
    return result


def neg_count_val(values):
    """Количество отрицательных чисел."""
    result = 0
    for value in values:
        if value < 0:
            result = result + 1
    return result


REPORT = [
    ("Количество", count_val, "d"),
    ("Сумма", sum_val, ".3f"),
    ("Ср. арифм.", mean_val, ".3f"),
    ("Сумма кв.", sum_squares_val, ".3f"),
    ("Ср. кв.", rms_val, ".3f"),
    ("Дисперсия", variance_val, ".3f"),
    ("СКО", sko_val, ".3f"),
    ("Станд. откл.", std_dev_val, ".3f"),
    ("Наименьшее", min_val, ".3f"),
    ("Наибольшее", max_val, ".3f"),
    ("Положительных", pos_count_val, "d"),
    ("Отрицательных", neg_count_val, "d"),
]
