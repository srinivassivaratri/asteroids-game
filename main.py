# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


# Write a main function that simply prints "Starting asteroids!" (use this exact text).
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

        #limiting framerate to 60 frames per second(fps)
        dt = clock.tick(60) / 1000
    
   

if __name__ == "__main__":
    main()
