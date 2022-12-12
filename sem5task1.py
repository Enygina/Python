# Посчитать НОК и НОД Числа

# n1 = int(input('Введите целое число : '))
# n2 = int(input('Введите целое число : '))
#
# list_of_factor = []
# list_of_factor_2 = []
#
#
# def f(n, list):
#     num_factor = 2
#     while n > 1:
#         if n % num_factor == 0:
#             list.append(num_factor)
#             n = int(n / num_factor)
#         else:
#             num_factor += 1
#
# f(n1,list_of_factor)
# f(n2,list_of_factor_2)
# print(set(list_of_factor))
# print(set(list_of_factor_2))
#
# nok_find = set(list_of_factor).intersection(list_of_factor_2)
# nod = 1
# for i in nok_find:
#     nod = nod * i
#
# nok = n1*n2/nod
# print(nod)
# print(nok)


import math

data = list(map(int, input("Введите два числа через пробел ").split()))

gcd = math.gcd(*data)
lcm = math.lcm(*data)

print(f'НОД: {gcd}, НОК: {lcm}')
