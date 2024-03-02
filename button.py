import pygame

from game_object import GameObject
from constants import *

class Button(GameObject):
    """
    All purpose button class. 
    The args argument can be an array of a single value, just has to be dealt with 
    correctly in the function that is called on-click.
    """

    def __init__(self, state, screen, x, y, width, height, text, text_color=BLACK, font=None, function=None, args=None) -> None:
        """
        Create a new button.
        """
        super().__init__(state, screen)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = text
        self.text_color = text_color
        self.font = font
        self.function = function
        self.args = args

    def draw(self) -> None:
        """
        Draw to screen.
        """
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, (0, 0, 50, 50))
        self.screen.blit(self.image, self.rect)

    def event_loop(self, events) -> None:
        """
        Check if button got clicked.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK and self.rect.collidepoint(event.pos):
                if self.function and self.args:
                    self.function(self.args)



