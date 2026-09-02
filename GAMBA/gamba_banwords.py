"""
В этом файле хранятся все запретки, использующиеся
в автомодерации чата в игре

Я так же только за расширение списка запреток, как
и за расширение списков в gamba_data.py

Список запреток ниже, на стриме не смотреть
"""

#функция модерации сообщения

def moderate(message):
    rawmessage = message.lower().split()
    tomoderate = []
    for word in rawmessage:
        if not (word in whitelist):
            tomoderate.append(word)
    tomoderate = ''.join(tomoderate)

    for banword in banwords:
        if banword in tomoderate:
            return 'ban'
    else:
        return 'pass'


#список слов, которые не являются запретками, но внутри них есть запретка

whitelist = [
    'педикюр'
]

#список запреток (должны быть в нижнем регистре)

banwords = [
    'жирны',
    'жироба',
    'жирдя',
    'жиртре',
    'пидор',
    'пидар',
    'педик',
    'гомик',
    'гомосек',
    'пидр',
    'зеля',
    'зеленский',
    'путин',
    'путятин',
    'пуйло',
    'зилибоб',
    'пендо',
    'москал',
    'бандер',
    'нацик',
    'нацист',
    'фашис',
    'фашик',
    'русн',
    'даун'
]


if __name__ == '__main__':
    message = 1
    while message != '0':
        message = input('Введи сообщение для проверки автомодерации или 0 чтобы выйти - ')

        print(moderate(message), '\n')