# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

lst = list(map(int, input("Введите числа через пробел:\n").split(',')))
new_lst = []
dic = dict((i, lst.count(i)) for i in lst)
for k, v in dic.items():
    if v == 1:
        new_lst.append(k)
print(f'Неповторяющиеся элементы списка {new_lst}')
