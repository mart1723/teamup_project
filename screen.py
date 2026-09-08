# Importing the library
import pygame
import timer
# Initializing Pygame modules
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing RGB Color
color = (0, 255, 0)

# Changing surface color
surface.fill(color)
timer.get_timer(5)
pygame.display.flip()







