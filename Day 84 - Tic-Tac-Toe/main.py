game_field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]


def show_field():
    print("   1  2  3")
    i = 1
    for f in game_field:
        print(f"{i} {''.join(f)}")
        i += 1


def check_win():
    for field in game_field:
        field_set = set(field)
        if len(field_set) == 1 and '[ ]' not in field_set:
            return True
    for i in range(3):
        if game_field[0][i] == game_field[1][i] == game_field[2][i]:
            if game_field[0][i] != '[ ]' or game_field[1][i] != '[ ]' or game_field[2][i] != '[ ]':
                return True
    if game_field[0][0] == game_field[1][1] == game_field[2][2] and game_field[2][2] != '[ ]':
        return True
    if game_field[2][0] == game_field[1][1] == game_field[0][2] and game_field[0][2] != '[ ]':
        return True
    return False


def mark_spot(player):
    mark = input(f"Write coordinates for putting {player} in form of two digits (e.g. 21) > ")
    cor = [int(char) for char in mark]
    if '[ ]' in game_field[cor[0]-1][cor[1]-1]:
        game_field[cor[0]-1][cor[1]-1] = game_field[cor[0]-1][cor[1]-1].replace('[ ]', f'[{player}]')
    else:
        print("This field is already taken!")
        mark_spot(player)
    show_field()
    if check_win():
        print(f"Player {player} wins!")
        return False
    return True


if __name__ == "__main__":

    show_field()
    while True:
        if not mark_spot('X') or not mark_spot('O'):
            break
