import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game Over!")
                sys.exit()


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Keep game at 60 FPS


if __name__ == "__main__":
    main()
