import math
import sys
Max_Coef = 10000
def spravka():
    return ('Добро пожаловать в программу mathtool \nВ  данной программе вы можете получить решения для уравнений уравнения формата A * x^2 + B * x + C = 0 \nСпособы запуска:\n'
        '  python mathtool.py                          — вывод справки\n'
        '  python mathtool.py --help                   — вывод справки\n'
        '  python mathtool.py solve                    — ввод коэффициентов с клавиатуры\n'
        '  python mathtool.py solve -a 1 -b -3 -c 2    — решение с заданными коэффициентами\n'
        '\n'
        'Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.\n')


def solv():
    if len(parts) >= 3 and parts[0] == 'python' and parts[1] == 'mathtool.py' and parts[2] == 'solve':
        try:
            if len(parts) == 6:
                a = int(float(parts[3]))
                b = int(float(parts[4]))
                c = int(float(parts[5]))
            elif len(parts) == 9 and parts[3] == '-a' and parts[5] == '-b' and parts[7] == '-c':
                a = int(float(parts[4]))
                b = int(float(parts[6]))
                c = int(float(parts[8]))
            else:
                print('Ошибка ввода команды')
                sys.exit(1)
        except ValueError:
            print('Ошибка: введенный символ не является числом')
            sys.exit(1)
        if abs(a) > Max_Coef or abs(b) > Max_Coef or abs(c) > Max_Coef:
            print('Ошибка: значение вне допустимого диапазона')
            sys.exit(1)
        if a != 0:
            print('Уравнение Квадратное:', end=' ')
            D = b ** 2 - 4 * a * c
            print('D =', end=' ')
            print(D)
            if a != 0:
                if D > 0:
                    x1 = (-b + math.sqrt(D)) / (2 * a)
                    x2 = (-b - math.sqrt(D)) / (2 * a)
                    print(f"x1 = {x1:.3f}")
                    print(f"x2 = {x2:.3f}")
                    sys.exit(0)
                if D == 0:
                    x = (-b) / (2 * a)
                    print(f"x = {x:.3f}")
                    sys.exit(0)
                if D < 0:
                    print('Ошибка: Нет действительных корней')
                    sys.exit(1)

        if a == 0:
            if b != 0:
                print('Уравнение линейное:')
                x = (-c) / (b)
                print(f"x = {x:.3f}")
                sys.exit(0)
        if a == 0:
            if b == 0:
                if c != 0:
                    print('Не уравнение: неизвестного нет')
                    sys.exit(1)
        if a == 0:
            if b == 0:
                if c == 0:
                    print('Не уравнение: неизвестного нет')
                    sys.exit(1)

def solve():
    try:
        a = int(float(input('Введите A: ')))
        b = int(float(input('Введите B: ')))
        c = int(float(input('Введите C: ')))
    except ValueError:
        print('Ошибка: введенный символ не является числом')
        sys.exit(1)
    if abs(a) > Max_Coef or abs(b) > Max_Coef or abs(c) > Max_Coef:
        print('Ошибка: значение вне допустимого диапазона')
        sys.exit(1)
    if a != 0:
        print('Уравнение Квадратное:', end=' ')
        D = b**2 - 4*a*c
        print('D =', end= ' ')
        print(D)
        if a != 0:
            if D > 0:
                x1 = (-b+math.sqrt(D))/(2*a)
                x2 = (-b-math.sqrt(D))/(2*a)
                print(f"x1 = {x1:.3f}")
                print(f"x2 = {x2:.3f}")
                sys.exit(0)
            if D == 0:
                x = (-b)/(2*a)
                print(f"x = {x:.3f}")
                sys.exit(0)
            if D < 0:
                print('Ошибка: Нет действительных корней')
                sys.exit(1)

    if a == 0:
        if b != 0:
            print('Уравнение линейное:')
            x = (-c)/(b)
            print(f"x = {x:.3f}")
            sys.exit(0)
    if a == 0:
        if b == 0:
            if c != 0:
                print('Не уравнение: неизвестного нет')
                sys.exit(1)
    if a == 0:
        if b == 0:
            if c == 0:
                print('Не уравнение: неизвестного нет')
                sys.exit(1)


args = sys.argv[1:]
if len(args) == 0 or args[0] == '--help':
    print(spravka())
    sys.exit(0)

if args[0] != 'solve':
    print('Ошибка: неизвестная команда')
    sys.exit(1)

parts = ['python', 'mathtool.py'] + args
parts1 = parts

if len(args) == 1:
    solve()
elif len(args) == 4 or len(args) == 7 and args[1] == '-a' and args[3] == '-b' and args[5] == '-c':
    solv()
else:
    print('Ошибка ввода команды')
    sys.exit(1)