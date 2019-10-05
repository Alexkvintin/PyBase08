d = {}
text = []


def text_stat(t):
    print("количество символов списка = ", len(t))
    for k in t:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1


b = int(input("введите дянные"))
while True:
    text.append(b)
    try:
        b = int(input())
    except:
        break
print(text)
text_stat(text)
for i in sorted(d):
    print(i, d[i])
