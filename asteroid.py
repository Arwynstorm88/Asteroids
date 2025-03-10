import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        cw_vector = self.velocity.rotate(random_angle)
        ccw_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid1.velocity = cw_vector * 1.2
        asteroid2 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid2.velocity = ccw_vector * 1.2
        return asteroid1, asteroid2