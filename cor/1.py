class Person:
    n = 0
    name = None
    surname = None
    patronymic = None
    mail = None
    phone = None
    address = None
    messenger = None


try:
    f = open('t.txt')
except:
    f = open('t.txt', 'w')

v = {}

while True:
    try:
     a = int(input("""
              Главное меню
    создать новый контакт нажмите: 1
    посмотреть список контактов нажмите: 2
    закончить работу программы нажмите: 3
    """))
    except:
        continue
    if a == 1:
        g = {}
        j = {}
        f = open('t.txt', 'a')
        Person.n += 1
        Person.name = input('Введите имя: ')
        Person.surname = input('Введите фамилию: ')
        b = input("хотите ввести еще данные (1 - да, 0 - нет)")
        if b == "1":
            Person.patronymic = input('Введите отчество: ')
            Person.mail = input('Введите основную почту: ')
            Person.phone = input('Введите основной номер телефона: ')
            Person.address = input('Введите адрес: ')
            g.a
        else:
            pass
        v = f'Person {Person.n}\n Name: {Person.name}, Surname: {Person.surname}, ' \
            f'Patronymic: {Person.patronymic}, Mail: {Person.mail}, Phone: {Person.phone} \n '
        f.write(v)
        f.close()
    elif a == 2:
        f = open('t.txt')
        for i in f:
            print(i)
        f.close()
    elif a == 3:
        c = input('Сохранить данные? (1 - да 0 - нет)')
        if c == '1':
            f.write(v)
        else:
            pass
        break
f.close()
