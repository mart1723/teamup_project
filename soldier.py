
import consts
from game_filed import move_soldier

def create_soldier():
    return{
        "top_row": 0,
        "first_col": 0
    }


def move_up(soldier):
    if soldier['top_row'] - 1 >= 0:
        soldier = move_soldier(soldier, "up")
        return True
    return False

def move_down(soldier):
    if soldier['top_row']+3 + 1 <= consts.BOARD_ROWS:
        soldier = move_soldier(soldier, "down")
        return True
    return False

def move_left(soldier):
    if soldier['top_col'] - 1 >= 0:
        soldier = move_soldier(soldier, "left")
        return True
    return False

def move_right(soldier):
    if soldier['top_col']+1 + 1 <= consts.BOARD_COLS:
        soldier = move_soldier(soldier, "right")
        return True
    return False

def touch_flag(soldier, flag_cord):
    soldier_row = soldier['top_row']
    soldier_col = soldier['top_col']
    for row in range(3):
        for col in range(2):
            if (soldier_row + row,soldier_col + col) in flag_cord:
                return True
    return False

def touch_mine(soldier, mine_map):
    leg_row = soldier['top_row'] + 3
    leg_cols = (soldier['first_col'], soldier['top_col']+1)
    for mine in mine_map:
        (mine_row, mine_first_col) = mine
        for leg_num in range(2):
            for col in range(consts.MINE_COL):
                if (leg_row == mine_row and
                        leg_cols+leg_num == mine_first_col+col):
                    return True
    return False
