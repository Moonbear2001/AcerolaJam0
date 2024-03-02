import pygame

from .state import State
from .gameplay import Gameplay
from button import Button
from constants import *


class Title(State):
    """
    A game state (menu, gameplay, etc.).
    """
    
    def __init__(self, game, title):
        """
        Create a new Title state.
        """
        super().__init__(game)
        self.title = title

        # Start game button
        sbsize = game.fonts["KgHoloceneRegular"].size("Start Game")
        start_button = Button(self.screen, 0, 0, sbsize[0], sbsize[1], "Start Game", font=game.fonts["KgHoloceneRegular"], function=self.enter_state, args=Gameplay(game))
        start_button.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.game_objects.add(start_button)
        

    def event_loop(self, events):
        """
        Handle list of passed-in events.
        """
        super().event_loop(events)

    def update(self):
        """
        Update per frame.
        """
        super().update()

    def draw(self):
        """
        Draw the frame.
        """
        self.screen.fill(LIGHT_GRAY)
        super().draw()