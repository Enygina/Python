# 4. Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.(строка)


print(sum(list(map(lambda x: 0 if x == '.' else int(x), input('введите вещественное число: ')))))


# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.


def get_numbers():  # список чисел от пользователя
    num_list = [int(i) for i in input('Введите числа через запятую ').split(",")]
    return num_list


print(f'Сумма чисел с нечетным индексом: {sum(get_numbers()[1::2])}')


# Задайте список. Напишите программу, которая
# определит, присутствует ли в заданном списке
# строк некое число.


lst = ['nl', 'njw3', 'ghjk']
res = ((''.join(lst)).find('4'))
print('Нет' if res == -1 else 'Есть')


# Посчитать НОК и НОД Числа


import math

data = list(map(int, input("Введите два числа через пробел ").split()))

gcd = math.gcd(*data)
lcm = math.lcm(*data)

print(f'НОД: {gcd}, НОК: {lcm}')

dcl = int(input('Введите число : '))


# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.


def dec_to_bi(d):
    return bin(d).replace("0b", "")


print(dec_to_bi(dcl))


# 2. Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.


from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_prods(N))
