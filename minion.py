import pygame

from game_object import GameObject
from constants import *


class Minion(GameObject):
    """
    Abstract minion class.
    """

    aa_cd = 3
    gold_value = 1

    width = 20
    height = 20

    def __init__(self, state, screen, color):
        """
        Make a new Champion.
        """
        super().__init__(state, screen)
        self.image = pygame.Surface([Minion.width, Minion.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # TEMP
        self.rect.center = (200, 200)

        self.target = (WIDTH // 2, HEIGHT // 2)

        # TODO: VARIABLE?
        # self.cds = {}
        self.auto_range = 15
        self.move_speed = 3

        self.camera_offset = pygame.math.Vector2()

        self.highlight = False


    def event_loop(self, events, camera_offset) -> None:
        """
        TODO: check for collisions?
        """
        pass


    def update(self, camera_offset) -> None:
        """
        Update.
        """
        # Update camera offset
        self.camera_offset = camera_offset

        # Check for highlight
        self.highlight = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.highlight:
            self.state.add_targeted(self)


        # # Update cooldowns
        # for cd in self.cds:
        #     if self.cds[cd] > 0:
        #         self.cds[cd] -= 1

    
    def draw(self) -> None:
        """
        Draw self.
        """
        pygame.draw.circle(self.screen, ORANGE, self.rect.center, Minion.width // 2)
        if self.highlight:
            pygame.draw.circle(self.screen, RED, self.rect.center, Minion.width // 2, 2)
            
    