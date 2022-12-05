# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input("Введите число: "))
simp_num = 2

lst = []
num = n
while simp_num <= n:
    if n % simp_num == 0:
        lst.append(simp_num)
        n //= simp_num
    else:
        simp_num += 1
print(f"Простые множители числа {n} : {lst}")