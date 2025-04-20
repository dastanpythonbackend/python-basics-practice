# 2. Дополните программу таким образом, чтобы рядом с
# названием каждой клетки выводился её цвет (black или white).
# Клетка A1 чёрная.

def print_chessboard_with_colors():
    columns = 'ABCDEFGH'
    rows = range(1, 9)

    for row in rows:
        for col_index in range(len(columns)):
            cell_name = f'{columns[col_index]}{row}'

            if (col_index + row) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            print(f'{cell_name}: {color}')


print_chessboard_with_colors()
