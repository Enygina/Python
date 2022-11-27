# 5. Реализуйте алгоритм нахождения(генерации)
# рандомного(случайного) числа.(Не используя
# библиотеки связанные с рандомом)


import time


def rand_val(max):
    random = int(time.time() * 1000)

    random %= max

    return random


max = int(input('Введите максмальное число: '))

print(f'Случайное число: {rand_val(max)}')
