# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


# Write a main function that simply prints "Starting asteroids!" (use this exact text).
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    
   

if __name__ == "__main__":
    main()
