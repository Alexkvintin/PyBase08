text = []


def text_stat(t):
    t = str(text)
    print(t)
    print("количество символов списка = ", len(t))
    for i in t:
        if i == '.' or i == ';' or i == ']' or i == '[' or i == ' ' or i == '(' or i == ')' or i == '\'' or i == ',':
            pass
        else:
            print(i, t.count(i))


b = input("введите дянные: ")
while True:
    text.append(b)
    b = input()
    if not b:
        break
print(text)
text_stat(text)
