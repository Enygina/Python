# Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них.

nams = [22, 39, 100, 8, 56]
max = nams[0]
for i in range(1, len(nams)):
    if nams[i] > max:
        max = nams[i]
print(f'max = {max}')
