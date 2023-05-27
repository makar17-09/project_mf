from random import randint

numsot = 0
def start():
    print('##▇▇▇########▇▇▇#####▇▇▇▇▇▇▇▇▇▇')
    print('##▇##▇▇####▇▇##▇#####▇▇')
    print('##▇####▇##▇####▇#####▇▇▇▇▇▇▇▇▇▇')
    print('##▇#####▇▇#####▇#####▇▇')
    print('##▇############▇#####▇▇')
    print('##▇############▇#####▇▇')
    print('')
    print('Добро пожаловать в консольный терминал, введите что-нибудь чтобы начать')
    input()

def onearif():
    while True:
        print('Введите end чтобы закончить')
        print('Введите первое число')
        fent = input()
        if fent == 'end':
            break
            start()
        print('Введите второе число')
        tent = input()
        if tent == 'end':
            break
            start()
        rslt = int(fent) + int(tent)
        print('Результат: ', rslt)
def twoarif():
    while True:
        print('Введите end чтобы закончить')
        print('Введите первое число')
        fent = input()
        if fent == 'end':
            break
            start()
        print('Введите второе число')
        tent = input()
        if tent == 'end':
            break
            start()
        rslt = int(fent) - int(tent)
        print('Результат: ', rslt)
def threearif():
    while True:
        print('Введите end чтобы закончить')
        print('Введите первое число')
        fent = input()
        if fent == 'end':
            break
            start()
        print('Введите второе число')
        tent = input()
        if tent == 'end':
            break
            start()
        rslt = int(fent) * int(tent)
        print('Результат: ', rslt)
def fourarif():
    while True:
        print('Введите end чтобы закончить')
        print('Введите первое число')
        fent = input()
        if fent == 'end':
            break
            start()
        print('Введите второе число')
        tent = input()
        if tent == 'end':
            break
            start()
        rslt = int(fent) / int(tent)
        print('Результат: ', rslt)
def fivearif():
    i = 0
    print('Введите числа')
    fiveent1 = input()
    fiveent2 = input()
    fiveent3 = input()
    fiveent4 = input()
    fiveent5 = input()
    rslt = ( int(fiveent1) + int(fiveent2) + int(fiveent3) + int(fiveent4) + int(fiveent5) ) / 5
    print('Результат: ', rslt)

start()
while True:
    print('')
    print('Вводите команду. (help для выведения списка команд)')
    enter = input('C:MarmaryFoundation>company>data>admin> ')
    statcp = randint(50, 100)
    if enter == 'help':
        print('')
        print('Список команд: \n'
              'help - выведение списка команд \n'
              'exit - выход из терминала \n'
              'quit - выход из терминала \n'
              'restart - перезапуск терминала \n'
              'open - открыть что-либо \n'
              'help open - список открывающегося \n'
              '21 - сыграть в очко')
    if enter == 'restart':
        start()
    if enter == 'help open':
        print('')
        print('Список открывающегося:')
        print('open archive - открыть архив сотрудников')
        print('open stat - просмотреть состояние ядра')
        print('open calc - открыть кальулятор')
    if enter == 'open stat':
        print('')
        print('Состояние ядра = ', statcp, '%')
    if enter == 'open archive':
        numsot = input('Введите номер сотрудника ')
        if numsot == '1':
            print('')
            print('ФИО: Гарлов Артём Филиппович')
            print('Дата рождения: 12.04.1982')
            print('Уровень доступа: научный сотрудник 2 уровня')
        if numsot == '2':
            print('')
            print('ФИО: Иригова Марта Ивановна')
            print('Дата рождения: 06.12.1984')
            print('Уровень доступа: научный сотрудник 1 уровня')
        if numsot == '3':
            print('')
            print('ФИО: Раков Матвей Семёнович')
            print('Дата рождения: 24.02.1978')
            print('Уровень доступа: научный сотрудник высшего уровня')
        if numsot == '4':
            print('')
            print('ФИО: Мартова Роза Петровна')
            print('Дата рождения: 03.20.1972')
            print('Уровня доступа: уборщик(ца)')
        if numsot == '5':
            print('')
            print('ФИО: Зубенко Михаил Петрович')
            print('Дата рождения: ?')
            print('Уровень доступа: мафиозник')
    if enter == 'open calc':
        print('')
        print('Какое арифметическое действие хотите выполнить?')
        print('Введите 1 чтобы сложить')
        print('Введите 2 чтобы вычесть')
        print('Введите 3 чтобы умножить')
        print('Введите 4 чтобы разделить')
        print('Введите 5 чтобы вычесть среднее арифметическое из пяти чисел')
        print('')
        calcent = input()
        if calcent == '1':
            onearif()
        if calcent == '2':
            twoarif()
        if calcent == '3':
            threearif()
        if calcent == '4':
            fourarif()
        if calcent == '5':
            fivearif()
    if enter == '21':
        useroc = 0
        aioc = 0
        genter = '1'
        while True:
            useroc = randint(1,15)
            aioc = randint(1,15)
            while aioc < 19:
                aioc = aioc + randint(2,6)
            while genter != '2':
                print('Ваше число: ', useroc, ". Введите 1 чтобы взять еще, 2 чтобы оставить.")
                genter = input()
                if genter == '1':
                    useroc = int(useroc) + randint(2,6)
            genter = '1'
            aioc2 = aioc
            aioc = 21 - aioc
            useroc = 21 - useroc
            if aioc < 0:
                print('Вы выиграли. Число соперника - ', aioc2)
            elif useroc < 0:
                print('Вы проиграли. Число соперника - ', aioc2)
            elif aioc > useroc:
                print('Вы выиграли. Число соперника - ', aioc2)
            elif useroc > aioc:
                print('Вы проиграли. Число соперника - ', aioc2)
            elif aioc == useroc:
                print('Ничья. Число соперника - ', aioc2)
            elif aioc < 0 and useroc < 0:
                print('Ничья. Число соперника - ', aioc2)



