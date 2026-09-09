
import pygame
import game_filed
import consts
import soldier

pygame.init()
is_running = True
sol = soldier.create_soldier()

game_filed.create_game_filed()
flag_cords = game_filed.create_flag()
game_filed.put_soldier(sol)
mine_map = game_filed.scatter_mines()
game_filed.scatter_bushes()
matrix = game_filed.get_game_filed()
for row in range(len(matrix)):
    print(matrix[row])

row_count = 3
col_count = 1

while is_running:
    if row_count < consts.BOARD_ROWS:
        soldier.move_down(sol)
        row_count += 1

    if col_count < consts.BOARD_COLS:
        soldier.move_right(sol)
        col_count += 1

    print("--------------------------------------------------------------------")
    for row in range(len(matrix)):
        print(matrix[row])

    if soldier.touch_mine(sol, mine_map):
        print("Mine")
        is_running = False
    if soldier.touch_flag(sol, flag_cords):
        print("Flag")
        is_running = False



"""
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Move up")
            elif event.key == pygame.K_DOWN:
                print("Move down")
            elif event.key == pygame.K_LEFT:
                print("Move left")
            elif event.key == pygame.K_RIGHT:
                print("Move right")
            elif event.key == pygame.K_KP_ENTER:
                print("Enter")
"""

