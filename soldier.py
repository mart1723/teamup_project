#פרוייקט זוגות מרטין ומאיה
#מרטין:330851031 מאיה:217214162
def create_soldier():
    return{
        "top_row": 0,
        "first_col": 0
    }

def touch_flag(soldier, flag_cord):
    soldier_row = soldier['top_row']
    soldier_col = soldier['first_col']
    for row in range(3):
        for col in range(2):
            if (soldier_row + row,soldier_col + col) in flag_cord:
                return True
    return False

def touch_mine(soldier, mine_map):
    leg_row = soldier['top_row'] + 3
    leg_cols = soldier['first_col']
    for col in range(2):
        if (leg_row, leg_cols + col) in mine_map:
            return True
    return False