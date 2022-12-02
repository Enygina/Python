# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт
# разницу между максимальным и минимальным
# значением дробной части элементов.

from random import uniform

def get_real_nums (n): #Генерация случайных дробных чисел от 1 до 10 с 3 символами после запятой
    lst=[]
    for i in range(n):
        lst.append(round(uniform(1, 10), 3))
    print(lst)
    return lst

def max_min_fraction_diff (lst):# нахождение разницы мин макс дробной части
    dif=[]
    for i in (lst):
        dif.append(round(i - int(i), 3))
        i+=1
    print(dif)
    return round((max(dif) - min(dif)),3)

n=int(input('Ведите кол-во элементов списка: '))

print(f'Разница: {max_min_fraction_diff(get_real_nums(n))}')


