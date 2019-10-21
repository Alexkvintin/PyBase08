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
        result = []
        for i, pers in enumerate(self.catalog, start=1):
         result.append(f"{i}. {str(pers)}")
        return '\n'.join(result)

    def _adding(self, *t):
        for per in t:
            self._add(per.name, per.surname, per.patronymic, per.mail, per.phone, per.address)

    def _add(self, name, surname, patronymic, mail, phone, address):
        self.catalog.append(Person(name, surname, patronymic, mail, phone, address))

    def _1search(self, name):
        for i, per in enumerate(self.catalog):
            if (per.name) \
                    == (name):
                return per
        else:
            raise ValueError('Контакт не найден')

    def _2search(self, surname):
        for i, per in enumerate(self.catalog):
            if (per.surname) \
                    == (surname):
                return per
        else:
            raise ValueError('Контакт не найден')

    def _3search(self, name, surname, patronymic):
            for i, per in enumerate(self.catalog):
                if (per.name, per.surname, per.patronymic) \
                        == (name, surname, patronymic):
                    return per
            else:
                raise ValueError('Контакт не найден')

    def _4search(self, name, surname, patronymic, mail, phone, address):
                for i, per in enumerate(self.catalog):
                    if (per.name, per.surname, per.patronymic, per.mail, per.phone, per.address) \
                            == (name, surname, patronymic, mail, phone, address,):
                        return per
                else:
                    raise ValueError('Контакт не найден')


try:
    f = open('list.txt', 'r', encoding='utf-8')
    x = f.readlines()
    l = List(x)
except:
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
     mal = []
     m = input("print mail")
     mal.append(m)
     mi = input("хотите ввести доплнительную почту? (1 - да, 0 - нет) ")
     if mi == "1":
         while True:
             m = input("print mail")
             mal.append(m)
             mi = input("хотите ввести доплнительную почту? (1 - да, 0 - нет) ")
             if mi == "1":
                 continue
             else:
                 break
     mail = '; '.join(mal)
     print(mail)
     ph = []
     p = input("print phone")
     ph.append(p)
     pi = input("хотите ввести доплнительный номер телефона? (1 - да, 0 - нет) ")
     if pi == "1" :
         while True :
             p = input("print phone")
             ph.append(p)
             pi = input("хотите ввести доплнительный номер телефона? (1 - да, 0 - нет) ")
             if pi == "1" :
                 continue
             else :
                 break
     phone = '; '.join(ph)
     u = input("хотите ввести адрес ? (1 - да, 0 - нет) ")
     if u == "1":
         address = input("print address")
     else:
         address = ''
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
        f.close()
    elif k == 4:
        try:
            j = int(input("""по каким парамерам будт осуществлятся поиск ?
            (1 - имя, 2 - фамилия, 3 - имя, фамилия, отчество, 4 - по всем реквизитам """))
        except:
            continue
        if j == 1:
            par1 = input()
            per = l._1search(par1)
            print(f'Контакт найден: имя {per.name}, фамилия {per.surname}, отчество {per.patronymic}, '
                  f'почта {per.mail}, '
                  f'мобильный телефон {per.phone}, {per.address}')
        elif j == 2:
            par1 = input()
            per = l._2search(par1)
            print(f'Контакт найден: имя {per.name}, фамилия {per.surname}, отчество {per.patronymic}, '
                  f'почта {per.mail}, '
                  f'мобильный телефон {per.phone}, {per.address}')
        elif j == 3:
            par1 = input()
            par2 = input()
            par3 = input()
            per = l._3search(par1, par2, par3)
            print(f'Контакт найден: имя {per.name}, фамилия {per.surname}, отчество {per.patronymic}, '
                  f'почта {per.mail}, '
                  f'мобильный телефон {per.phone}, {per.address}')
        elif j == 4:
            par1 = input()
            par2 = input()
            par3 = input()
            par4 = input()
            par5 = input()
            par6 = input()
            per = l._4search(par1, par2, par3, par4, par5, par6)
            print(f'Контакт найден: имя {per.name}, фамилия {per.surname}, отчество {per.patronymic}, '
                  f'почта {per.mail}, '
                  f'мобильный телефон {per.phone}, адрес {per.address}')
    elif k == 5:
        print('-'*110)
        try:
            f = open('list.txt', 'r', encoding='utf-8')
        except:
            print("файл не найден!")
        for i in f.readlines():
            print(i)
        print('-'*110)
        f.close()
    elif k == 6:
        n = input("сохранить данные в файле \'list.txt\' (1 - да, 0 - нет)")
        if n == "1":
            try:
                f = open('list.txt', 'a', encoding='utf-8')
            except:
                f = open('list.txt', 'w', encoding='utf-8')
            if l == "\n":
                pass
            else:
                h = str(l)
            f.write(h)
            f.close()
            break
        else:
          break
