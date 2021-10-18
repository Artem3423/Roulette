import random
import time


def pylet():
    print('-----\n'
          '//              3к  6ч  9к 12к  15ч  18к  21к  24ч  27к  30к  33ч  36ч | 1.1  2 к 1 (x3) 1й - ряд|  \\\\\n'
          '||  |0 (x36) |  2ч  5к  8ч 11ч  14к  17ч  20ч  23к  26ч  29ч  32к  35к | 1.2  2 к 1 (x3) 2й - ряд|  ||\n'
          '||              1к  4ч  7к 10ч  13ч  16к  19к  22ч  25к  28ч  31ч  34ч | 1.3  2 к 1 (x3) 3й - ряд|  ||\n'
          '||             |2.1  1ая-дюжина| 2.2   2ая-дюжина | 2.3    3ия-дюжина | (x3)                        ||\n'
          '||             |от 1 до 18|чётные|красное|чёрное|нечётные|от 19 до 36 | (x2)                        ||\n'
          '\\\\             |   3.18   | 3.4  |  3.1  |  3.2 |   3.3  |   3.36     |                             //\n')


def helpryl():
    print('-----\n'
          '// (x Число) Означает во сколько раз увеличится ваша ставка при выигрыше. Пример: (x3)       \\\\\n'
          '|| Чтобы поставить на число, просто впишите его (без буквы означающей цвет числа) Пример: 19 ||\n'
          '|| Чтобы поставить на какое то поле впешите (x.x). Пример: 1.2                               ||\n'
          '|| Все числа вводить в числовом формате. Пример: 3.36                                        ||\n'
          '\\\\ x = цифра                                                                                 //')


def st21andBJ(chisl, x=1):  # st21andBJ = lambda chisl, x: chisl - (chisl * 2) if x == 0 else chisl  # Функция для расчёта и вывода выигрыша (21 и BJ)
    if x == 0:  # chisl - (chisl * 2) if x == 0 else chisl
        chisl -= (chisl * 2)
    return chisl


def stavRyl(chisl, pole, x, win=0):  # Функция для расчёта и вывода выигрыша (Рулетка)
    chisl = int(chisl)
    if win == 1:
        chisl = chisl * x
        print('-----\nВы выйграли. Ваш выйгрышь составил:', probel(chisl), ' Со ставки на:', pole, '(' + poleStav[pole] + ')  Коэфицент был: (x' + str(pstavkaPolex[pole]) + ')')
        time.sleep(1)
    else:
        chisl -= chisl * 2
        print('-----\nВы проиграли:', probel(chisl), ' Со ставки на:', pole, '(' + poleStav[pole] + ')  Коэфицент был: (x' + str(pstavkaPolex[pole]) + ')')
        time.sleep(1)
    return chisl


def probel(chisl):  # Функция для пробело в больших числах
    if int(chisl) >= 1000 or int(chisl) <= -1000:
        chisl = str(chisl)
        for h in range(len(chisl) // 3):
            chisl2 = chisl[:-(3 + (h * 3) + h)] + ' ' + chisl[-(3 + (h * 3) + h):]
            chisl = chisl2
        if chisl[0] == ' ':
            chisl = chisl[1:]
    return chisl


def balryl(fbalance, chisl):  # Воспомогательная функция для расчёта и вывода баланса к функии stavRyl
    fbalance += chisl
    print('Ваш баланс в итоге составил:', probel(fbalance))
    return fbalance


def Save():  # Функция для сохранения игры (баланса и профиля)
    with open('Profili_users.txt', 'r') as profili_f, open('system.txt', 'w') as vrem_f:  # Два файла отвечают за перезапись данных профилей
        for line_f in profili_f:
            if line_f.count(Name) > 0:
                global SaveBalance
                line_f = line.replace(str(SaveBalance), str(balance))
                SaveBalance = balance
                vrem_f.write(line_f)
            else:
                vrem_f.write(line_f)
    with open('Profili_users.txt', 'w') as profili_f, open('system.txt', 'r') as vrem_f:
        profili_f.write(vrem_f.read())


kart = ('6', '7', '8', '9', '10', 'B', 'D', 'K', 'T')
kart21 = (6, 7, 8, 9, 10, 2, 3, 4, 11)
kartBJ = (6, 7, 8, 9, 10, 10, 10, 10, 11)
mast = ('б', 'ч', 'п', 'к')
pstavka = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36')
colorstavka = ('z', 'к', 'ч', 'к', 'ч', 'к', 'ч', 'к', 'ч', 'к', 'ч', 'ч', 'к', 'ч', 'к', 'ч', 'к', 'ч', 'к', 'к', 'ч', 'к',
               'ч', 'к', 'ч', 'к', 'ч', 'к', 'ч', 'ч', 'к', 'ч', 'к', 'ч', 'ч', 'к', 'ч')
slcolor = dict(zip(pstavka, colorstavka))
pstavka2 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
            '1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.18', '3.4', '3.1', '3.2', '3.3', '3.36')
