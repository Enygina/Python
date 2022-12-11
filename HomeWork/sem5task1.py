# Создайте программу для игры с конфетами человек против человека.
import math

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один
# ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому  игроку, чтобы забрать
# все конфеты у своего конкурента
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

n = int(input('Выбери сколько конфет я у тебя выиграю '))
max_step = int(input('Теперь выбери, сколько максимум можно забрать за один ход '))
human = int(input('Рискни сделать первый ход: '))
rem_div = n % (max_step + 1)             # математическая формула победы для первого хода
ai = 0                                   # ход компьютера

# проверка введенного числа
if human > max_step or human < 1:
    human = int(input(f'Кто-то забыл правила игры...поробуй еще раз '))

# первый шаг
def first_step(human, max_step, n, rem_div):  # первый ход:
    """"Для победы первые два хода должны быть равны rem_div,
или, если пользователь ввел большее число, то rem_div+(max_step+1)"""
    if human in range(0, max_step + 1):
        if human > rem_div:
            ai = (rem_div + (max_step + 1)) - human
            n = n - ai - human
        elif human < rem_div:
            ai = rem_div - human
            n = n - ai - human
        elif human == rem_div:
            print('Сдаюсь, давай еще ')
            exit()
        print(f'Мой ход {ai}, осталось конфет:  {n} ')
    return n

def second_to_last_step(n):
    """"Следующие шаги должны быть равны (max_step + 1) - ход игрока"""
    while n > max_step + 1:
        human = int(input('Твой ход: '))
        if human > max_step or human < 1:
            human = int(input(f'Кто-то забыл правила игры...поробуй еще раз'))
        ai = max_step + 1 - human
        print(f'Мой ход {ai}, осталось конфет {n - human - ai} ')
        n = n - human - ai
    return n


def last_step(n):
    """"Вывод результата игры"""
    human = int(input('Твой ход: '))
    if human > max_step or human < 1:
        human = int(input(f'Кто-то забыл правила игры...поробуй еще раз'))
    if n-human == 0:
        print('Поздравляю! Бери свои конфетки, я требую реванш!')
    else:
        print(f'Мой ход {n-human}')
        print(f'Гони свои конфетки! Готов отиграться? ')




last_step(second_to_last_step(first_step(human, max_step, n, rem_div)))
