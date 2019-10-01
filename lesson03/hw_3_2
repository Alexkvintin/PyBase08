import math


def nok(x, y):
    print("НОК чисел a и b =", x * y // math.gcd(x, y))


c = input("что-бы посчитать НОК нажмите ENTER ")
while c != None:
     try:
        print("введите целые положительные числа а и b")
        a = int(input("a: "))
        b = int(input("b: "))
        nok(a, b)
        c = int(input("хотите продолжить ? (1 - да, 0 - нет)"))
        if c == 0:
            break
        elif c == 1:
            continue
     except ValueError:
        print("Ошибка ввода !")
print("работа программы завершена")
