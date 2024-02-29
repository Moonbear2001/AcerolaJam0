import pygame
import math

from game_object import GameObject
from constants import *
from my_math import *


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
        
        self.input = {"a": False, "s": False, "d": False, "q": False, "w": False, "e": False}
        self.target = (WIDTH // 2, HEIGHT // 2)

        # TODO: VARIABLE?
        self.auto_range = 100
        self.move_speed = 3

    def event_loop(self, events) -> None:
        """
        Track input.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT_CLICK:
                self.mouse_clicks[event.pos] = self.linger_time
                self.target = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.input["a"] = True
                if event.key == pygame.K_s:
                    self.input["s"] = True
                if event.key == pygame.K_d:
                    self.input["d"] = True
                if event.key == pygame.K_q:
                    self.input["q"] = True
                if event.key == pygame.K_w:
                    self.input["w"] = True
                if event.key == pygame.K_e:
                    self.input["e"] = True
        
        if pygame.key.get_pressed()[pygame.K_a]:
            self.input["a"] = True


    def update(self) -> None:
        """
        Update.
        """
        # Update mouse clicks
        for click_pos, time in list(self.mouse_clicks.items()):
            self.mouse_clicks[click_pos] -= 1
            if self.mouse_clicks[click_pos] == 0:
                del self.mouse_clicks[click_pos]

        # Call abilities
        if self.input["q"]:
            self.q()
        if self.input["w"]:
            self.w()
        if self.input["e"]:
            self.e()
        if self.input["s"]:
            self.s()
        if self.input["d"]:
            self.d()
            
        # Move toward target click
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
        self.input = {"a": False, "s": False, "d": False, "q": False, "w": False, "e": False}

    
    def q(self) -> None:
        """
        Draw auto range.
        """
        print("q")

    def w(self) -> None:
        """
        Use w ability.
        """
        print("w")

    def e(self) -> None:
        """
        Use e ability.
        """
        print("e")

    def a(self, screen) -> None:
        """
        Draw auto range.
        """
        pygame.draw.circle(screen, BLUE, self.rect.center, self.auto_range, 2)

    def s(self) -> None:
        """
        Stop movement.
        """
        self.target = self.rect.center

    def d(self) -> None:
        """
        Flash.
        """
        # Get mouse position and direction towards flash
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        flash_unit_vector = pygame.math.Vector2(dx / distance, dy / distance)
        if distance < FLASH_DIST:
            self.rect.center = (mouse_x, mouse_y)
        else:
            self.rect.x += flash_unit_vector.x * FLASH_DIST
            self.rect.y += flash_unit_vector.y * FLASH_DIST

        # Reset movement if flash is away from previously desired direction
        target_vector = vector_between_points(self.rect.center, self.target)
        if angle_between(target_vector, (flash_unit_vector.x, flash_unit_vector.y)) > 90:
            self.target = self.rect.center

            
    