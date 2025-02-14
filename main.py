import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS
)
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        # player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            player_did_collide = asteroid.collision_check(player)

            for shot in shots:
                shot_did_collide = asteroid.collision_check(shot)

                if shot_did_collide:
                    asteroid.split()
                    shot.kill()

            if player_did_collide:
                print("Game over!")
                game_active = False

        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
