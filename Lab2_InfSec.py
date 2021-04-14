import re

values = [
    ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з'],
    ['и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р'],
    ['с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'],
    ['ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В'],
    ['Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К'],
    ['Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У'],
    ['Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
    ['Э', 'Ю', 'Я', ' ', '.', ':', '!', '?', ',']
]
length = len(values) * len(values[0])
P, K, Y = [], [], []

pattern = r'[А-я,.:;?! ]+'
phrase = input('Введите фразу с клавиатуры: ')
while re.fullmatch(pattern, phrase) is None:
    phrase = input('Введенная строка некоректна, повторите ввод: ')

key = input('Введите ключ: ')
for p in phrase:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if p in values[i][j]:
                P.append(i * len(values[i]) + j + 1)
for k in key:
    for i in range(len(values)):
        for j in range(len(values[i])):
            if k in values[i][j]:
                K.append(i * len(values[i]) + j + 1)
j = 0
for i in range(len(P)):
    if j < len(K):
        Y.append((P[i] + K[j]) % length)
        j += 1
    else:
        j = 0
        Y.append((P[i] + K[j]) % length)
        j += 1
print(*Y)
###########################################
#########Обратная операция#################
###########################################
while True:
    P, K, phrase = [], [], ''
    key = input('Введите ключ: ')
    for k in key:
        for i in range(len(values)):
            for j in range(len(values[i])):
                if k in values[i][j]:
                    K.append(i * len(values[i]) + j + 1)
    j = 0
    for i in range(len(Y)):
        if j < len(K):
            if K[j] < Y[i]:
                P.append(Y[i] - K[j])
            else:
                P.append(length + Y[i] - K[j])
            j += 1
        else:
            j = 0
            if K[j] < Y[i]:
                P.append(Y[i] - K[j])
            else:
                P.append(length + Y[i] - K[j])
            j += 1
    for p in P:
        for i in range(len(values)):
            for j in range(len(values[i])):
                if i * len(values[i]) + j + 1 == p:
                    phrase += values[i][j]
    print(phrase)
