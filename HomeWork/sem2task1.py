# 4. Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.(строка)

str_num = input('Введите число ')
str_num = "".join(i for i in str_num if  i.isdecimal())  # убираем все символы
print(str_num)
num = [int(i) for i in str_num]  # из строки в список чисел
print(num)
print(sum(num))