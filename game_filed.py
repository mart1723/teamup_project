
import consts
import random

game_filed = []
mine_list = []

def create_game_filed():
    for row in range(consts.BOARD_ROWS):
        game_filed.append([])
        for col in range(consts.BOARD_COLS):
            game_filed[row].append('')

def scatter_mines():
    mines_scattered = 0
    while mines_scattered < consts.MINE_COUNT:
        rnd_row = random.randrange(0, consts.BOARD_ROWS)
        start_col = random.randrange(0, consts.BOARD_COLS-2)
        if check_space(rnd_row, start_col, "mine") and check_col(start_col):
            for check in range(consts.MINE_COL):
                game_filed[rnd_row][start_col + check] = consts.MINE_NAME
            mines_scattered += 1
            mine_list.append((rnd_row, start_col))

def scatter_bushes():
    bushes_scattered = 0
    while bushes_scattered < consts.BUSH_COUNT:
        start_row = random.randrange(0, consts.BOARD_ROWS-1)
        start_col = random.randrange(0, consts.BOARD_COLS-1)
        if check_space(start_row, start_col, "bush"):
            for check_row in range(consts.BUSH_ROW):
                for check_col in range(consts.BUSH_COL):
                    if game_filed[start_row + check_row][start_col+check_col] != '':
                        game_filed[start_row + check_row][start_col + check_col] +="_"+consts.BUSH_NAME
                    else:
                        game_filed[start_row + check_row][start_col + check_col] = consts.BUSH_NAME
            bushes_scattered += 1


def check_space(row, col, object):
    if object == "mine":
        for check in range(consts.MINE_COL):
            if game_filed[row][col+check] != '':
                return False
        return True
    elif object == "bush":
        for check_row in range(consts.BUSH_ROW):
            for check_col in range(consts.BUSH_COL):
                if game_filed[row+check_row][col+check_col].find("Bush") != -1:
                    return False
        return True

    return False

def check_col(start_col):
    for col in range(start_col,consts.MINE_COL):
        mine_in_col = 0
        for row in range(consts.BOARD_ROWS):
            if game_filed[row][col] == 'mine':
                mine_in_col += 1

        if mine_in_col == consts.BUSH_ROW:
            return False
    return True

def touch_flag():
    pass

def touch_mine():
    pass

def get_game_filed():
    return game_filed