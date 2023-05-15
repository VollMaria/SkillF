"""Приветствие"""
def hello():
    print('          Начинаем игру')
    print('        в крестики-нолики!')
    print()
    print('    Правила:')
    print('     * Координаты клетки - "x" и "y"')
    print('     * x - номер строки')
    print('     * y - номер столбца')
    print('     * Первыми ходят крестики')
    print('     * Выигрывает тот, кто первым заполнит ряд')
    print()
    print('          Желаю удачи!')


"""Вывод пустого поля"""
def print_board():
    print(f"  0 1 2")
    for i in range(3):
        print(f'{i} {board[i][0]} {board[i][1]} {board[i][2]}')

# print_board()

"""Ввод координат и проверка"""
def move():
    while True:
        print(f'        Введите координаты:')
        step = input('          x, y: ').split()

        if len(step) != 2:
            print('Нужно ввести 2 значения!')
            continue

        x, y = step

        if not(x.isdigit()) or not(y.isdigit()):
            print('Нужно ввести числа!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Нужно ввести значения от 0 до 2!')
            continue

        if board[x][y] != '-':
            print('Это место уже занято!')

        return x, y

"""Проверка выигрыша"""
def winner():
    win_list = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_list:
        symbols = []
        for i in coord:
            symbols.append(board[i[0]][i[1]])
            if symbols == ["X", "X", "X"]:
                print(f'{name_1}, поздравляю, ты выиграл !!!')
                return True
        if symbols == ["0", "0", "0"]:
                print(f'{name_2}, поздравляю, ты выиграл !!!')
                return True
    return False


hello()
name_1, name_2 = input('Игрок 1, введите ваше имя: '), input('Игрок 2, введите ваше имя: ')
board = [["-"] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    print_board()
    if count % 2 == 1:
        print(f'Ходит {name_1}!')
    else:
        print(f'Ходит {name_2}!')

    x, y = move()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if winner():
        break

    if count == 9:
        print(" Ничья!")
        break
