import math
a = int(input("������� ����� 1 ��� ������ ������"))


def calc(n):
    sum(c != ' ' for c in n)


while a == 1:
    b = int(input("������� �����, ����������� �����: "))
    if b == 0:
        print("�� ����� ����� �� ��������������� �����������")
        continue
    elif b is int(b):
        b = str(b)
        calc(b)
    a = int(input("������ ���������� ? (1 - ��, 0 - ���)"))
    if a == 1:
        continue
    elif a == 0:
        break

print("������ ��������� ��������� !")