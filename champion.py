import pygame

from game_object import GameObject
from colors import *

class Champion(GameObject):
    """
    Abstract champion class. 
    """

    def __init__(self, color, width, height):
        """
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.mouse_clicks = {}
        self.linger_time = 10

    def event_loop(self) -> None:
        """
        Track new mouse clicks.
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_clicks[event.pos] = self.linger_time

    def update(self) -> None:
        """
        Update mouse clicks.
        """
        for click_pos, time in list(self.mouse_clicks.items()):
            self.mouse_clicks[click_pos] -= 1
            if self.mouse_clicks[click_pos] == 0:
                del self.mouse_clicks[click_pos]
    
    def draw(self, screen) -> None:
        """
        Draw mouse clicks.
        """
        for click_pos, time in self.mouse_clicks.items():
            pygame.draw.circle(screen, WHITE, click_pos, int(10 * (time/self.linger_time)))

        pygame.draw.circle(screen, BLUE, self.rect.center, 10)
        pygame.draw.circle(screen, BLUE, self.rect.center, self.rect.width, 2)

    