pstavkax = (36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36,
            36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2)
pstavkaPolex = dict(zip(pstavka2, pstavkax))
pstavkaName = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
               '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
               '2 к 1 - 1й ряд', '2 к 1 - 2й ряд', '2 к 1 - 3й ряд', '1ая-дюжина', '2ая-дюжина', '3ия-дюжина',
               'от 1 до 18', 'чётные', 'красное', 'чёрное', 'нечётные', 'от 19 до 36')
poleStav = dict(zip(pstavka2, pstavkaName))
vrmMen = []
vrmPC = []
pTrue = ''
games = ''
Name = ''
stavka = 0
Men = 0
PC = 0
SaveBalance = 0
balance = 10000

while True:
    pTrue = str(input('-----\nНажмите ENTER, если хотите выбрать существующий профиль, или нажмите ПРОБЕЛ и ENTER если хотите создать новый.'))
    if pTrue == '':
        with open('Profili_users.txt', 'r') as profili:  # profili = open('Profili_users.txt', 'r')  -->  with open('Profili_users.txt', 'r') as profili:
            lineNum = 0
            print('-----')
            for line in profili:
                vr = tuple(line.split(':'))
                lineNum += 1
                print(str(lineNum) + '.', vr[0], ' Баланс:', vr[1].strip())

        while True:
            vr = input('-----\nВыберите профиль, для этого введите номер профиля --> ')
            if not vr.isnumeric():
                print("-----\nВы ввели не число. Попробуйте снова: ")
            elif int(vr) > lineNum or int(vr) <= 0:
                print('-----\nТакого номера нет.')
            else:
                break

        with open('Profili_users.txt', 'r') as profili:
            lineNum = 0
            for line in profili:
                lineNum += 1
                if str(lineNum) == vr:
                    vr = tuple(line.split(':'))
                    Name = vr[0]
                    balance = int(vr[1])
                    SaveBalance = balance
                    break
        break
    elif pTrue == ' ':

        print('-----\n'
              '// Имя профиля должно содержать только Латинские символы. \\\\\n'
              '|| Имя профиля не может быть пустым.                      ||\n'
              '\\\\ Имя профиля не может содержать двоеточие --> : <--     //')

        with open('Profili_users.txt', 'r') as profili:
            for line in profili:
                vr = tuple(line.split(':'))
                vrmMen.append(vr[0])

        while True:  # Проверка корректности ввода имени профиля
            vrem = str(input('-----\nВведите имя нового профиля --> '))
            if ':' in vrem:
                print('Имя профиля не может содержать двоеточие --> : < --  Попробуйте снова.')
            elif len(vrem) == 0:
                print('Имя профиля не может быть пустым. Попробуйте снова.')
            elif vrem in vrmMen:
                print('Имя профиля не может повторяться. Попробуйте снова.')
            else:
                with open('Profili_users.txt', 'a') as profili:
                    profili.write('\n' + vrem + ':10000')
                print('-----\nВам было зачисленно 10 000 деревянных')
                vrmMen.clear()
                break
    else:
        print('Неверная кнопка. Нажмите ENTER, или нажмите ПРОБЕЛ и ENTER.')

