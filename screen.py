#פרוייקט זוגות מרטין ומאיה
#מרטין:330851031 מאיה:217214162
import pygame
import time
import consts
import game_filed

surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("flag game")

# פונקציה שיוצרת את הטקסט של ברוכה הבאה למשחק, מתאימה את הגודל ומציירת על המסך
def create_text():
    my_font = pygame.font.SysFont(None, 20)
    text_surface = my_font.render('Welcome to The Flag game. \n have fun!', False, (255, 255, 255))
    surface.blit(text_surface, (80,0))

# פונקציה שיוצרת שיח, מתאימה את הגודל ומציירת אותו על המסך
def create_bush(x, y):
    bush_raw = pygame.image.load("bin\\grass.png")
    bush = pygame.transform.scale(bush_raw, (consts.CELL_SIZE * consts.BUSH_COL, consts.CELL_SIZE * consts.BUSH_ROW))
    return surface.blit(bush,(y*consts.CELL_SIZE,x*consts.CELL_SIZE))

# פונקציה שמקבלת רשימה של שיחים ומציירת את כל השיחים במיקומים הרנדומלים שלהם על המסך בעזרת הפונקציה create_bush
def insert_bushes(bush_list):
    for i in range(len(bush_list)):
        create_bush(bush_list[i][0],bush_list[i][1])

# פונקציה שיוצרת חייל, מתאימה את הגודל ומציירת אותו על המסך במיקום המתאים
def create_soldier(x, y):
    soldier_raw = pygame.image.load("bin\\soldier.png")
    soldier = pygame.transform.scale(soldier_raw, (consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier,(x,y))

# פונקציה שיוצרת דגל, מתאימה את הגודל ומציירת אותו על המסך במיקום המתאים
def create_flag(x, y):
    flag_raw = pygame.image.load("bin\\flag.png")
    flag = pygame.transform.scale(flag_raw, (consts.CELL_SIZE * consts.FLAG_COLS, consts.CELL_SIZE * consts.FLAG_ROWS))
    return surface.blit(flag,(x,y))

#פונקציה שמציירת את הגריד על המסך כאשר גודל של קוביה הוא תא אחד
def drawGrid(color):
    blockSize = consts.CELL_SIZE #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(surface, color, rect, 1)

# פונקציה שיוצרת חייל במצב "לילה", מתאימה את הגודל ומציירת אותו על המסך במיקום המתאים
def create_soldier_night(x, y):
    night_soldier_raw = pygame.image.load("bin\\soldier_night.png")
    soldier = pygame.transform.scale(night_soldier_raw,(consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier, (x, y))


# פונקציה שיוצרת מוקש, מתאימה את הגודל ומציירת אותו על המסך
def create_mine(x, y):
    mine_raw = pygame.image.load("bin\\mine.png")
    mine  = pygame.transform.scale(mine_raw, (consts.CELL_SIZE * consts.MINE_COL, consts.CELL_SIZE * consts.MINE_ROW))
    return surface.blit(mine,(y*consts.CELL_SIZE,x*consts.CELL_SIZE))


# פונקציה שמקבלת רשימה של מוקשים ומציירת את כל המוקשים במיקומים הרנדומלים שלהם על המסך בעזרת הפונקציה create_mine
def insert_mines(mine_list):
    for i in range(len(mine_list)):
        create_mine(mine_list[i][0],mine_list[i][1])


# פונקציה המציירת את המסך הרגיל ואת כל האלמנטים שלו בעזרת קריאה לפונקציות היצירה שלהן
def draw_day_screen(soldier, bush_map):
    surface.fill(consts.DARK_GREEN)
    insert_bushes(bush_map)
    create_flag(game_filed.flag_col * consts.CELL_SIZE, game_filed.flag_row * consts.CELL_SIZE)
    create_soldier(soldier["first_col"] * consts.CELL_SIZE, soldier["top_row"] * consts.CELL_SIZE)
    create_text()
    pygame.display.flip()


# פונקציה המציירת את המסך "לילה"(גריד) ואת כל האלמנטים שלו בעזרת קריאה לפונקציות היצירה שלהן
def draw_night_screen(soldier,mine_map,bush_map):
    # Initializing RGB Color
    color = (0, 0, 0)
    surface.fill(color)

    drawGrid(consts.DARK_GREEN)
    create_soldier_night(soldier["first_col"] * consts.CELL_SIZE, soldier["top_row"] * consts.CELL_SIZE)
    game_filed.create_game_filed()
    insert_mines(mine_map)

    pygame.display.flip()
    time.sleep(1)
    draw_day_screen(soldier, bush_map)

#פונקציה המציגה על המסך הודעת הפסד בעזרת קריאה לפונקציה של הצגת הודעה
def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    pygame.display.update()
    time.sleep(3)

#פונקציה המציגה על המסך הודעת ניצחון בעזרת קריאה לפונקציה של הצגת הודעה
def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.update()
    time.sleep(3)

# פונקציה המציגה את ההודעה המתבקשת על המסך
def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    return surface.blit(text_img, location)
