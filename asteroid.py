import random
from typing import override

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        log_event("asteroid_split")
        split_vector_1 = self.velocity.rotate(random.uniform(20,50))
        split_vector_2 = self.velocity.rotate(random.uniform(20,50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        split_asteroid1 = Asteroid(x,y,new_radius)
        split_asteroid2 = Asteroid(x,y,new_radius)
        split_asteroid1.velocity = split_vector_1 * 1.2
        split_asteroid2.velocity = split_vector_2 * 1.2
