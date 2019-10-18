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

    def __repr__(self):
        return f'Car({repr(self.name)}, {repr(self.surname)}, {repr(self.patronymic)}, {self.mail}, ' \
               f'{self.phone}, {self.address})'


class List:

    def __init__(self, catalog, numbers=0):
        self.catalog = catalog
        self.numbers = numbers

    def __str__(self):
        result = [f"Количество контактов = {self.numbers}"]
        for i, pers in enumerate(self.catalog, start=1) :
         self.numbers += 1
         result.append(f"{i}. {str(pers)}")
        return '\n'.join(result)

    def __repr__(self):
        result = [f"Количество контактов = {self.numbers}"]
        for pers in self.catalog:
            result.append(repr(pers))
        return f"{self.__class__.__name__}(" \
               f"[{','.join(result)}], " \
               f"{self.numbers}" \
               f")"

    def _adding(self, *t):
        for per in t:
            self._add(per.name, per.surname, per.patronymic, per.mail, per.phone, per.address)

    def _add(self, name, surname, patronymic, mail, phone, address):
        self.catalog.append(Person(name, surname, patronymic, mail, phone, address))

    def _search(self, name, surname, patronymic, mail, phone, address):
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
         закончить работу программы нажмите: 5
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
        pass
    elif k == 4:
        par1 = input()
        par2 = input()
        per = l._search(par1, par2)
    elif k == 5:
        break
