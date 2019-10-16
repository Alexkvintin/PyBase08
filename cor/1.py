class Person:
    n = 0
    name = None
    surname = None
    def __init__(self, **kwargs):
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
        j = []
        f = open('t.txt', 'a')
        Person.n += 1
        Person.name = input('Введите имя: ')
        Person.surname = input('Введите фамилию: ')
        b = input("хотите ввести еще данные (1 - да, 0 - нет)")
        if b == "1":
            Person.patronymic = input('Введите отчество: ')
            phones = []
            mails = []
            Person.mail = input('Введите основную почту: ')
            mails.append(Person.mail)
            while True:
             c = input("that's all ? (1 - yes, ENTER - continue)")
             if c == "1":
              break
             else:
              Person.mail = input('Введите дополнительную почту: ')
              mails.append(Person.mail)
              continue
            print(mails)
            Person.phone = input('Введите основной номер телефона: ')
            phones.append(Person.phone)
            while True:
             c = input("that's all ? (1 - yes, ENTER - continue)")
             if c == "1":
              break
             else:
              Person.phone = input('Введите дополнительный номер телефона: ')
              phones.append(Person.phone)
              continue

            print(phones)
            Person.address = input('Введите адрес: ')
        else:
            pass
        if b == "1":
            g = dict(**{'Name': Person.name, 'Surname': Person.surname, 'Patronymic': Person.patronymic, 'Mail': Person.mail, 'Phone': Person.phone})
        else:
            g = dict(**{'Name': Person.name, 'Surname': Person.surname })
        j.append(g)
        print(j)
        if b == "1":
            v = f'Person {Person.n}\nName: <<{Person.name}>> Surname: <<{Person.surname}>> ' \
                f'Patronymic: <<{Person.patronymic}>> Mail: <<{Person.mail}>>, Phone: <<{Person.phone}>> \n '
        else:
            v = f'Person {Person.n}\nName: <<{Person.name}>> Surname: <<{Person.surname}>> '
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
