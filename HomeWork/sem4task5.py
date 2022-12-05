# Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.(одинаковый размер уравнений)*

import itertools

with open('s4t4_Polynomial.txt', 'r') as file:  # открываем файл, записываем в список
    poly_1 = file.readline().replace(' + ', ' ').replace(' - ', ' -').replace(' = 0', '')
    lst_of_poly_1 = poly_1.split()
    print(f'Первый многочлен: {lst_of_poly_1}')

with open('s4t5_Polynomial.txt', 'r') as file:  # открываем файл, записываем в список
    poly_2 = file.readline().replace(' + ', ' ').replace(' - ', ' -').replace(' = 0', '')
    lst_of_poly_2 = poly_2.split()
    print(f'Второй многочлен: {lst_of_poly_2}')

if len(lst_of_poly_1) > len(lst_of_poly_2):  # получаем список плюсов длинной меньшего многочлена
    len_p = len(lst_of_poly_2)
else:
    len_p = len(lst_of_poly_1)
lst_plus = [' + '] * (int(len_p))

poly_3 = [[l_1, l_p, l_2] for l_1, l_p, l_2 in itertools.zip_longest(   # соединяем списки многочленов и плюсов
    lst_of_poly_1, lst_plus, lst_of_poly_2, fillvalue='') if l_2 or l_1 != 0]

for x in poly_3:
    x.append(' + ')
poly_3 = list(itertools.chain(*poly_3))
poly_3[-1] = ' = 0'
poly_3 = "".join(map(str, poly_3)).replace('+ -', '-').replace('-', ' - ')
print(f'Сумма двух: {poly_3}')

with open('s4t5_Poly_final.txt', 'w') as data:
    data.write(poly_3)