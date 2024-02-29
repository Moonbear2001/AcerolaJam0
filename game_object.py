import pygame

class GameObject(pygame.sprite.Sprite):
    """
    A sprite with the ability to handle events. Makes for a flexible general
    purpose game object.
    """

    def __init__(self) -> None:
        super().__init__()

    def event_loop(events) -> None:
        pass

    