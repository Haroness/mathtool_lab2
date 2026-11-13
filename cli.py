"""Модуль разбора параметров командной строки."""

import argparse
from calc.series import FORMULAS
from calc.integration import FUNCTIONS


def build_parser():
    """Создает и настраивает разборщик параметров командной строки."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    # Команда solve
    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения",
        description="Решение квадратных и линейных уравнений",
        allow_abbrev=False,
    )
    solve_parser.add_argument("-a", type=int, help="коэффициент A")
    solve_parser.add_argument("-b", type=int, help="коэффициент B")
    solve_parser.add_argument("-c", type=int, help="коэффициент C")

    # Команда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="показатели последовательности",
        description="Вычисление показателей числовой последовательности",
        allow_abbrev=False,
    )
    stats_parser.add_argument("--input", type=str, help="имя файла с числами")

    # Команда series
    series_parser = subparsers.add_parser(
        "series",
        help="сумма ряда",
        description="Вычисление суммы числового ряда",
        allow_abbrev=False,
    )
    series_names = sorted(FORMULAS)
    series_parser.add_argument(
        "--func",
        choices=series_names,
        required=True,
        help="выбор ряда для вычисления",
    )
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", type=int, help="количество слагаемых")
    series_group.add_argument("--eps", type=float, help="точность вычислений")

    # Команда integrate
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное интегрирование",
        description="Численное интегрирование функции методом левых прямоугольников",
        allow_abbrev=False,
    )
    func_names = sorted(FUNCTIONS)
    integrate_parser.add_argument(
        "--func",
        choices=func_names,
        required=True,
        help="подынтегральная функция",
    )
    integrate_parser.add_argument(
        "--from",
        dest="start",
        type=float,
        required=True,
        help="нижний предел интегрирования",
    )
    integrate_parser.add_argument(
        "--to",
        dest="end",
        type=float,
        required=True,
        help="верхний предел интегрирования",
    )
    integrate_parser.add_argument(
        "--steps",
        type=int,
        required=True,
        help="количество шагов (прямоугольников)",
    )

    return parser
