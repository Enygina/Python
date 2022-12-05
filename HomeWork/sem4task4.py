# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)*
# многочлена и записать в файл многочлен степени k.
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

from random import randint
import itertools

k = randint(2, 10)
k1 = randint(2, 10)


def rand_ratios(k):
    ratios = [randint(-100, 100) for i in range(k + 1)]
    return ratios


def get_polynomial(k, ratios):  # функция соединяет два списка разной длины
    pol = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[rt, p, r] for rt, p, r in itertools.zip_longest(
        ratios, pol, range(k, 1, -1), fillvalue='') if p != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x').replace('+ -', ' - ')


ratios = rand_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(f' Степень k: {k} \n Коэффициенты: {ratios} \n\n {polynom1}')

with open('s4t4_Polynomial.txt', 'w') as data:
    data.write(polynom1)

# Пятая задача
ratios = rand_ratios(k1)
polynom2 = get_polynomial(k1, ratios)

with open('s4t5_Polynomial.txt', 'w') as data:
    data.write(polynom2)
