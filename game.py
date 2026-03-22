from random import randint # импортируем функцию randint из модуля random

def is_digital(number): # функция проверки на ввод числа
    num = number.strip()
    while True:
        if not num.isdigit() or int(num) == 0:
            print('Некорректные данные, введите число!')
            num = input('Введите число: ').strip()
        else:
            return int(num)


def is_valid(number, r_side, num_list): # функция проверки ввода числа по условиям
    num = is_digital(number)
    while True:
        if 1 <= num <= r_side and num not in num_list:
            return num
        elif 1 <= num <= r_side and num in num_list:
            print(f'Вы уже вводили данное число!')
            num = is_digital(input('Введите число: '))
        else:
            print(f'Число вне допустимого предела от 1 до {r_side}!')
            num = is_digital(input('Введите число: '))

def compare(num, secret): # функция сравнения введенного числа и сгенерированного
    if num > secret:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif num < secret:
        print('Ваше число меньше загаданного, попробуйте еще разок')

def answer(ans): # функция проверки ответа о повторной игре
    if ans.lower() in ['д', 'да', 'y', 'yes']:
        return True
    else:
        return False

def game(): # функция игры
    print('Добро пожаловать в числовую угадайку!')
    r_side = is_digital(input('Введите правую границу для случайного выбора числа от 1 до: '))
    secret = randint(1, r_side)
    num_list = []  # список введённых чисел
    cnt = 0  # счётчик попыток

    while True:
        num = is_valid(input(f'Угадайте загаданное целое число от 1 до {r_side}: '), r_side, num_list)
        num_list.append(num)
        cnt += 1
        compare(num, secret)
        print(f'Введенные числа: {num_list}')
        print(f'Количество попыток: {cnt}')
        if num == secret:
            print('-' * 18)
            print('Вы угадали, поздравляем!')
            print(f'Загаданное число: {secret}')
            print(f'Введенные числа: {num_list}')
            print(f'Всего попыток: {cnt}')
            break

again = 'True'
while again:
    game()
    again = answer(input('Хотите сыграть ещё раз?(д / н) '))
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

