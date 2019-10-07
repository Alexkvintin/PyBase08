text = []
d = {}


def text_stat(t):
    for l in t:
        l += 1
        print(l)
    t = str(text)
    print("количество символов списка = ", len(t))
    for i in t:
        if i == '.' or i == ';' or i == ']' or i == '[' or i == ' ' or i == '(' or i == ')' or i == '\'' or i == ',':
            pass
        else:
            d[i] = t.count(i)
    for i in d:
     print(i, d[i])


b = input("введите дянные: ")
while True:
    text.append(b)
    b = input()
    if not b:
        break
p = ['.', ',', ':', ';', '!', '?', '(', ')', '[', ']', '&', '*']
print(text)
i = 0
for w in text:
    if w[-1] in p:
        text[i] = w[:-1]
        w = text[i]
    if w[0] in p:
        text[i] = w[1:]
        i += 1

i = 0
while i < len(text):
    print(text[i], end=' ')
    i += 1
    if i % 1 == 0:
     print()
print(text)
text_stat(text)
