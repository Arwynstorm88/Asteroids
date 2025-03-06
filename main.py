import pygame
import sys
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()