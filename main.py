import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialise delta time and clock for a smooth 60 fps
    dt = 0
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Keep game at 60 FPS


if __name__ == "__main__":
    main()
