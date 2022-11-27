# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

def get_numers(n):  # создаем список от -n до n
    lst = []
    for i in range(-n, n + 1, 1):
        lst.append(i)
    return lst


with open('sem2task4hw.txt', 'w') as data:  # создает файл txt с индексами
    data.write('0\n')
    data.write('2\n')
    data.write('4\n')


def get_num_from_txt(txt):  # переводим индексы из файла в список
    data = open(txt, 'r')
    numlist = [int(line.strip()) for line in data]
    data.close()
    return numlist

def mult_index (numbers, numlist):
    mult = 1
    for i in numlist:
        mult *= numbers[i]
    return mult

n = int(input('Введите число N: '))
numbers = get_numers(n)
txt = 'sem2task4hw.txt'
numlist = get_num_from_txt(txt)

print(f'Список от -N до N: {numbers}')
print(f'Индексы из файла txt: {numlist}')
print(f'Произведение элементов: {mult_index(numbers,numlist)}')