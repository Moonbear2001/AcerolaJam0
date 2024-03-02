import pygame

from constants import *

class State:
    """
    A game state (menu, gameplay, etc.).
    State is changed in the frame AFTER enter_state() is called.
    """
    
    def __init__(self, game) -> None:
        """
        Create a new state.
        """
        self.game = game
        self.stack = game.state_stack
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        self.game_objects = pygame.sprite.Group()

    def event_loop(self, events) -> None:
        """
        Handle list of passed-in events.
        """
        for go in self.game_objects:
            go.event_loop(events)

    def update(self) -> None:
        """
        Update per frame.
        """
        self.game_objects.update()

    def draw(self) -> None:
        """
        Draw the frame.
        """
        for go in self.game_objects:
            go.draw()

    def enter_state(self, state) -> None:
        """
        Enter a new state.
        """
        self.stack.append(state)

    def exit_state(self) -> None:
        """
        Exit the current state.
        """
        if len(self.stack) == 1:
            return
        self.stack.pop()

