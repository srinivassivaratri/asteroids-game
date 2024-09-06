# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


# Write a main function that simply prints "Starting asteroids!" (use this exact text).
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # calling the update method before rendering.
        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
  
        #limiting framerate to 60 frames per second(fps)
        dt = clock.tick(60) / 1000
    
    

    
    
   

if __name__ == "__main__":
    main()
