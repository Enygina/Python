# Задайте список. Напишите программу, которая
# определит, присутствует ли в заданном списке
# строк некое число.


lst = ['nl', 'njw3', 'ghjk']
num = 3
answer = False

# for i in lst:
#     if str(num)in i:
#         answer = True
#         break

# answer = False
# for i in lst:
#     for j in i:
#         if j == str(num):
#             answer = True
#             break

for i in lst:
    if i.count(str(num)):
        answer = True
print(answer)
