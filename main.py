
import pygame
import game_filed
import consts
import soldier

pygame.init()
is_running = True
sol = soldier.create_soldier()

game_filed.create_game_filed()
game_filed.create_flag()
game_filed.put_soldier(sol)
game_filed.scatter_mines()
game_filed.scatter_bushes()
matrix = game_filed.get_game_filed()
for row in range(len(matrix)):
    print(matrix[row])

soldier.move_down(sol)

print("-----------------------")
for row in range(len(matrix)):
    print(matrix[row])

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

