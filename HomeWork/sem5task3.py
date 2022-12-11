str_for_rle = input("Введите текст для шифрования: ")


def rle_encode(s):
    encoding = ''
    prev_i = ''
    count = 1

    for i in s:
        if i != prev_i:
            if prev_i:
                encoding += str(count) + prev_i
            count = 1
            prev_i = i
        else:
            count += 1
    else:
        encoding += str(count) + prev_i
        return encoding
rle_encode=rle_encode(str_for_rle)
print(f'Закодированный текст: {rle_encode}')

def rle_decode(s):
    decode=''
    count=''
    for i in s:
        if i.isdigit():
            count+=i
        else:
            decode+=i*int(count)
            count=''
    return decode

rle_decode=rle_decode(rle_encode)
print(f'Разкодированный текст: {rle_decode}')

