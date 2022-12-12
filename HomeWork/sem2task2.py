# 2. Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.
import math

# n = int(input('Введите N: '))
# a = 1
# f = 1
# for i in range(n):
#     print(f, end=' ')
#     f *= a + 1
#     a += 1
#
# for i in range(n):
#     f = math.factorial(a)
#     print(f, end=' ')
#     a += 1


from itertools import accumulate
import operator

N = int(input('Введите число: '))


def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_prods(N))
