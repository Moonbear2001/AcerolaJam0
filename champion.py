import pygame
import math

from game_object import GameObject
from constants import *


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
        
        self.input = {"a": False, "s": False, "d": False}
        self.target = (WIDTH // 2, HEIGHT // 2)

        # TODO: VARIABLE?
        self.auto_range = 100
        self.move_speed = 3

    def event_loop(self, events) -> None:
        """
        Track input.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_clicks[event.pos] = self.linger_time
                self.target = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.input["a"] = True
                if event.key == pygame.K_s:
                    self.input["s"] = True
                if event.key == pygame.K_d:
                    self.input["d"] = True
        
        if pygame.key.get_pressed()[pygame.K_a]:
            self.input["a"] = True


    def update(self) -> None:
        """
        Update mouse clicks.
        """
        for click_pos, time in list(self.mouse_clicks.items()):
            self.mouse_clicks[click_pos] -= 1
            if self.mouse_clicks[click_pos] == 0:
                del self.mouse_clicks[click_pos]

        # Call abilities
        if self.input["s"]:
            self.s()
        if self.input["d"]:
            self.d()

        # Move toward click
        distance = math.sqrt((self.target[0] - self.rect.centerx)**2 + (self.target[1] - self.rect.centery)**2)
        if distance >= self.move_speed:
            direction_x = (self.target[0] - self.rect.centerx) / distance
            direction_y = (self.target[1] - self.rect.centery) / distance
            self.rect.x += direction_x * self.move_speed
            self.rect.y += direction_y * self.move_speed
        else:
            self.rect.center = self.target

    
    def draw(self, screen) -> None:
        """
        Draw mouse clicks.
        """
        for click_pos, time in self.mouse_clicks.items():
            pygame.draw.circle(screen, BLUE, click_pos, int(10 * (time/self.linger_time)))

        pygame.draw.circle(screen, BLUE, self.rect.center, 10)

        # Draw auto range
        if self.input["a"]:
            self.a(screen)

        # RESET
        self.input = {"a": False, "s": False, "d": False}
        

    def a(self, screen) -> None:
        """
        Draw auto range.
        """
        pygame.draw.circle(screen, BLUE, self.rect.center, self.auto_range, 2)

    def s(self) -> None:
        """
        Use ability 1.
        """
        print("s")

    def d(self) -> None:
        """
        Use ability 2.
        """
        print("d")
    