print('Здравствуйте, ' + Name + '. Ваш баланс:', balance, 'деревянных')

while pTrue == '':
    games = str(input('-----\nВо что будете играть?\n'
                      ' Игры:  1. 21\n'
                      '        2. Рулетка\n'
                      '        3. BJ\n'
                      '        4. Рулетка (Pre-Alpha)\n'
                      'Введите номер игры (без точки). --> '))

    if games == '1':  # 21
        while pTrue == '':
            print('-----\nНачинаем!')

            while True:  # Цикл отвечающий за проверку корректности ввода ставки
                stavka = input('Сколько хотите поставить? --> ')
                if not stavka.isnumeric():
                    print("-----\nВы ввели не число. Попробуйте снова: ")
                elif 0 > int(stavka):
                    print('-----\nСтавка не может быть отрицательной.')
                elif balance < int(stavka):
                    print('-----\nНа вашем счету недостаточно средст для такой большой ставки.')
                else:
                    stavka = int(stavka)
                    break

            print('-----\nКомпьютер начинает.')
            while PC < 18:  # pc
                if PC < 18:
                    vr = random.randint(0, 8)
                    PC = PC + kart21[vr]
                    vrmPC.append(kart[vr])
                    print('Карты ПК: (', ', '.join(vrmPC), ') Очки:', PC)
                time.sleep(1)
            if PC == 21:
                print('-----\nКомпьютер выбил очко! Вы проиграли! Вы проиграли:', st21andBJ(stavka, 0))
                balance = balryl(balance, st21andBJ(stavka, 0))
                break
            print('-----')
            if PC < 22:
                while pTrue == '':  # you
                    vr = random.randint(0, 8)
                    Men = Men + kart21[vr]
                    vrmMen.append(kart[vr])
                    print('Твои карты (', ', '.join(vrmMen), ') Твои очки:', Men)
                    time.sleep(1)
                    if Men > 21:
                        print('-----\nУ вас перебор. Вы проиграли. Вы проиграли:', st21andBJ(stavka, 0))
                        balance = balryl(balance, st21andBJ(stavka, 0))
                        break
                    pTrue = str(input('-----\nНажмите ENTER, если хотите взять ещё одну карту, или нажмите ПРОБЕЛ и ENTER.'))
                if Men < 22:
                    if Men > PC:
                        print('-----\nВы выйграли! Даже Компьютер в шоке! Ваш выигрышь составил:', st21andBJ(stavka))
                        balance = balryl(balance, st21andBJ(stavka))
                    elif Men == PC:
                        print('-----\nНичья! Ваш выигрышь составил: 0')
                        print('Ваш баланс в итоге составил:', balance)
            else:
                print('-----\nКомпьютер сделал перебор и проиграл! Вы выиграли! Ваш выигрышь составил:', st21andBJ(stavka))
                balance = balryl(balance, st21andBJ(stavka))

            Save()

            pTrue = str(input('-----\nНажмите ENTER, если хотите взять реванш, или нажмите ПРОБЕЛ и ENTER.'))
            PC, Men, stavka = 0, 0, 0
            vrmPC.clear()
            vrmMen.clear()

    elif games == '4':  # Рулетка (Pre-Alpha)
        while pTrue == '':
            ryl = ('красное', 'чёрное')
            rylv = str(input('-----\nНа какой цвет будите ставить? (красное или чёрное)'))
            vr = random.randint(0, 1)
            print('-----\nВыпадает:', ryl[vr])
            if ryl[vr] == rylv:
                print('-----\nВы выйграли!')
            else:
                print('-----\nВы проиграли!')
            pTrue = str(input('-----\nНажмите ENTER, если хотите попробовать ещё, или нажмите ПРОБЕЛ и ENTER.'))

    elif games == '2':  # Рулетка
        while pTrue == '':
            while True:
                pTrue = str(input('-----\nНажмите ENTER, если хотите увидеть игровое поле, или нажмите ПРОБЕЛ и ENTER.'))
                if pTrue == '':
                    pylet()
                    break
                elif pTrue == ' ':
                    break
                else:
                    print('Нажмите ENTER, или нажмите ПРОБЕЛ и ENTER.')
            while True:
                pTrue = str(input('-----\nНажмите ENTER, если хотите увидеть игровые подсказки, или нажмите ПРОБЕЛ и ENTER.'))
                if pTrue == '':
                    helpryl()
                    break
                elif pTrue == ' ':
                    break
                else:
                    print('-----\nНажмите ENTER, или нажмите ПРОБЕЛ и ENTER.')
            pTrue = ''

            while True:  # Цикл отвечающий за ввод поле и ставку на него

                vr = str(input('-----\nНа что будете ставить? (Введите чило (Пример: x.xx или x если ставите на число) без пробелов.) --> '))
                if vr.count('_') == 0 and pstavka.count(vr) > 0 or vr.count('_') == 0 and pstavka2.count(vr) > 0:

                    while True:  # Проверка корректности ставок
                        stavka = input('Сколько хотите поставить? --> ')
                        if not stavka.isnumeric():
                            print("-----\nВы ввели не число. Попробуйте снова: ")
                        elif 0 > int(stavka):
                            print('-----\nСтавка не может быть отрицательной.')
                        elif balance < int(stavka):
                            print('-----\nНа вашем счету недостаточно средст для такой большой ставки.')
                        else:
                            break

                    vrmMen.append(vr)
                    vrmPC.append(stavka)

                else:
                    print('-----\nНеверное число. Ставка не поставилась.')

                while True:  # Цикл проверки на верноомть ввода ENTER и ПРОБЕЛ
                    pTrue = str(input('-----\nНажмите ENTER, если хотите поставить ещё, или нажмите ПРОБЕЛ и ENTER.'))
                    if pTrue == ' ':
                        break
                    elif pTrue == '':
                        break
                    else:
                        print('-----\nВы не нажали ENTER, или  ПРОБЕЛ и ENTER. Нажмите ENTER, или нажмите ПРОБЕЛ и ENTER.')
                if pTrue == ' ':
                    break

            for i in range(random.randint(8, 14)):
                vr = random.randint(0, 36)
                print(vr, slcolor[str(vr)])
                time.sleep(0.5 + i / 10)

            print('Выпадает...')
            time.sleep(2)
            print('* Барабанная дробь *')
            time.sleep(2)
            vr = random.randint(0, 36)
            vr = str(vr)
            print(vr, slcolor[vr])

            pTrue = str(input('-----\nНажмите ENTER, чтобы увидеть результаты ваших ставок.'))

            for i in range(len(vrmMen)):  # Цикл проверки и вывода ставок
                if vrmMen[i].count('.') > 0:
                    mas = tuple(vrmMen[i].split('.'))
                    if mas[0] == '1':
                        if mas[1] == '1':
                            if vr in pstavka[3::3]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '2':
                            if vr in pstavka[2::3]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '3':
                            if vr in pstavka[1::3]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                    elif mas[0] == '2':
                        if mas[1] == '1':
                            if vr in pstavka[1:13]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '2':
                            if vr in pstavka[13:25]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '3':
                            if vr in pstavka[25:37]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                    elif mas[0] == '3':
                        if mas[1] == '1':
                            if slcolor[vr] == 'к':
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '2':
                            if slcolor[vr] == 'ч':
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '3':
                            if int(vr) % 2 != 0 and vr != '0':
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '4':
                            if int(vr) % 2 == 0 and vr != '0':
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '18':
                            if vr in pstavka[1:19]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                        elif mas[1] == '36':
                            if vr in pstavka[19:37]:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]], 1))
                            else:
                                balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], pstavkaPolex[vrmMen[i]]))
                else:
                    if vrmMen[i] == '0':
                        if vr == '0':
                            balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], 36, 1))
                        else:
                            balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], 36))
                    else:
                        if vr == vrmMen[i]:
                            balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], 36, 1))
                        else:
                            balance = balryl(balance, stavRyl(vrmPC[i], vrmMen[i], 36))

            Save()

            pTrue = str(input('-----\nНажмите ENTER, если хотите узнать свой баланс, или нажмите ПРОБЕЛ и ENTER.'))
            if pTrue == '':
                print('На вашем балансе осталось:', probel(balance), 'шекелей')
            pTrue = str(input('-----\nНажмите ENTER, если хотите попробовать ещё, или нажмите ПРОБЕЛ и ENTER.'))
            PC, Men, stavka = 0, 0, 0
            vrmPC.clear()
            vrmMen.clear()

    elif games == '3':  # BJ
        while pTrue == '':
            print('-----\nНачинаем!')

            while True:  # Цикл отвечающий за проверку корректности ввода ставки
                stavka = input('Сколько хотите поставить? --> ')
                if not stavka.isnumeric():
                    print("-----\nВы ввели не число. Попробуйте снова: ")
                elif 0 > int(stavka):
                    print('-----\nСтавка не может быть отрицательной.')
                elif balance < int(stavka):
                    print('-----\nНа вашем счету недостаточно средст для такой большой ставки.')
                else:
                    stavka = int(stavka)
                    break

            print('-----\nКомпьютер начинает.')
            while PC < 17:  # pc
                if PC < 17:
                    vr = random.randint(0, 8)
                    PC = PC + kartBJ[vr]
                    vrmPC.append(kart[vr])
                    if kart[vr] == 'T' and PC > 21:
                        PC = PC - 10
                    print('Карты ПК: (', ', '.join(vrmPC), ') Очки:', PC)
                time.sleep(1)
            if PC == 21:
                print('-----\nКомпьютер выбил очко! Вы проиграли! Вы проиграли:', st21andBJ(stavka, 0))
                balance = balryl(balance, st21andBJ(stavka, 0))
                break
            print('-----')
            if PC < 22:
                while pTrue == '':  # you
                    vr = random.randint(0, 8)
                    Men = Men + kartBJ[vr]
                    vrmMen.append(kart[vr])
                    if kart[vr] == 'T' and Men > 21:
                        Men = Men - 10
                    print('Твои карты (', ', '.join(vrmMen), ') Твои очки:', Men)
                    time.sleep(1)
                    if Men > 21:
                        print('-----\nУ вас перебор. Вы проиграли. Вы проиграли:', st21andBJ(stavka, 0))
                        balance = balryl(balance, st21andBJ(stavka, 0))
                        break
                    pTrue = str(input('-----\nНажмите ENTER, если хотите взять ещё одну карту, или нажмите ПРОБЕЛ и ENTER.'))
                if Men < 22:
                    if Men > PC:
                        print('-----\nВы выйграли! Даже Компьютер в шоке! Ваш выигрышь составил:', st21andBJ(stavka))
                        balance = balryl(balance, st21andBJ(stavka))
                    elif Men == PC:
                        print('-----\nНичья! Ваш выигрышь составил: 0')
                        print('Ваш баланс в итоге составил:', balance)
            else:
                print('-----\nКомпьютер сделал перебор и проиграл! Вы выиграли! Ваш выигрышь составил:', st21andBJ(stavka))
                balance = balryl(balance, st21andBJ(stavka))

            Save()

            pTrue = str(input('-----\nНажмите ENTER, если хотите взять реванш, или нажмите ПРОБЕЛ и ENTER.'))
            PC, Men, stavka = 0, 0, 0
            vrmPC.clear()
            vrmMen.clear()

    else:
        print('-----\nНеверное название игры')
    pTrue = str(input('-----\nНажмите ENTER, если хотите выбрать другую игру, или нажмите ПРОБЕЛ и ENTER что бы закончить игровую сессию.'))
print('-----\nВаш баланс:', balance)
print('-----\nСпасибо что сыграли.')
