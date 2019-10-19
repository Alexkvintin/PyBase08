class Person:
    def __init__(self, name, surname, patronymic, mail, phone, address):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mail = mail
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'имя {self.name}, фамилия {self.surname}, отчество {self.patronymic}, почта {self.mail},' \
               f' номер телефона {self.phone}, адрес {self.address}.'


class List:

    def __init__(self, catalog):
        self.catalog = catalog


    def __str__(self):
        result = ['']
        for i, pers in enumerate(self.catalog, start=1):
         result.append(f"{i}. {str(pers)}")
        return '\n'.join(result)

    def _adding(self, *t):
        for per in t:
            self._add(per.name, per.surname, per.patronymic, per.mail, per.phone, per.address)

    def _add(self, name, surname, patronymic, mail, phone, address):
        self.catalog.append(Person(name, surname, patronymic, mail, phone, address))

    def _search(self, name, surname):
        for i, per in enumerate(self.catalog):
            if (per.name, per.surname) \
                    == (name, surname):
                return per
        else:
            raise ValueError('Контакт не найден')


l = List([])
print(l)
while True:
    try:
        k = int(input("""
                  Главное меню
          создать новый контакт нажмите: 1
        посмотреть список контактов нажмите: 2
          записать данные в файл нажмите: 3
               для поиска нажмите: 4
    посмотредь данные из файла \"list.txt\" нажмите 5
         закончить работу программы нажмите: 6
        """))
    except :
        continue
    if k == 1 :
     name = input("print name")
     surname = input("print surname")
     patronymic = input("print patronymic")
     mail = input("print mail")
     phone = input("print phone")
     address = input("print address")
     pers = (Person(name, surname, patronymic, mail, phone, address),)
     l._adding(*pers)
    elif k == 2:
       print(l)
    elif k == 3:
        try:
            f = open('list.txt', 'a', encoding='utf-8')
        except:
            f = open('list.txt', 'w', encoding='utf-8')
        if l == "\n":
            pass
        else:
            h = str(l)
        f.write(h)
    elif k == 4:
        par1 = input()
        par2 = input()
        try:
         per = l._search(par1, par2)
        except:
                m = input('Контакт не найден, хотите выполнить поиск в файле \"list.txt\"(1 - да, 0 - нет)')
                if m == '1':
                    c = open('list.txt', 'r', encoding='utf-8')
                    f = []
                    for i in c.readlines():
                        if i == '\n':
                            print('\n')
                        else:
                            print(i)
                            f.append(i)




                    for i in c.readlines():
                        if i == '\n':
                            f.append('\n')
                        else:
                            f.append(i)
                            print(f)
                    print(f)
                    f = l
                    f._search(par1, par2)
                    if ValueError:
                        print('Контакт не найден!')
                else:
                    continue
        print(f'Контакт найден: имя {per.name}, фамилия {per.surname}, отчество {per.patronymic}, '
              f'почта {per.mail}, '
              f'мобильный телефон {per.phone}, {per.address}')


    elif k == 5:
        try:
            f = open('list.txt', 'r', encoding='utf-8')
        except:
            print("файл не найден!")
        for i in f.readlines():
            print(i)
    elif k == 6:
        break
