
import consts
import random

game_filed = []
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS


def create_game_filed():
    global game_filed
    for row in range(consts.BOARD_ROWS):
        game_filed.append([])
        for col in range(consts.BOARD_COLS):
            game_filed[row].append('')

def create_flag():
    flag_cord = []
    for row in range(flag_row, consts.BOARD_ROWS):
        for col in range(flag_col, consts.BOARD_COLS):
            game_filed[row][col] = consts.FLAG_NAME
            flag_cord.append((row, col))
    return flag_cord


def scatter_mines():
    mines_scattered = 0
    mine_map = []
    while mines_scattered < consts.MINE_COUNT:
        rnd_row = random.randrange(0, consts.BOARD_ROWS)
        start_col = random.randrange(0, consts.BOARD_COLS-2)
        if (check_space(rnd_row, start_col, consts.MINE_NAME) and check_col(start_col) and
                not_in_spawn(rnd_row, start_col) and not_in_flag(rnd_row, start_col)):
            for check in range(consts.MINE_COL):
                game_filed[rnd_row][start_col + check] = consts.MINE_NAME
            mines_scattered += 1
            mine_map.append((rnd_row, start_col))
    return mine_map

def scatter_bushes():
    bushes_scattered = 0
    bushes_map = []
    while bushes_scattered < consts.BUSH_COUNT:
        start_row = random.randrange(0, consts.BOARD_ROWS-1)
        start_col = random.randrange(0, consts.BOARD_COLS-1)
        if check_space(start_row, start_col, consts.BUSH_NAME):
            for check_row in range(consts.BUSH_ROW):
                for check_col in range(consts.BUSH_COL):
                    if game_filed[start_row + check_row][start_col+check_col] != '':
                        game_filed[start_row + check_row][start_col + check_col] +="_"+consts.BUSH_NAME
                    else:
                        game_filed[start_row + check_row][start_col + check_col] = consts.BUSH_NAME
            bushes_scattered += 1
            bushes_map.append((start_row, start_col))
    return bushes_map


def check_space(row, col, object):
    if object == consts.MINE_NAME:
        for check in range(consts.MINE_COL):
            if game_filed[row][col+check] != '':
                return False
        return True
    elif object == consts.BUSH_NAME:
        for check_row in range(consts.BUSH_ROW):
            for check_col in range(consts.BUSH_COL):
                if game_filed[row+check_row][col+check_col].find(consts.BUSH_NAME) != -1 or game_filed[row+check_row][col+check_col] == consts.FLAG_NAME:
                    return False
        return True

    return False

def check_col(start_col):
    for col in range(start_col,consts.MINE_COL):
        mine_in_col = 0
        for row in range(consts.BOARD_ROWS):
            if game_filed[row][col] == consts.MINE_NAME:
                mine_in_col += 1

        if mine_in_col == consts.BUSH_ROW:
            return False
    return True

def not_in_spawn(mine_row, mine_col):
    for row in range(0, 6):
        for col in range(0, 4):
            if mine_row == row and mine_col == col:
                return False
    return True

def not_in_flag(mine_row, mine_col):
    for row in range(flag_row, consts.BOARD_ROWS):
        for col in range(flag_col, consts.BOARD_COLS):
            if row == mine_row and col == mine_col:
                return False
    return True

def get_game_filed():
    return game_filed