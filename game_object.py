import pygame

class GameObject(pygame.sprite.Sprite):
    """
    A sprite with the ability to handle events and hold other game objects.
    
    """

    def __init__(self, screen) -> None:
        super().__init__()
        self.screen = screen

    def event_loop(self, events) -> None:
        pass

    