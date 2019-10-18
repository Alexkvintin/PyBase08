class Person :
    n = 0
    name = None
    surname = None


def _save(x):
    h = open('b.txt', 'a')
    for i in x[:] :
        h.write(repr(x.pop()))
        h.write('\n')
    h.close()


def write(x):
    import pickle
    t = x.pop(-1)
    v = t
    print(t)
    print(v)
    f = open('t.txt', 'ab')
    pickle.dump(v, f)
    f.close()


def newfile():
    from os import rename
    f = open('newfile.txt', 'w')
    f.close()


def _open():
    import pickle
    f = open('t.txt', 'rb')
    a = pickle.load(f)
    print(a)
    f.close()

try:
    f = open('t.txt', 'ar')
except:
    f = open('t.txt', 'w')

try:
    h = open('b.txt', 'ar')
except :
    h = open('b.txt', 'w')

o = []
v = {}
j = []
while True :
    try :
        a = int(input("""
              Главное меню
    создать новый контакт нажмите: 1
    посмотреть список контактов нажмите: 2
    записать данные в файл нажмите 3
    посмотреть список контактов нажмите: 4
    закончить работу программы нажмите: 5
    """))
    except :
        continue
    if a == 1 :
        g = {}
        f = open('t.txt', 'a')
        Pn = Person
        Pn.n += 1
        Pn.name = input('Введите имя: ')
        Pn.surname = input('Введите фамилию: ')
        b = input("хотите ввести еще данные (1 - да, 0 - нет)")
        if b == "1" :
            mails = []
            phones = []
            Pn.patronymic = input('Введите отчество: ')
            Pn.mail = input('Введите основную почту: ')
            if not Pn.mail:
                pass
            else:
             mails.append(Pn.mail)
             while True :
                c = input("that's all ? (1 - yes, ENTER - continue)")
                if c == "1" :
                    break
                else :
                    Pn.mail = input('Введите дополнительную почту: ')
                    mails.append(Pn.mail)
                    continue

            Pn.phone = input('Введите основной номер телефона: ')
            if not Pn.phone:
                pass
            else:
             phones.append(Pn.phone)
             while True :
                c = input("that's all ? (1 - yes, ENTER - continue)")
                if c == "1" :
                    break
                else :
                    Pn.phone = input('Введите дополнительный номер телефона: ')
                    phones.append(Pn.phone)
                    continue
            print(phones)
            print(mails)
            Pn.address = input('Введите адрес: ')
        else :
            pass
        if b == "1" :
            g = dict(
                {'Name' : Pn.name, 'Surname' : Pn.surname, 'Patronymic' : Pn.patronymic, 'Mail' : mails,
                 'Phone' : phones, 'Address' : Pn.address})
        else :
            g = dict({'Name' : Pn.name, 'Surname' : Pn.surname})
        j.append(g)
        if b == "1" :
            l = f'Person {Pn.n}\nName: <<{Pn.name}>> Surname: <<{Pn.surname}>> ' \
                f'Patronymic: <<{Pn.patronymic}>> Mail: <<{Pn.mail}>>, Phone: <<{Pn.phone}>> \n '
        else :
            l = f'Person {Person.n}\nName: <<{Person.name}>> Surname: <<{Person.surname}>> '
        o.append(g)
        print(o)
        print(g)
        print(j)
        phones = []
        mails = []

    elif a == 2 :
        h = open('b.txt', 'r')
        for i in h :
            print(i)
        h.close()
    elif a == 3 :
        write(j)
    elif a == 4:
        _open()
        del a
    elif a == 5 :
        c = input('Сохранить данные? (1 - да 0 - нет)')
        if c == '1' :
            _save(o)
        else :
            pass
        break
f.close()
h.close()
