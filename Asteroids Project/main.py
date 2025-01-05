# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *





def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("Asteroids Game")

    running = True
    while running:
        screen.fill((0, 0, 0))
        
        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        pygame.display.flip()
main()
