#פרוייקט זוגות מרטין ומאיה
#מרטין:330851031 מאיה:217214162
import consts
import random
from consts import BOARD_ROWS
from consts import BOARD_COLS

game_filed = []
flag_row = BOARD_ROWS - consts.FLAG_ROWS
flag_col = BOARD_COLS - consts.FLAG_COLS

#פונקציה המאתחלת את כל המשתנים שנמצאים במודל
def first_creat(soldier):
    create_game_filed()
    flag_cord =create_flag()
    put_soldier(soldier)
    mine_map = scatter_mines()
    bush_map = scatter_bushes()
    return (flag_cord, mine_map, bush_map)

#פורנציה היוצרת לוח משחק
def create_game_filed():
    global game_filed
    for row in range(BOARD_ROWS):
        game_filed.append([])
        for col in range(BOARD_COLS):
            game_filed[row].append('')

#פונקציה היוצרת דגל וממקמת אותו
#הפונקציה מחזירה את מיקום הדגל כטופל
def create_flag():
    flag_cord = []
    for row in range(flag_row, BOARD_ROWS):
        for col in range(flag_col, BOARD_COLS):
            game_filed[row][col] = consts.FLAG_NAME
            flag_cord.append((row, col))
    return flag_cord

#פונרציה היוצרת ומפזרת את המוקשים ברחבי הלוח
#הפונקציה מחזירה ליסט ען מיקומי המוקשים כטופל
def scatter_mines():
    mines_scattered = 0
    mine_map = []
    while mines_scattered < consts.MINE_COUNT:
        rnd_row = random.randrange(0, BOARD_ROWS)
        start_col = random.randrange(0, BOARD_COLS-2)
        if (check_space(rnd_row, start_col, consts.MINE_NAME) and check_col(start_col) and
                not_in_spawn(rnd_row, start_col) and not_in_flag(rnd_row, start_col)):
            for check in range(consts.MINE_COL):
                game_filed[rnd_row][start_col + check] = consts.MINE_NAME
            mines_scattered += 1
            mine_map.append((rnd_row, start_col))
    return mine_map

#פונקציה המפזרת את השיחים ברכבי הלוח
#הונקציפה מחזירה רשימה עם מיקומי השיחים כטופל
def scatter_bushes():
    bushes_scattered = 0
    bushes_map = []
    while bushes_scattered < consts.BUSH_COUNT:
        start_row = random.randrange(0, BOARD_ROWS-1)
        start_col = random.randrange(0, BOARD_COLS-1)
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


#פוקציה בדיקה האם ניתן להניח אובייקט במיקום הרנדומלי שהתקבל
#הפונקציה מקבלת את שם האובייקט וקורינטה ובודקת פר אובייקט האם ניתן למקם
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

#פונקציה הבודקת האם התור שבו יהיה מוקש יחסם ממוקשים
#אם כן תחזיר שקר
def check_col(start_col):
    for col in range(start_col,consts.MINE_COL):
        mine_in_col = 0
        for row in range(BOARD_ROWS):
            if game_filed[row][col] == consts.MINE_NAME:
                mine_in_col += 1

        if mine_in_col == consts.BOARD_ROWS:
            return False
    return True

#פונקציה הבודקת האם המוקש נמצא באזור ההתלתי של החייל
#אם כן תחזיר שקר
def not_in_spawn(mine_row, mine_col):
    for row in range(0, 6):
        for col in range(0, 4):
            if mine_row == row and mine_col == col:
                return False
    return True

#פונרציה הבודקת האם המוקש נמצא בשטח הדגל
#אם כן תחזיר שקר
def not_in_flag(mine_row, mine_col):
    for row in range(flag_row, BOARD_ROWS):
        for col in range(flag_col, BOARD_COLS):
            if row == mine_row and col == mine_col:
                return False
    return True

# פונקציה המזיזה את החייל, מקבלת חייל ואת הכיוון אליו הוא רוצה ללכת
#מחזירה אמת אם החייל זז ושקר אם לא
def move_soldier(soldier, direction):
    soldier_row = soldier['top_row']
    soldier_col = soldier['first_col']
    remove_soldier_from_filed(soldier_row, soldier_col)
    if direction == "up" and soldier['top_row'] - 1 > 0:
        soldier['top_row'] -= 1
        put_soldier(soldier)
        return True
    elif direction == "down" and soldier['top_row'] + consts.SOLDIER_ROWS < BOARD_ROWS:
        soldier['top_row'] += 1
        put_soldier(soldier)
        return True
    elif direction == "left" and soldier['first_col'] - 1 > 0:
        soldier['first_col'] -= 1
        put_soldier(soldier)
        return True
    elif direction == "right" and soldier['first_col'] + consts.SOLDIER_COLS + 1 < consts.BOARD_COLS:
        soldier['first_col'] += 1
        put_soldier(soldier)
        return True
    return False

#מכניסה את החייל ללוח לפי נקודת הראש השמאלית שלו
def put_soldier(soldier):
    soldier_row = soldier['top_row']
    soldier_col = soldier['first_col']
    for row in range(soldier_row, soldier_row + consts.SOLDIER_ROWS):
        for col in range(soldier_col, soldier_col + consts.SOLDIER_COLS):
            if game_filed[row][col] == '':
                game_filed[row][col] = consts.SOLDIER_NAME
            else:
                game_filed[row][col] += '_' + consts.SOLDIER_NAME

#מוחקת את החייל מהלוח
def remove_soldier_from_filed(soldier_row, soldier_col):
    for row in range(soldier_row, soldier_row + consts.SOLDIER_ROWS):
        for col in range(soldier_col, soldier_col + consts.SOLDIER_COLS):
            if game_filed[row][col] == consts.SOLDIER_NAME:
                game_filed[row][col] = ''
            else:
                words = game_filed[row][col].split('_')
                if words[0] == consts.SOLDIER_NAME:
                    words.pop(0)
                game_filed[row][col] = words[0]

