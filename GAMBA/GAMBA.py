"""
Это - файл с основным кодом игры
не рекомендую его изменять, чтобы
случайно не поломать что-то
"""

# пажилые дольки - ₫
# энергия - ∈
# рубли - ₽
# символы картинок - █▓▒░


from gamba_ui import *
from gamba_data import *
from gamba_banwords import *
import random
import time
import colorama
import platform
import subprocess
import copy

colorama.init()

class points:
    def __init__(self, value : int, symbol : str):
        self.value = value
        self.symbol = symbol

    def cantake(self, value : int):
        if self.value >= value:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.value} {self.symbol}'

    def __repr__(self):
        return f'{self} : value = {self.value}, symbol = {self.symbol}'


class progress:
    def __init__(self, value : int):
        self.value = value / 100

    def __str__(self):
        value = int(self.value * 10)

        if value >= 3:
            out = '█' * (value - 3) + '▓▒░'
        else:
            out = '▓▒░'[-value:]
        return out

    def __repr__(self):
        return f'{self} : value = {self.value}'


def clear_screen():
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.call(command, shell=True)


def banned():
    clear_screen()
    global slices
    global reset
    print('Тебя забанили. Ты проиграл.')
    print('Кто-то забыл про правила твича, да?\n')

    print(f'За игру ты успел накопить {slices}\n')

    reset = input('Введи "1", если хочешь попробовать снова - ')


def nomoney():
    global money
    global slices
    global reset

    if money.value <= 0:
        clear_screen()
        print('У тебя закончились деньги. Тебе больше не на что покупать еду.')
        print('Придётся искать дополнительные пути заработка. Ты проиграл.\n')

        print(f'За игру ты успел накопить {slices}\n')

        reset = input('Введи "1", если хочешь попробовать снова - ')


def fulltutor():
    global slices
    global money
    global energy

    clear_screen()
    print(screen(slices, money, energy,
                 'П О Л Н О Е   О Б У Ч Е Н И Е',
                 '',
                 'Снизу справа у тебя есть несколько значений:',
                 f'Пажилые дольки ( ₫ ), сейчас их у тебя - {slices}',
                 'Ты будешь копить их на стримах и во время гамб',
                 '',
                 f'Рубли ( ₽ ), сейчас их у тебя - {money}',
                 'Ты будешь зарабатывать их на работе в пвз ОзонДберриз Маркета,',
                 'на них ты каждый день покупаешь себе еду (500 ₽),',
                 'а также в какой-то день тебе позвонят насчёт аренды квартиры... (27 000 ₽)',
                 '',
                 f'Энергия ( ∈ ), сейчас её у тебя - {energy}',
                 'Не давай ей спуститься до нуля, тебя сразу вырубит, а на работе за это дают штрафы',
                 '',
                 'В целом это всё, что ты должен знать, жми Enter, чтобы продолжить'))

def basetutor():
    global slices
    global money
    global energy

    clear_screen()
    print(screen(slices, money, energy,
                 'Б А З О В Ы Й   М И Н И М У М   О Б У Ч Е Н И Я',
                 '',
                 'Обозначения снизу справа:',
                 '',
                 'Пажилые дольки -- ₫',
                 '',
                 'Рубли -- ₽',
                 '',
                 'Энергия -- ∈',
                 '',
                 'Этого хватит, жми Enter, чтобы продолжить'))


def win():
    global slices
    global money
    global energy

    if slices.value >= 5000000:
        clear_screen()
        print(winscreen(slices, money, energy))

        print('Ты победил! У тебя получилось накопить на випку за месяц!')

        if rentpayed:
            print('Да ещё и аренду заплатил! Чистая победа!')

        else:
            print('Только вот за аренду в этом месяце ты не заплатил... Надеюсь, не выселят...')
            print('Грязная победа...')

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)

        nextt = input('\033[2mНажми Enter, чтобы продолжить...\033[0m ')

        clear_screen()

        print(screen(slices, money, energy,
                     '                                           К О Н Е Ц',
                     '',
                     'У тебя получилось пройти эту игру, поздравляю!',
                     '',
                     'На самом деле я сам не успевал пройти игру, поэтому не знаю насколько это тяжело',
                     '',
                     'Наверное, к концу игры рутина уже невыносима, но, как я вижу, ты справился!',
                     'И это самое классное',
                     '',
                     '',
                     'На этом всё',
                     'Возможно, в будущем здесь появится больше игр... Я надеюсь',
                     '',
                     '',
                     '...Пока!'))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)

        nextt = input('\033[2mНажми Enter, чтобы выйти...\033[0m ')

        exit()


