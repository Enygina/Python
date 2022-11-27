# 2. Для натурального n создать словарь
# индекс-значение, состоящий из элементов
# последовательности 3n + 1.

n = int(input('Введите N: '))
# n_list={}
# for i in range(1, n+1):
#     n_list[i]=i*3+1
n_list = {i: i * 3 + 1 for i in range(1, n + 1)}
print(n_list)
