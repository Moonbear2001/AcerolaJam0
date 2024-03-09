import pygame

from .state import State
from constants import *


class Intro(State):
    """
    The game's intro screen.
    """

    delay = 2 * FPS
    
    def __init__(self, game):
        """
        Create a new Intro state.
        """
        super().__init__(game)
        self.alpha_surface = pygame.Surface((WIDTH, HEIGHT))
        self.alpha_surface.fill(BLACK)
        # self.alpha_surface.set_alpha(1)

        self.fade_in = False
        self.fade_out = False


    def event_loop(self, events):
        """
        Event loop.
        """
        for event in events:
            if event.type == pygame.K_RETURN:
                print("enter event")
                # self.exit_state()
                self.fade_in = True
                break

    def update(self):
        """
        Update per frame.
        """
        if self.fade_in:
            if self.alpha_surface.get_alpha() <= 0:
                self.fade_in = False
            else:
                print("fading in ")
                self.alpha_surface.set_alpha(self.alpha_surface.get_alpha() - 1)
        elif self.fade_out:
            if self.alpha_surface.get_alpha() >= 255:
                self.fade_out = False
            else:
                self.alpha_surface.set_alpha(self.alpha_surface.get_alpha() + 1)

    def draw(self):
        """
        Draw the frame.
        """
        self.screen.fill("white")
        self.screen.blit(self.alpha_surface, (0, 0))

    # def fade_in(self, duration):
    #     """
    #     Fade in from black effect.
    #     """
    #     for alpha in range(255, 0, -5):
    #         self.alpha_surface.set_alpha(alpha)
    #         self.screen.blit(self.alpha_surface, (0, 0))

    # def fade_out(self, duration):
    #     """
    #     Fade out to black effect.
    #     """
    #     for alpha in range(0, 255, 5):
    #         self.alpha_surface.set_alpha(alpha)
    #         self.screen.blit(self.alpha_surface, (0, 0))
    #         pygame.display.flip()
    #         pygame.time.delay(duration // 51)  # Control fade-out speed
    #         self.screen.fill(WHITE)
        
    