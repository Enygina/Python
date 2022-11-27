# 4. Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.
#
# num=float(input('Введите число '))
# while num%1 != 0:
#     num*=10
# sum = 0
# while num>0:
#     res = num % 10
#     sum+=res
#     num//=10
# print(int(sum))

# str_num = input('Введите число ')
# num = [int(a) for a in str(str_num)] # из строки в список чисел
# print(sum(num))

# str_num = input('Введите число ')
# str_num = str_num.replaceAll("[^0-9]", "")
# print(str_num)

str_num = input('Введите число ')
str_num = "".join(i for i in str_num if  i.isdecimal())  # убираем все символы
print(str_num)
num = [int(i) for i in str_num]  # из строки в список чисел
print(num)
print(sum(num))
