# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

dcl = int(input('Введите число : '))


# def decimal_to_binary(dcl):
#     bnr=[]
#     while dcl > 0:
#         if dcl%2 ==0:
#             bnr.append(0)
#             dcl/=2
#         else:
#             dcl%2 !=0
#             bnr.append(1)
#             dcl=(dcl-1)/2
#     return bnr
#
# print(decimal_to_binary(dcl))


def dec_to_bi(d):
    return bin(d).replace("0b","")
print(dec_to_bi(dcl))
