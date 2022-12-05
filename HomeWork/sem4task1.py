# Вычислить число Пи c заданной точностью d
# 10^-1 ≤ d ≤10^-10

from math import pi

d = int(input('Введите желаемое кол-во знаков после запятой от 1 до 10  '))
pi_str = str(pi)
print(pi_str[:d + 2])
