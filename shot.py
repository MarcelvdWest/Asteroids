import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def draw(self, screen):
        # print("draw")
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            SHOT_RADIUS,
            2
        )

    def update(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SHOOT_SPEED
