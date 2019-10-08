def circle(x):
    y = int(x ** 2)
    s = 3.14 * y
    print("площадь круга равна:", s)


def triangle(x, y, z):
    import math
    p = float((x + y + z) / 2)
    s = (math.sqrt(p * (p - x) * (p - y) * (p - z)))
    print("площадь треугольника равна:", s)


def rectangle(x, y):
    s = int(x * y)
    print("Площадь прямоугольника равна", s)


f = input("для начала работы програмы нажмите ENTER ")
while f is not None:
 try:
     a = int(input("""                     Площадь какой фигуры вы хотите вычеслить ?
                                   Круг (1)
                                   Треугольник (2)
                                   Квадрат (3)
                           Для выхода нажмите ENTER"""))
     if a == 1:
        b = float(input("Ввудите радиус круга:"))
        circle(b)
        k = int(input("для продолжения нажмите 1 для выхода 0: "))
        if k == 1:
            continue
        elif k == 0:
            break
     elif a == 2:
        b = float(input("Введите размер первой стороны треугольника:"))
        c = float(input("Введите размер второй стороны треугольника:"))
        d = float(input("Введите размер третей стороны треугольника:"))
        triangle(b, c, d)
        k = int(input("для продолжения нажмите 1 для выхода 0: "))
        if k == 1:
            continue
        elif k == 0:
            break
     elif a == 3:
        d = float(input("Введите длину прямоугольника:"))
        c = float(input("Введите ширину прямоугольника:"))
        rectangle(d, c)
        k = int(input("для продолжения нажмите 1 для выхода 0: "))
        if k == 1:
            continue
        elif k == 0:
            break
 except:
    break
print("работа программы завершена")