def chathi():
    global mods
    global modhi
    global vips
    global viphi
    global nns
    global nnhi
    global name
    global reset
    localmods = copy.deepcopy(mods)
    localvips = copy.deepcopy(vips)
    localnns = copy.deepcopy(nns)
    chatseq = []

    for messages in range(random.randint(7, 12)):
        mvn = random.choices((0, 1, 2), (2, 8, 90), k=1)[0]
        bro = random.choice((localmods, localvips, localnns)[mvn])

        (localmods, localvips, localnns)[mvn].pop((localmods, localvips, localnns)[mvn].index(bro))

        line = random.choice((modhi, viphi, nnhi)[mvn])
        ban = '\033[2m' if '-- permanently banned' in line else ''

        cur = f'{ban}{bro}: {line}\033[0m'
        chatseq.append(cur)

    print('\033[2mWelcome to the chat room!\033[0m')

    for line in chatseq:
        wait = random.randint(2, 4) * 0.1
        time.sleep(wait)
        print(line)

    print('')

    message = input('Напиши что-нибудь в чат: ')

    moderation = moderate(message)

    print('\033[2F\033[0J', end='', flush=True)
    print(f'{'\033[2m' if moderation == 'ban' else ''}{name}: {message}{' -- permanently banned' if moderation == 'ban' else ''}\033[0m')

    time.sleep(2)

    if moderation == 'ban':
        banned()
        if reset != '1':
            exit()


def gamba(viewers, isgamba, theme):
    global slices
    global energy

    if isgamba:
        global gamba_stream
        curstream = gamba_stream
    else:
        global stream
        curstream = stream

    gamba = random.choice(curstream[theme])

    print(gamba[0])
    print(gamba[1])
    print('')

    votesa = progress(random.randint(10, 90))
    votesb = progress(100 - (votesa.value * 100))

    voters = random.randint(3000, viewers)

    fonda = round(votesa.value * voters * 1000)
    fondb = round(votesb.value * voters * 1000)
    fond = fonda + fondb

    avote = 0
    if isgamba:     #если рекламный стрим - Антон тоже голосует

        avote = random.randint(1, 2)

        if avote == 1:
            votesa.value = votesa.value * 0.7

        else:
            votesb.value = votesb.value * 0.7

    print(f'[1] : {gamba[2]} - поставили {fonda} долек {votesa} {'+ Антон поставил на это' if avote == 1 else ''}\t\033[2m(-5 ∈)\033[0m')
    print(f'[2] : {gamba[3]} - поставили {fondb} долек {votesb} {'+ Антон поставил на это' if avote == 2 else ''}\t\033[2m(-5 ∈)\033[0m')
    print('[0] : не делать ставку \033[2m(-0 ∈)\033[0m')

    vote = input('\nЗа что проголосуешь? Введи цифру - ')
    while not (vote in ('1', '2', '0')):
        print('\033[1F\033[0K', end='', flush=True)
        vote = input('Введи одну из предложенных цифр - ')
    vote = int(vote) - 1

    if vote != -1:
        bet = input(f'Сколько долек поставишь? - ')
        while not bet.isdigit() or int(bet) > slices.value or int(bet) <= 0:
            print('\033[1F\033[0K', end='', flush=True)
            bet = input(f'Неподходящее значение. Сколько долек поставишь? - ')
        bet = int(bet)

        slices.value -= bet
        energy.value -= 5

    clear_screen()
    print(streamscreen(viewers, slices, money, energy))
    print('')

    for i in range(1, 4):
        print(f'Ждём конца гамбы {'.' * i}')
        time.sleep(1)
        print('\033[1F\033[0K', end='', flush=True)

    win = random.choices((gamba[2], gamba[3]), (votesa.value, votesb.value), k=1)[0]

    if vote != -1:
        reward = round((bet / (fonda, fondb)[vote]) * fond)

        if (gamba[2], gamba[3])[vote] == win:
            print(f'Сыграла ставка - {win}')
            print('\nТы победил!')
            print(f'Ты получаешь +{reward}\n')
            slices.value += reward

        else:
            print(f'Сыграла ставка - {win}')
            print('\nТы проиграл...\n')

    else:
        print(f'Сыграла ставка - {win}\n')

    nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m ')

def onstream():
    global energy
    global slices
    global money
    global streak

    viewers = random.randint(8196, 15374)

    clear_screen()

    print(streamstart(viewers, slices, money, energy))

    print('\nНачался стрим!\n')

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(0.5)
        print('\033[1F\033[0K', end='', flush=True)

    nextt = input('\033[2mНажми Enter, чтобы продолжить...\033[0m ')

    clear_screen()

    print(streamscreen(viewers, slices, money, energy))

    if streak == 0:
        print('У тебя нулевая серия просмотров,\nне пропускай стримы, чтобы получать баллы!\n')
        print(f'Твой стрик - {streak} \033[2m+1\033[0m')
        print('\033[2m(+100 баллов)\033[0m')
        streak += 1
        slices.value += 50
    elif streak < 3:
        print(f'Не пропускай стримы, чтобы получать баллы!\nДо следующей награды \033[2m(350)\033[0m {3 - streak} {('стрим', 'стрима')[2 - streak]}\n')
        print(f'Твой стрик - {streak} \033[2m+1\033[0m')
        print('\033[2m(+150 баллов)\033[0m')
        streak += 1
        slices.value += 150
    elif streak < 7:
        print(f'Не пропускай стримы, чтобы получать баллы!\nДо следующей награды \033[2m(450)\033[0m {7 - streak} {('стрим', 'стрима', 'стрима', 'стрима')[6 - streak]}\n')
        print(f'Твой стрик - {streak} \033[2m+1\033[0m')
        print('\033[2m(+350 баллов)\033[0m')
        streak += 1
        slices.value += 350
    elif streak >= 7:
        print(f'У тебя максимальная награда за стрик! Не пропускай стримы, чтобы сохранить её!\n')
        print(f'Твой стрик - {streak} \033[2m+1\033[0m')
        print('\033[2m(+450 баллов)\033[0m')
        streak += 1
        slices.value += 450

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(0.5)
        print('\033[1F\033[0K', end='', flush=True)

    nextt = input('\033[2mНажми Enter, чтобы продолжить...\033[0m ')

    win()

    clear_screen()

    chathi()

    clear_screen()

    if reset == '1':
        return None

    print(streamscreen(viewers, slices, money, energy))

    print('')

    if random.randint(1, 10) <= 3:
        isgamba = 1
        print('Сегодня рекламный стрим, будет много гамб!')
        todaygambas = random.randint(4, 7)
    else:
        isgamba = 0
        print('Сегодня обычный стрим.')
        todaygambas = random.randint(1, 3)

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(1.5)
        print('\033[1F\033[0K', end='', flush=True)

    for i in range(todaygambas):
        skipstream = input('Введи "0", если хочешь пропустить оставшуюся часть стрима \033[2m(-5 ∈, если продолжишь)\033[0m - ')
        if skipstream == '0':
            break

        if energy.cantake(5):
            energy.value -= 5
        else:
            energy.value -= energy.value

        if energy.value == 0:
            clear_screen()
            print('Ты слишком устал, тебя вырубает...')

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1)
                print('\033[1F\033[0K', end='', flush=True)

            break

        clear_screen()

        print(gambascreen(viewers, slices, money, energy))
        time.sleep(3)

        clear_screen()

        if isgamba:
            theme = random.choice(list(gamba_stream.keys()))

            if '{game}' in theme:
                theme = theme.replace('{game}', random.choice(paid_game))
        else:
            theme = random.choice(list(stream.keys()))

        print(streamscreen(viewers, slices, money, energy))
        print(theme)
        print('')

        gamba(viewers, isgamba, theme)

        win()

        clear_screen()

        print(streamscreen(viewers, slices, money, energy))
        print('\n\033[2mТы получаешь +100 баллов за просмотр\033[0m\n')
        slices.value += 100
        time.sleep(2)

        win()

    else:
        if energy.value != 0:
            clear_screen()
            print(streamscreen(viewers, slices, money, energy))
            print('\nСтрим закончен!')
            time.sleep(3)


