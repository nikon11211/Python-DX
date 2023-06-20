import random


def is_valid(n, x, y):  # проверка на соответствие введенного значения условию
    return n.isdigit() and float(n) - int(float(n)) == 0 and x <= int(n) <= y


# ввод данных, значениями по умолчанию заданы верхний и нижний возможные пределы
def input_num(down_num=0, up_num=99999999999999999999999999):
    while True:
        guess = input()
        if is_valid(guess, down_num, up_num):
            return int(guess)
        else:
            print(
                f'А может быть все-таки введем целое число от {down_num} до {up_num}?')


# Сравнение введенного значения с загаданным
def compare_num(down_num, up_num):
    num = random.randint(down_num, up_num)
    total = 0
    while True:
        n = input_num(down_num, up_num)
        total += 1
        if n < num:
            print('Не угадали, попробуйте число побольше')
        elif n > num:
            print('Мимо, назовите число поменьше')
        else:
            print('Победа!!! Вы угадали ответ с',
                  total,  'попытки, поздравляем!')
            break


def continue_game():  # Предложение продолжить игру
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input(
                'Так да или нет?...\nПродолжим (д/н)?')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True


def game():  # Запуск игры
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа:')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y)
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break


game()  # Вызов игры
