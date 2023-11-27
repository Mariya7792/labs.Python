from typing import Union, Optional

EMPTY_CELL = "_"


def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list:
    """
    Создает пустое поле для начала игры
    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: отображение пустого поля в виде списка списков

    """
    return [[empty_cell] * size for _ in range(size)]


def draw_field(field):
    """
    Функция рисует поле
    :param field: само поле

    """
    for line in field:
        print(line)


def get_int_val(text: str, border) -> int:
    """
   Спрашиваем у пользователя размеры поля и проверяем, ввел ли игрок правильное значение
   :param text: текст, который запрашивает данные
   :param border: границы размера поля
   """
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print('Пожалуйста, вводите только число')
            continue

        if number not in range(border[0], border[-1] + 1):
            print(f'Пожалуйста, введите число только в диапазоне от {border[0]} до {border[-1]}')
            continue

        return number


def get_char_val(text: str, req_list: list) -> str:
    """
    Пользователь вводит символ (0 или X). Проверяем, сответствует ли элемент, введенный пользователем, условиям задачи.
    Если нет, то просим заново ввести.
    :param text: текст, который запрашивает данные
    :param req_list: знак, который можно ввести
    :return: знак, выбранный пользователем
    """
    while True:
        symbol = input(text)
        if symbol not in req_list:
            print(f'Пожалуйста, введите знак из списка {req_list}!')
            continue

        return symbol


def get_index_from_table(field, size: int):
    """
    Спрашиваем у игрока, куда он хочет поставить символ. Получив ответ, проверяем, можно ли туда поставить
    :param field: поле игры
    :param size: размер поля
    :return: возвращаем индекс, куда можно поставить
    """
    while True:
        place_line = get_int_val("Укажите, в какую строку хотите поставить символ: ", (1, size)) - 1
        place_column = int(input("Укажите, в какой столбец хотите поставить символ:")) - 1

        index = [place_line, place_column]
        if field[place_line][place_column] == EMPTY_CELL:
            return index
        elif place_line > size or place_column > size:
            print("Вы вышли за пределы поля!")
            continue
        elif place_line == -1 or place_column == -1:
            print('Пожалуйста, введите символ!')
            continue
        else:
            print("Здесь уже есть символ. Пожалуйста, выберите другое место!")
            continue


def set_player_in_field(field,
                        current_player: str,
                        index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field: поле игры
    :param current_player: текущий игрок
    :param index_step: куда ставим игрока
    :return: возвращаем поле с текущим ходом игрока
    """
    index_lists = index_step[0]
    index_field = index_step[1]
    if field[index_lists][index_field] == EMPTY_CELL:
        field[index_lists][index_field] = current_player

    return field


def is_win(field):
    """
    Проверка, выигрышная ли компинация
    :param field: поле для игры
    :return: возвращаем поле после проверки
    """
    # Проверка по горизонтали
    for lists in field:
        if (set(lists)) == {'X'} or (set(lists)) == {'0'}:
            return True
        
    # Проверка по вертикали
    list_vertical = []
    for index in range(len(field)):
        for indexes in range(len(field)):
            list_vertical.append(field[index][indexes])
    border = len(field)
    for i in range(len(list_vertical[::3])):
        if set(list_vertical[i::border]) == {'X'} or set(list_vertical[i::border]) == {'0'}:
            return True

    # Проверка по диагонали
    list_diagonal_left = []
    list_diagonal_right = []
    index_left = 0
    index_right = -1
    for index in range(len(field)):
        list_diagonal_left.append(field[index][index_left])
        list_diagonal_right.append(field[index][index_right])
        index_left += 1
        index_right -= 1
    if set(list_diagonal_left) == {'X'} or set(list_diagonal_right) == {'X'}:
        return True
    elif set(list_diagonal_left) == {'0'} or set(list_diagonal_right) == {'0'}:
        return True
    else:
        return False


def change_player(current_player: str) -> str:
    """
    Определяет, кто ходит следующий

    :param current_player: текущий игрок
    :return: возвращает следующего игрока
    """
    if current_player == 'X':
        next_player = '0'
    if current_player == '0':
        next_player = 'X'

    return next_player


def game(player: str, size: int):
    """
    Запускает игру

    :param player: игрок, который ходит первым
    :param size: размер поля
    :return: выводим 'ничья' или возвращаем победителя
    """
    field_for_game = init_field(size)

    print('Ваше поле для игры:')
    draw_field(field_for_game)

    attempts = 0

    while attempts < size * size:
        player_chosen_index = get_index_from_table(field_for_game, size)
        current_field = set_player_in_field(field_for_game, player, player_chosen_index)
        if is_win(current_field) is True:
            print(f'Поздравляем! Игрок, выбравший {player}, выиграл!')
            break
        attempts += 1
        print('Смена игрока')
        print('Ваше поле после хода последнего игрока:')
        player = change_player(player)
        draw_field(current_field)

    if attempts == size * size:
        print('Ничья!')


def app():
    """
    Запуск приложения игры крестики-нолики
    """
    print('Добро пожаловать в игру крестики-нолики!')

    game_partner_choice = input('С кем вы хотели бы играть? С другим человеком(1) или компьютером(2)?')

    if game_partner_choice == '1':
        print('Игра запускается')
    else:
        print('Игра с компьютером пока в разработке. Запускаем игру с другим человеком')
    border = [3, 6]
    text_for_border = f'Выберите размер поля. Пожалуйста, введите число в диапазоне от {border[0]} до {border[-1]}:'
    border_number = get_int_val(text_for_border, border)

    req_list = ['0', 'X']

    text_for_player = f'Выберите, каким символом будете играть из значений {req_list}:'

    player_1 = get_char_val(text_for_player, req_list)
    if player_1 == 'X':
        player_2 = '0'
    else:
        player_2 = 'X'

    print(f'Первый игрок выбрал {player_1}, второй игрок: {player_2}')
    print('Начнем игру!')
    game(player_1, border_number)


if __name__ == "__main__":
    app()