def workaction(code, fname, lname, order):
    global energy
    global money
    global orders
    global ords
    global mistakes

    if code != '0':    #код есть
        right = '1'
        print(f' * {random.choice(clicode)}')

        time.sleep(0.5)
        print(f'  {random.choice(barcodes)}')

    else:       #кода нет
        right = '0'
        print(f' * {random.choice(clinocode)}')

    time.sleep(1.5)

    print('\n\033[2m[0] - Я не выдам вам заказ\033[0m')
    print('\033[2m[1] - Сканировать код и пойти на склад за заказом \033[0m\n')

    action = input('Выбери действие \033[2m(его номер)\033[0m - ')

    while not action in ('0', '1'):
        action = input('Неподходящее значение. Выбери действие \033[2m(его номер)\033[0m - ')

    print('\033[4F\033[0J', end='', flush=True)

    if action == right:     #действие правильное
        if action == '0':       #не выдал заказ
            print(' - Я не выдам вам заказ')
            time.sleep(1.5)

            print(f' * {random.choice(clicomplain)}')

            time.sleep(1)

            print(' - ...')

        else:                   #выдал заказ
            clear_screen()
            print(workorderscreen(money, energy, orders, fname, lname, order, code))

            time.sleep(1.5)
            print('\033[2mЗапомни код и иди за заказом\033[0m\n')

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1)
                print('\033[1F\033[0K', end='', flush=True)

            nextt = input('\033[2mНажми Enter, чтобы продолжить...\033[0m ')

            print('\033[3F\033[0J\033[2mУходим на склад... (-2 ∈)\033[0m')

            if energy.cantake(2):
                energy.value -= 2
            else:
                energy.value -= energy.value

            time.sleep(2)

            clear_screen()
            print(warehouse(ords[0], ords[1], ords[2], ords[3], ords[4], ords[5]))
            print('')

            time.sleep(1.5)
            choice = input('Выбери ячейку, из которой заберёшь посылку \033[2m(цифра 1-6)\033[0m - ')

            print('\033[1F\033[0K', end='', flush=True)

            while True:
                if choice.isdigit():
                    if choice in ('1', '2', '3', '4', '5', '6'):
                        if not (ords[(int(choice) - 1)] == '0'):
                            break
                print('Неподходящее значение')

                time.sleep(1.5)
                print('\033[1F\033[0K', end='', flush=True)
                choice = input('Выбери ячейку, из которой заберёшь посылку \033[2m(цифра 1-6)\033[0m - ')

            choicecode = ords[(int(choice) - 1)]

            print('\033[1F\033[0K', end='', flush=True)
            print('\033[2mВозвращаемся...\033[0m')
            time.sleep(2)

            while choicecode != code:   #проверка - правильную ли посылку забрал игрок
                clear_screen()
                print(workorderscreen(money, energy, orders, fname, lname, order, code))
                print('')
                print(f'Ты забрал посылку с номером {choicecode}')

                print('')
                print('Эта не та посылка! Запомни код и иди, забирай нужную!')

                for i in range(1, 4):
                    print('. ' * i)
                    time.sleep(1)
                    print('\033[1F\033[0K', end='', flush=True)

                nextt = input('\033[2mНажми Enter, чтобы продолжить...\033[0m ')

                print('\033[1F\033[0K', end='', flush=True)
                print('\033[3F\033[0J\033[2mУходим на склад... (-2 ∈)\033[0m')

                if energy.cantake(2):
                    energy.value -= 2
                else:
                    energy.value -= energy.value

                time.sleep(2)

                clear_screen()
                print(warehouse(ords[0], ords[1], ords[2], ords[3], ords[4], ords[5]))
                print('')

                time.sleep(1.5)
                choice = input('Выбери ячейку, из которой заберёшь посылку \033[2m(цифра 1-6)\033[0m - ')

                print('\033[1F\033[0K', end='', flush=True)
                while True:
                    if choice.isdigit():
                        if choice in ('1', '2', '3', '4', '5', '6'):
                            if not (ords[(int(choice) - 1)] == '0'):
                                break
                    print('Неподходящее значение')

                    time.sleep(1.5)
                    print('\033[1F\033[0K', end='', flush=True)
                    choice = input('Выбери ячейку, из которой заберёшь посылку \033[2m(цифра 1-6)\033[0m - ')

                choicecode = ords[(int(choice) - 1)]

                print('\033[1F\033[0K', end='', flush=True)
                print('\033[2mВозвращаемся...\033[0m')
                time.sleep(2)

            else:   #игрок забрал нужную посылку
                clear_screen()
                print(workorderscreen(money, energy, orders, fname, lname, order, code))
                print('')
                print(f'Ты забрал посылку с номером {choicecode}')
                print('')
                nextt = input('\033[2mНажми Enter, чтобы отдать посылку\033[0m')
                print('\033[1F\033[0K', end='', flush=True)

                ords[int(choice) - 1] = '0'
                orders -= 1

                clear_screen()
                print(workorderscreen(money, energy, orders, fname, lname, order, code))
                print('')
                print('Ждём пока товар проверят')
                print('')
                for i in range(1, 4):
                    print('. ' * i)
                    time.sleep(1.5)
                    print('\033[1F\033[0K', end='', flush=True)

                good = random.choices((0, 1), (0.1, 0.9))[0]

                print('\033[2F\033[0K', end='', flush=True)

                if good:    #посылку забирают
                    print(f' * {random.choice(clipick)}')
                    print('')

                    time.sleep(1.5)
                    print('[0] - \033[2mОформить возврат\033[0m')
                    print('[1] - \033[2mСписать деньги\033[0m\n')

                    action = input('Выбери действие \033[2m(его номер)\033[0m - ')

                    while not action in ('0', '1'):
                        print('\033[1F\033[0K', end='', flush=True)
                        action = input('Неподходящее значение. Выбери действие \033[2m(его номер)\033[0m - ')

                    clear_screen()
                    print(workorderscreen(money, energy, orders, fname, lname, order, code))
                    print('')

                    time.sleep(1.5)
                    if action == '1':   #списываем деньги
                        print('\033[2mДеньги списаны\033[0m')
                        print('')

                        time.sleep(2)
                        print('\033[2mПосылку забрали\033[0m')
                        print('')

                    else:               #оформляем возврат - ошибка
                        print('\033[2mОформлен возврат\033[0m')
                        print('')

                        time.sleep(2)
                        print('\033[2mПосылку забрали\033[0m')
                        print('')

                        time.sleep(1.5)
                        mistakes += 1
                        print(f'\033[2m+1 штраф (всего {mistakes})\033[0m')

                else:   #посылку возвращают
                    print(f' * {(random.choice(clinopick))}')
                    print('')

                    time.sleep(1.5)
                    print('[0] - \033[2mОформить возврат\033[0m')
                    print('[1] - \033[2mСписать деньги\033[0m\n')

                    action = input('Выбери действие \033[2m(его номер)\033[0m - ')

                    while not action in ('0', '1'):
                        print('\033[1F\033[0K', end='', flush=True)
                        action = input('Неподходящее значение. Выбери действие \033[2m(его номер)\033[0m - ')

                    clear_screen()
                    print(workorderscreen(money, energy, orders, fname, lname, order, code))
                    print('')

                    if action == '1':   #списываем деньги - ошибка
                        print('\033[2mДеньги списаны\033[0m')
                        print('')

                        time.sleep(2)
                        print('\033[2mПосылку оставили\033[0m')
                        print('')

                        time.sleep(1.5)
                        mistakes += 1
                        print(f'\033[2m+1 штраф (всего {mistakes})\033[0m')

                    else:               #оформляем возврат
                        print('\033[2mОформлен возврат\033[0m')
                        print('')

                        time.sleep(2)
                        print('\033[2mПосылку оставили\033[0m')
                        print('')

    else:   #действие неправильное
        if action == '0':   #не выдал заказ - ошибка
            print(' - Я не выдам вам заказ')
            time.sleep(1.5)

            print('')
            print(f' * {random.choice(clicomplain)}')

            time.sleep(1)
            print('')
            print(' - ...')

            time.sleep(1.5)
            print('')
            mistakes += 1
            print(f'\033[2m+1 штраф (всего {mistakes})\033[0m')

        else:               #сканировал код - ошибка
            clear_screen()
            print(workorderscreen(money, energy, orders, '---', '---', '---', '---'))
            print('')

            time.sleep(2)
            print(' - Я не могу выдать заказ без кода...')
            print('')

            time.sleep(1.5)
            print(f' * {random.choice(clicomplain)}')
            print('')

            time.sleep(1)
            print(' - ...')
            print('')

            time.sleep(1.5)
            mistakes += 1
            print(f'\033[2m+1 штраф (всего {mistakes})\033[0m')

    time.sleep(2)
    clear_screen()
    print(' - До свидания!')
    print('')

    time.sleep(1.5)
    print(f' * {random.choice(clibye)}')

    time.sleep(2.5)


