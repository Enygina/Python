# 1. Напишите программу вычисления арифметического выражения
# заданного строкой. Используйте операции +,-,/,*. приоритет
# операций стандартный.
#
# *Пример:*
#
# 2+2 => 4;
#
# 1+2*3 => 7;
#
# 1-2*3 => -5;
#
#


def multiplic(num):
    num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
    num.pop(num.index('*') + 1)
    num.pop(num.index('*'))


def division(num):
    num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
    num.pop(num.index('/') + 1)
    num.pop(num.index('/'))


def addit(num):
    num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
    num.pop(num.index('+') + 1)
    num.pop(num.index('+'))


def subtrac(num):
    num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
    num.pop(num.index('-') + 1)
    num.pop(num.index('-'))


num1 = '2 + 3 * 2 - 4 / 2'
num = num1.split()
print(num)
while len(num) > 1:
    while '*' in num or '/' in num:
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                multiplic(num)
            else:
                division(num)
        else:
            if '*' in num:
                multiplic(num)
            else:
                division(num)
    while '+' in num or '-' in num:
        if num.count('+') > 0 and num.count('-') > 0:
            if num.index('-') > num.index('+'):
                addit(num)
            else:
                subtrac(num)
        else:
            if '*' in num:
                addit(num)
            else:
                subtrac(num)

num = ''.join(map(str, num))
print(type(num))
print(f'{num1} = {num}')

line = input("Введите выражение: ")
line = line.split()
print(line)
result = 0


