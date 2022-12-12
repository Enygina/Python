# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

def get_numbers():  # список чисел от пользователя
    num_list = [int(i) for i in input('Введите числа через запятую ').split(",")]
    return num_list

#
# def find_odd_pos(list):  # нахождение нечетных позиций
#     odd_pos = []
#     for i in range(len(list)):
#         i = 1
#         odd_pos.append(list[i])
#         i += 2
#     return odd_pos
# print(f"Сумма чисел с нечетным индексом: {sum(find_odd_pos(get_numbers()))}")

print(f'Сумма чисел с нечетным индексом: {sum(get_numbers()[1::2])}')



