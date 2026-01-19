from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_angle1 = self.velocity.rotate(angle)
            new_angle2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(*self.position, new_radius)
            new_asteroid2 = Asteroid(*self.position, new_radius)
            new_asteroid1.velocity = new_angle1
            new_asteroid2.velocity = new_angle2
