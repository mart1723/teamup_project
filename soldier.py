#פרוייקט זוגות מרטין ומאיה
#מרטין:330851031 מאיה:217214162

import consts

#פונקציה היוצרת חייל:
#top_row- שומרת את השורה העליונה של החייל
#first_col- שומרת את התור השמאלי של החייל
def create_soldier():
    return{
        "top_row": 0,
        "first_col": 0
    }

#פונקציה הבודקת האם גוף החייל נוגע בדגל
#אם כן מחזירה אמת אם לא שקר
def touch_flag(soldier, flag_cord):
    soldier_row = soldier['top_row']
    soldier_col = soldier['first_col']
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if (soldier_row + row,soldier_col + col) in flag_cord:
                return True
    return False

#פונקציה הבודקת האם חייל דרך על מוקש עם הרגליים
#אם כן מחזירה אמת אם לא שקר
def touch_mine(soldier, mine_map):
    leg_row = soldier['top_row'] + 3
    leg_cols = soldier['first_col']
    for col in range(consts.SOLDIER_COLS):
        if (leg_row, leg_cols + col) in mine_map:
            return True
    return False