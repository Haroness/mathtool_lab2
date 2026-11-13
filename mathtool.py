"""Точка входа консольного приложения mathtool."""

import math
import sys
from cli import build_parser
from calc import equation, stats, series, integration


def handle_solve(args):
    """Обработчик команды solve."""
    if args.a is None and args.b is None and args.c is None:
        try:
            text_a = input("Введите A: ")
            a = int(text_a)
            text_b = input("Введите B: ")
            b = int(text_b)
            text_c = input("Введите C: ")
            c = int(text_c)
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif args.a is not None and args.b is not None and args.c is not None:
        a = args.a
        b = args.b
        c = args.c
    else:
        raise ValueError("укажите все три коэффициента либо ни одного")

    coeffs = {"A": a, "B": b, "C": c}
    equation.check_coefficients(coeffs)
    kind, d, roots = equation.solve(a, b, c)

    if kind == "квадратное":
        print("Уравнение квадратное")
        print(f"Дискриминант: {d}")
        roots_count = len(roots)
        if roots_count == 2:
            x1 = roots[0]
            x2 = roots[1]
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif roots_count == 1:
            x = roots[0]
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")
    else:
        print("Уравнение линейное")
        x = roots[0]
        print(f"x = {x:.3f}")

    return 0


def handle_stats(args):
    """Обработчик команды stats."""
    if args.input is not None:
        try:
            with open(args.input, encoding="utf-8-sig") as handle:
                lines = handle.readlines()
        except OSError:
            raise OSError("файл не открывается")
    else:
        lines = sys.stdin.readlines()

    numbers = []
    for line in lines:
        words = line.split()
        for word in words:
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом")
            numbers.append(value)

    count = len(numbers)
    if count == 0:
        raise ValueError("последовательность пуста")
    if count > stats.MAX_COUNT:
        raise ValueError(f"чисел больше {stats.MAX_COUNT}")

    for value in numbers:
        if not math.isfinite(value):
            raise ValueError("значение не является конечным числом")
        if abs(value) > stats.MAX_VALUE:
            raise ValueError("значение вне допустимого диапазона")

    for label, function, form in stats.REPORT:
        value = function(numbers)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0


def handle_series(args):
    """Обработчик команды series."""
    if args.terms is not None:
        if args.terms < 1 or args.terms > series.MAX_TERMS:
            raise ValueError("количество слагаемых вне диапазона")
    elif args.eps is not None:
        if not math.isfinite(args.eps):
            raise ValueError("точность вне диапазона")
        if args.eps <= 0 or args.eps > series.MAX_EPS:
            raise ValueError("точность вне диапазона")

    term, formula = series.FORMULAS[args.func]

    if args.terms is not None:
        result = series.sum_by_terms(term, args.terms)
        count = args.terms
    else:
        result, count = series.sum_by_eps(term, args.eps)

    digits = series.DIGITS
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{digits}f}")
    return 0


def handle_integrate(args):
    """Обработчик команды integrate."""
    a = args.start
    b = args.end
    steps = args.steps

    if steps < 1 or steps > integration.MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("предел не является конечным числом")

    if a >= b:
        raise ValueError("начальный предел не меньше конечного")

    func, formula, low, high, inclusive = integration.FUNCTIONS[args.func]
    if inclusive:
        if a < low or b > high:
            raise ValueError("предел вне промежутка")
    else:
        if a <= low or b >= high:
            raise ValueError("предел вне промежутка")

    result = integration.integrate(func, a, b, steps)
    digits = integration.DIGITS
    print(formula)
    print(f"Значение интеграла: {result:.{digits}f}")
    return 0


def main(argv):
    """Основная функция программы."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)
        elif args.command == "stats":
            return handle_stats(args)
        elif args.command == "series":
            return handle_series(args)
        elif args.command == "integrate":
            return handle_integrate(args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    code = main(sys.argv[1:])
    sys.exit(code)
