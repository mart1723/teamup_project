# Importing the library
import pygame
import time
import consts
import game_filed

# Initializing Pygame modules
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.

pygame.display.set_caption("flag game")
# Initializing RGB Color
DARK_GREEN = (2, 89, 15)

# Changing surface color
surface.fill(DARK_GREEN)
my_font = pygame.font.SysFont('arial', 30)
text_surface = my_font.render('Welcome to The Flag game, have fun!', False, (255, 255, 255))
surface.blit(text_surface, (80,0))

def create_flag(x, y):
    flag_raw = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag_raw, (consts.CELL_SIZE * consts.FLAG_COLS, consts.CELL_SIZE * consts.FLAG_ROWS))
    return surface.blit(flag,(x,y))

create_flag(game_filed.flag_col*consts.CELL_SIZE, game_filed.flag_row*consts.CELL_SIZE)


def create_soldier(x, y):
    soldier_raw = pygame.image.load("soldier.png")
    soldier = pygame.transform.scale(soldier_raw, (consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier,(x,y))

create_soldier(0, 0)


def create_bush(x, y):
    bush_raw = pygame.image.load("grass.png")
    bush = pygame.transform.scale(bush_raw, (consts.CELL_SIZE * consts.BUSH_COL, consts.CELL_SIZE * consts.BUSH_ROW))
    return surface.blit(bush,(x,y))

def insert_bushes(bush_list):
    for i in range(len(bush_list)):
        create_bush(bush_list[i][0],bush_list[i][1])
#        print(bush_list[i][0],bush_list[i][1])

game_filed.create_game_filed()
insert_bushes(game_filed.scatter_bushes())
pygame.display.flip()
time.sleep(3)



# Initializing Pygame modules
pygame.init()

# Initializing surface
night_surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("flag game")
# Initializing RGB Color
color = (0, 0, 0)
night_surface.fill(color)


def drawGrid():
    blockSize = consts.CELL_SIZE #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(night_surface, DARK_GREEN, rect, 1)

drawGrid()

def create_soldier_night(x, y):
    night_soldier_raw = pygame.image.load("soldier_night.png")
    soldier = pygame.transform.scale(night_soldier_raw,(consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier, (x, y))
create_soldier_night(0, 0)


def create_mine(x, y):
    mine_raw = pygame.image.load("mine.png")
    mine  = pygame.transform.scale(mine_raw, (consts.CELL_SIZE * consts.MINE_COL, consts.CELL_SIZE * consts.MINE_ROW))
    return surface.blit(mine,(x,y))


pygame.display.flip()
time.sleep(3)
