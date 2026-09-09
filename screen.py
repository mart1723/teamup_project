import pygame
import time

from pygame import surface

import consts
import game_filed


def create_text(surface):
    my_font = pygame.font.SysFont(None, 20)
    text_surface = my_font.render('Welcome to The Flag game. \n have fun!', False, (255, 255, 255))
    surface.blit(text_surface, (80,0))


def create_bush(surface,x, y):
    bush_raw = pygame.image.load("grass.png")
    bush = pygame.transform.scale(bush_raw, (consts.CELL_SIZE * consts.BUSH_COL, consts.CELL_SIZE * consts.BUSH_ROW))
    return surface.blit(bush,(y*consts.CELL_SIZE,x*consts.CELL_SIZE))

def insert_bushes(surface,bush_list):
    for i in range(len(bush_list)):
        create_bush(surface,bush_list[i][0],bush_list[i][1])


def create_soldier(surface,x, y):
    soldier_raw = pygame.image.load("soldier.png")
    soldier = pygame.transform.scale(soldier_raw, (consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier,(x,y))


def create_flag(surface,x, y):
    flag_raw = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag_raw, (consts.CELL_SIZE * consts.FLAG_COLS, consts.CELL_SIZE * consts.FLAG_ROWS))
    return surface.blit(flag,(x,y))

def drawGrid(night_surface,color):
    blockSize = consts.CELL_SIZE #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(night_surface, color, rect, 1)

def create_soldier_night(surface,x, y):
    night_soldier_raw = pygame.image.load("soldier_night.png")
    soldier = pygame.transform.scale(night_soldier_raw,(consts.CELL_SIZE * consts.SOLDIER_COLS*2, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    return surface.blit(soldier, (x, y))


def create_mine(surface,x, y):
    mine_raw = pygame.image.load("mine.png")
    mine  = pygame.transform.scale(mine_raw, (consts.CELL_SIZE * consts.MINE_COL, consts.CELL_SIZE * consts.MINE_ROW))
    return surface.blit(mine,(y*consts.CELL_SIZE,x*consts.CELL_SIZE))

def insert_mines(surface,mine_list):
    for i in range(len(mine_list)):
        create_mine(surface,mine_list[i][0],mine_list[i][1])





def create_day_screen(soldier,bush_map):
    surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    surface.fill(consts.DARK_GREEN)
    pygame.display.set_caption("flag game")
    draw = draw_day_screen(soldier,bush_map)
    return draw


def draw_day_screen(soldier,bush_map):
    surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    surface.fill(consts.DARK_GREEN)

    game_filed.create_game_filed()
    insert_bushes(surface,bush_map)
    create_flag(surface,game_filed.flag_col*consts.CELL_SIZE, game_filed.flag_row*consts.CELL_SIZE)
    create_soldier(surface,soldier["first_col"]*consts.CELL_SIZE, soldier["top_row"]*consts.CELL_SIZE)
    create_text(surface)
    pygame.display.flip()


def create_night_screen(soldier,mine_map, bush_map):
    #night screen
    # Initializing Pygame modules
    pygame.init()

    # Initializing surface
    night_surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("flag game")
    #draw = draw_night_screen(soldier,mine_map, bush_map)

    #return draw



def draw_night_screen(soldier,mine_map,bush_map):
    night_surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    # Initializing RGB Color
    color = (0, 0, 0)
    night_surface.fill(color)

    drawGrid(night_surface, consts.DARK_GREEN)
    create_soldier_night(night_surface, soldier["first_col"] * consts.CELL_SIZE, soldier["top_row"] * consts.CELL_SIZE)
    game_filed.create_game_filed()
    insert_mines(night_surface, mine_map)

    pygame.display.flip()
    time.sleep(1)
    create_day_screen(soldier,bush_map)




def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    return surface.blit(text_img, location)

