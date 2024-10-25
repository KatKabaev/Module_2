def draw_area():
    for i in area:
        print(*i)


area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Крестики-нолики')
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ход "0"')
    else:
        turn_char = 'X'
        print('Ход "X"')
    row = int(input('Введите номер строки (1, 2, 3): ')) - 1
    column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    area[row][column] = turn_char
    draw_area()

    if check_winner() == 'X':
        print("Победа Х")
        break                                       # выход из цикла

    if check_winner() == '0':
        print("Победа 0")
        break
    if check_winner() == '*' and turn == 9
        print("Ничья")
        