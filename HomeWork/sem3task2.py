# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.
import math


def get_numbers():  # список чисел от пользователя
    num_list = [int(i) for i in input('Введите числа через запятую').split(",")]
    return num_list


def multiplication_pair(lst):  # перемножение пар через их удаление
    mult_pair=[]
    while len(lst) >1:
        mult_pair.append(lst[0]*lst[-1])
        del lst[0]
        del lst[-1]
    return mult_pair

def mult_pair(lst): # перемножение пар путем сторого деления длинны списка
    res = []
    for i in range(len(lst) // 2):
        res.append(lst[i] * lst[-i - 1])
        print({lst[i]}, {lst[-i - 1]})
        i += 1

    return res


print(f'Произведение пар чисел: {mult_pair(get_numbers())}')
# print(f'Произведение пар чисел: {multiplication_pair(get_numbers())}')
