import pygame
from constants import *





def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))    
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()
    framerate = 60

    running = True


# get rid of this later, this is for testing:
#    previous_time = pygame.time.get_ticks()


    while running:
# Testing Stuff        
# Calculate dt (time difference since the last frame)
        # current_time = pygame.time.get_ticks()
        # dt = (current_time - previous_time) / 1000.0  # Convert to seconds
        # previous_time = current_time  # Update previous_time for the next frame

        # # Optional: Print dt to see how much time has passed (testing)
        # print(f"Delta Time (dt): {dt:.4f} seconds")


# End of Testing Stuff

        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =  False
                return

        pygame.display.flip()

        clock.tick(framerate)

        
main()
