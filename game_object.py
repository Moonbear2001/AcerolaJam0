import pygame

class GameObject(pygame.sprite.Sprite):
    """
    A extended Sprite with the ability to handle events and hold other game objects.
    """

    def __init__(self, state, screen) -> None:
        super().__init__()
        self.state = state
        self.screen = screen

    def event_loop(self, events) -> None:
        pass

    