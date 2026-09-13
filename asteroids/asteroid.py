import pygame
import random

from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a1_mov = self.velocity.rotate(angle)
        a2_mov = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position.x, self.position.y, new_rad)
        aster2 = Asteroid(self.position.x, self.position.y, new_rad)
        aster1.velocity = a1_mov * 1.2
        aster2.velocity = a2_mov * 1.2
