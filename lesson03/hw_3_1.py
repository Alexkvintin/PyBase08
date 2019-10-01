a = int(input("введите цифру 1 для начала работы"))


def _sum(n):
    print("количество символов в вашем числе =", len(n))


while a == 1:
    b = int(input("введите целое, натуральное число: "))
    if b <= 0:
        print("Вы ввели число не соответствующее требованиям")
        continue
    elif b is int(b):
        b = str(b)
        _sum(b)
    a = int(input("хотите продолжить ? (1 - да, 0 - нет)"))
    if a == 1:
        continue
    elif a == 0:
        break

print("работа программы завершена !")
