import pygame
import math

from constants import *

class Ability(pygame.sprite.Sprite):
    """
    Geometric shape correspond to an ability that orbits around a champion.
    Has the ability to evolve.
    """

    shapes = ["circle", "square", "triangle"]

    def __init__(self, orbit_center, radius, speed, shape, color):
        """
        Make new instance.
        """
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.radius = radius
        self.angle = 0
        self.speed = speed
        self.orbit_center = orbit_center
        self.color = color

        # Determine correct shape
        if shape == "square":
            self.image.fill(self.color)
        elif shape == "circle":
            pygame.draw.circle(self.image, self.color, self.rect.center, self.rect.width//2)



    def update(self, center):
        """
        Math go brrr.
        """
        self.orbit_center = center
        self.angle += self.speed
        self.rect.centerx = self.orbit_center[0] + self.radius * math.cos(math.radians(self.angle))
        self.rect.centery = self.orbit_center[1] + self.radius * math.sin(math.radians(self.angle))