def work():
    global energy
    global money
    global orders
    global ords
    global mistakes
    mistakes = 0

    print('Пора на работу...')

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(1)
        print('\033[1F\033[0K', end='', flush=True)

    clear_screen()

    clients = random.randint(3, 5)

    orders = clients + random.randint(1, 3)

    print(workscreen(money, energy, orders))

    ords = []

    for order in range(min(orders, 6)):
        order = random.randint(100000, 999999)
        while order in ords:
            order = random.randint(100000, 999999)
        ords.append(str(order))

    while len(ords) < 6:
        ords.append('0')

    random.shuffle(ords)

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(1.5)
        print('\033[1F\033[0K', end='', flush=True)

    for _ in range(clients):

        fname = random.choice(first_name)
        lname = random.choice(last_name)
        order = random.choice(orderlist)

        if (first_name.index(fname) % 2) != 0:
            lname += 'а'

        clear_screen()

        print('\033[2mКто-то пришёл...\033[0m\n')

        time.sleep(1)

        print(' - Здравствуйте!\n')

        time.sleep(random.randint(10, 25) * 0.1)

        print(f' * {random.choice(clihi)}')

        time.sleep(1.5)

        print(' *  Я хочу забрать заказ...\n')

        time.sleep(1)

        print(' - Показывайте штрих-код\n')

        answer = random.choices(('_', random.choice(ords)), (10, 90))[0]

        if answer != '_':
            if answer == '0':
                rl = random.randint(0, 1)
                if rl:
                    for code in reversed(ords):
                        if code != '0':
                            answer = code
                            break
                else:
                    for code in ords:
                        if code != '0':
                            answer = code
                            break
        else:
            answer = '0'

        time.sleep(2)
        workaction(answer, fname, lname, order)

        clear_screen()

        if energy.cantake(2):
            energy.value -= 2
        else:
            energy.value -= energy.value

        print('\033[2m-2 ∈\033[0m')

        if energy.value == 0:
            time.sleep(1.5)

            clear_screen()
            print('\033[2mГлаза закрываются...\033[0m')

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1)
                print('\033[1F\033[0K', end='', flush=True)

            mistakes += 1
            energy.value += 15
            print(f'\033[2mТы уснул на работе! +1 штраф (всего {mistakes}), +15 ∈\033[0m')
            print('')

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1.5)
                print('\033[1F\033[0K', end='', flush=True)

        clear_screen()
        print(workscreen(money, energy, orders))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1)
            print('\033[1F\033[0K', end='', flush=True)

    print('Рабочий день закончился!')
    print(f'За сегодня {mistakes} штрафов == -{mistakes * 100} ₽')
    print('Зарплата за смену == 2500 ₽')
    print(f'Итого == {2500 - (mistakes * 100)} ₽')
    money.value += (2500 - (mistakes * 100))

    for i in range(1, 4):
        print('. ' * i)
        time.sleep(1.5)
        print('\033[1F\033[0K', end='', flush=True)


