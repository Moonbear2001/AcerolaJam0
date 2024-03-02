import pygame

from .state import State
from constants import *


class Pause(State):
    """
    Pauses gameplay.
    """
    
    def __init__(self, game):
        """
        Create a new Title state.
        """
        super().__init__(game)

    def event_loop(self, events):
        """
        P unpauses.
        """
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.exit_state()
                break

    def update(self):
        """
        Update per frame.
        """
        pass

    def draw(self):
        """
        Draw the frame.
        """
        pygame.draw.rect(self.screen, BLACK, (0, 0, 100, 100))
        
    