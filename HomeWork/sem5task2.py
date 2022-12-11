# Создайте программу для игры в ""Крестики-нолики"".

choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
choices_closed = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Is_Current_One = True
won = False
wrongEntryPlayer1 = False
wrongEntryPlayer2 = False

while not won:
    if not wrongEntryPlayer1 and not wrongEntryPlayer2:
        print('\n')
        print(' | ' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] + ' | ')
        print('---------------')
        print(' | ' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] + ' | ')
        print('---------------')
        print(' | ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] + ' | ')

    if Is_Current_One:
        print("Ходит первый игрок\nВыберите номер клетки для крестика")
        try:
            a = int(input())
            if a > 8 or a < 0:
                print("Неа...только от 1 до 9)")
                wrongEntryPlayer1 = True
                continue
            else:
                choice = a
            wrongEntryPlayer1 = False
        except ValueError:
            print("Неа...только от 1 до 9)")
            wrongEntryPlayer1 = True
            continue
    else:
        print("Ходит второй игрок\nВыберите номер клетки для нолика")
        try:
            a = int(input())
            if a > 8 or a < 0:
                print("Неа...только от 1 до 9)")
                wrongEntryPlayer2 = True
                continue
            else:
                choice = a
            wrongEntryPlayer2 = False
        except ValueError:
            print(("Неа...только от 1 до 9)"))
            wrongEntryPlayer2 = True
            continue

    if Is_Current_One:
        if choices[choice - 1] != int:
            if choices_closed[choice - 1] != '+':
                print(choices_closed)
                try:
                    choices[choice - 1] = 'X'
                    choices_closed[choice - 1] = '+'
                    wrongEntryPlayer1 = False
                except IndexError:
                    print(("Неа...только от 1 до 9)"))
                    wrongEntryPlayer1 = True
            else:
                print("Упс, тут занято1")
                Is_Current_One = False
        else:
            print("Выбери не занятое поле")
            wrongEntryPlayer1 = True
    else:
        if choices[choice - 1] != int:
            if choices_closed[choice - 1] != '+':
                print(choices_closed)
                try:
                    choices[choice - 1] = 'O'
                    choices_closed[choice - 1] = '+'
                    wrongEntryPlayer2 = False
                except IndexError:
                    print("Неа...только от 1 до 9)")
                    wrongEntryPlayer2 = True
            else:
                print("Упс, тут занято")
                Is_Current_One = True

        else:
            print("Выбери не занятое поле")
            wrongEntryPlayer2 = True

    Is_Current_One = not Is_Current_One

    for pos_x in range(0, 3):
        pos_y = pos_x * 3

        # горизонталь:
        if (choices[pos_y] == choices[(pos_y + 1)]) and (
                choices[pos_y] == choices[(pos_y + 2)]):
            won = True

        # вертикаль:
        if (choices[pos_x] == choices[(pos_x + 3)]) and (
                choices[pos_x] == choices[(pos_x + 6)]):
            won = True

        # диагональ
    if ((choices[0] == choices[4] and choices[0] == choices[8])
            or (choices[2] == choices[4] and choices[4] == choices[6])):
        won = True

print("Ура! Игрок " + str(int(Is_Current_One + 1)) + " победил.")