def rungame():
    global slices   #прописаны все глобальные значения, чтобы их можно было изменять внутри функции
    global money
    global energy
    global streak
    global orders
    global ords
    global mistakes
    global reset
    global name
    global rentpayed

    clear_screen()
    print(gabarytes)
    nextt = input()
    clear_screen()

    print(jointwitch())
    print('')
    print('Введи свой ник')
    name = input('\033[15;10f')

    clear_screen()

    createdtime = time.ctime().split()
    t1 = createdtime[-2][:-3]
    created = f'{createdtime[-1]} {createdtime[-4]} {createdtime[-3]}'

    while True:         #цикл игры
        slices = points(random.randint(30, 60) * 100, '₫')  #все глобальные значения задаются
        money = points(random.randint(4, 9) * 100, '₽')     #снова, чтобы при перезапуске игры
        energy = points(random.randint(4, 7) * 10, '∈')     #всё сбрасывалось
        streak = random.randint(2, 6)
        orders = 0
        ords = []
        mistakes = 0

        reset = 0
        misses = 0
        streamchance = 1.0
        streamstreak = 0
        rent = 27000
        rentchance = 0.5
        rentpayed = 0

        viewers = random.randint(8196, 15374)

        print(storyscreen1(viewers, slices, money, energy, name, created, t1))  #сюжет в картинках

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        clear_screen()
        print(storyscreen2(viewers, slices, money, energy))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        clear_screen()
        print(storyscreen3(viewers, slices, money, energy))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        newtime = time.ctime().split()
        t2 = newtime[-2][:-3]
        clear_screen()
        print(storyscreen4(viewers, slices, money, energy, name, created, t2))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        clear_screen()
        print(storyscreen5(viewers, slices, money, energy))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        clear_screen()
        print(storyscreen6(viewers, slices, money, energy))

        for i in range(1, 4):
            print('. ' * i)
            time.sleep(1.5)
            print('\033[1F\033[0K', end='', flush=True)
        nextt = input('\033[2mНажми Enter чтобы продолжить...\033[0m')

        clear_screen()

        print(screen(slices, money, energy,
                     ' * Если ты запускаешь игрушку первый раз, желательно прочитать обучение',
                     '',
                     'Выбери одно из перечисленного:',
                     '',
                     '[1] - Открыть полное обучение',
                     '[2] - Открыть базовый минимум обучения',
                     '[0] - "Я и так всё знаю, включай уже игрушку"',
                     '',
                     'Введи цифру, соответствующую твоему выбору (и нажми Enter)'))


        choice = input(' >> ')

        while not choice in ('0', '1', '2'):
            print('\033[1F\033[0K', end='', flush=True)
            choice = input('Неподходящее значение. Ты должен ввести цифру 0, 1 или 2 >> ')

        if choice == '1':
            fulltutor()
            nextt = input()

        elif choice == '2':
            basetutor()
            nextt = input()

        clear_screen()

        for days in range(1, 32):     #цикл день/ночь, работа/стрим

            if streamstreak <= 3:   #первые 3 стрима подряд - 100%, далее - -25% от шанса на проведение стрима
                onstream()
                streamstreak += 1
            else:
                streamchance -= 0.25
                if random.choices((True, False), (streamchance, (1 - streamchance)), k=1)[0]:
                    onstream()
                    streamstreak += 1
                else:
                    print('У Антона сегодня выходной!')
                    streamstreak = 0
                    streamchance = 1.0
                    time.sleep(3)

            if reset == '1':
                break

            clear_screen()

            print(f'ДЕНЬ {days}')

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1)
                print('\033[1F\033[0K', end='', flush=True)
            clear_screen()

            if days % 4 != 0:    #проверка - выходной или рабочий день

                #рабочий день

                if energy.value == 0:   #после стрима энергия на нуле = проспал работу
                    print('Ты проспал!')
                    print('Тебе выписали штраф за опоздание на работу...')

                    if misses == 0:
                        print('\033[2m-100 ₽\033[0m')
                        money.value -= 100
                        misses += 1
                    elif misses <= 3:
                        print('\033[2m-250 ₽\033[0m')
                        money.value -= 250
                        misses += 1
                    else:
                        print('\033[2m-500 ₽\033[0m')
                        money.value -= 500
                        misses += 1

                    print('')

                    print('За ночь +30 ∈')
                    energy.value += 30

                else:
                    print('За ночь +20 ∈')
                    energy.value += 20

                print('')
                for i in range(1, 4):
                    print('. ' * i)
                    time.sleep(1.5)
                    print('\033[1F\033[0K', end='', flush=True)
                clear_screen()

                work()

                nomoney()

                if reset == '1':
                    break

            else:

                #сегодня выходной

                print('Сегодня у тебя выходной! Ты выспался! \033[2m(100 ∈)\033[0m')
                energy.value = 100

                print('')
                for i in range(1, 4):
                    print('. ' * i)
                    time.sleep(1.5)
                    print('\033[1F\033[0K', end='', flush=True)

            clear_screen()
            print('Ежедневные затраты на еду == -500 ₽')
            money.value -= 500

            for i in range(1, 4):
                print('. ' * i)
                time.sleep(1.5)
                print('\033[1F\033[0K', end='', flush=True)

            nomoney()

            if reset == '1':
                break

            clear_screen()

            if not rentpayed:   #если за аренду не заплатили
                if days >= 14:      #если прошло 2 недели от начала игры
                    if not rentchance == 1:     #если шанс на звонок ещё не 100%
                        paytoday = random.choices((0, 1), ((1 - rentchance), rentchance))
                        rentchance += 0.1
                    else:
                        paytoday = 1

                    if paytoday:
                        print('Тебе позвонили насчёт аренды квартиры...')
                        print(f'Нужно заплатить {rent} ₽')
                        print('')

                        time.sleep(1.5)
                        print('[0] - У меня сейчас нет денег...')
                        print(f'[1] - Заплатить \033[2m(У тебя {money.value} ₽)\033[0m')
                        print('')

                        action = input('Выбери действие \033[2m(его номер)\033[0m - ')

                        while not action in ('0', '1'):
                            print('\033[1F\033[0K', end='', flush=True)
                            action = input('Неподходящее значение. Выбери действие \033[2m(его номер)\033[0m - ')

                        print('\033[4F\033[0J', end='', flush=True)

                        if action == '0':   #говорим, что не можем заплатить сегодня
                            print('Ты сказал, что не сможешь оплатить сегодня...')
                            print('За каждый просроченный день к аренде добавляется +500 ₽')
                            rent += 500

                        else:               #оплачиваем аренду
                            if money.cantake(rent):     #денег хватает
                                print('Ты оплатил аренду!')
                                print(f'\033[2m-{rent} ₽\033[0m')
                                rentpayed = 1

                            else:                       #денег не хватает
                                print('У тебя не хватает денег на оплату аренды...')
                                print('Ты сказал, что не сможешь оплатить сегодня...')
                                print('За каждый просроченный день к аренде добавляется +500 ₽')
                                rent += 500

        else: #просмотр финального стрима
            if streamstreak <= 3:   #первые 3 стрима подряд - 100%, далее - -25% от шанса на проведение стрима
                onstream()
                streamstreak += 1
            else:
                streamchance -= 0.25
                if random.choices((True, False), (streamchance, (1 - streamchance)), k=1)[0]:
                    onstream()
                    streamstreak += 1
                else:
                    print('У Антона сегодня выходной!')
                    streamstreak = 0
                    streamchance = 1.0

        if (slices.value < 5000000) and reset != '1':
            clear_screen()
            print('Ты не успел накопить 5 000 000 баллов...')

            time.sleep(1.5)
            print('Ты проиграл...')

            time.sleep(1.5)
            print('Не хочешь попробовать ещё раз?')
            print('')

            reset = input('Введи "1", чтобы попробовать снова - ')

        else:
            win()

        if reset != '1':
            break


slices = points(random.randint(30, 60) * 100, '₫')
money = points(random.randint(4, 9) * 100, '₽')
energy = points(random.randint(4, 7) * 10, '∈')
streak = random.randint(2, 6)
name = 'defaultname'
reset = 0
orders = 0
ords = []
mistakes = 0
rentpayed = 0


if __name__ == '__main__':

    rungame()

    exitt = input('Enter для выхода ')