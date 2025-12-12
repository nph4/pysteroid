import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT /2

    ship = player.Player(x, y)
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        ship.draw(screen)
        
        pygame.display.flip()

        #limit the framerate to 60fps
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
