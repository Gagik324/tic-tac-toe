# Поля игры
board = list(range(1, 10))

# Счетчик ходов
counter = 0

# Флажок выйгрыша
is_win = False

# Условие побуды
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8)
    (0, 4, 8), (2, 4, 6),
)

def draw_board():
    print('Игра Крестики-нолики:')

    for i in range(3):
        print('-'*13)
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')

    print('-'*13)

# Игровой цикл
while not is_win:
    draw_board()

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answer = input(f'Куда ставим {player_token}?: ')

    # Получаем индекс для хода
    player_answer = int(player_answer) - 1

    # Проверяем, что ячейка свободна
    if board[player_answer] in ['X', 'O']:
        print('Ячейка уже занята')
        # Переходим к началу цикла
        continue

    # Делаем ход
    board[player_answer] = player_token
    counter += 1

    # Проверяем на выйгрыш
    for coords in win_coords:
        if board[coords[0]] == board[coords[1]] == board[coords[2]]:
            is_win = True
            break
    
    if is_win:
        draw_board()
        print(f"Победил {player_token}! Поздравляем!\n")
        break

    # Проверка на ничью
    if counter == 9:
        draw_board()
        print("Ничья! Игра окончена.\n")
        break