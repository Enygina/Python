# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = input('Введите текст:')
text = text.split(' ')
del_t = 'абв'
new_text = []
for word in text:
    if del_t not in word:
        new_text.append(word)
print(' '.join(str(i) for i in new_text))
