import pygame

from .state import State
from .pause import Pause
from constants import *
from champion import Champion

class Gameplay(State):
    """
    Create a new Gameplay state.
    """
    
    def __init__(self, game):
        """
        Create a new Gameplay state.
        """
        super().__init__(game)

        self.map = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.game_objects.add(Champion(self.map, (255, 255, 255), 100, 100))

        self.camera_offset = pygame.math.Vector2(0, 0)
        self.camera_speed = 5


    def event_loop(self, events):
        """
        Handle list of passed-in events.
        """
        # super().event_loop(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.enter_state(Pause(self.game))
                break
        
        for champion in self.game_objects:
            champion.event_loop(events, self.camera_offset)

    def update(self):
        """
        Update per frame.
        """
        # Move the camera
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x == WIDTH - 1:
            self.camera_offset.x += self.camera_speed
        elif  mouse_x == 0:
            self.camera_offset.x -= self.camera_speed
        if mouse_y == HEIGHT - 1:
            self.camera_offset.y += self.camera_speed
        elif mouse_y == 0:
            self.camera_offset.y -= self.camera_speed

        # Ensure camera does not go out of bounds
        self.camera_offset.x = max(0, min(self.camera_offset.x, MAP_WIDTH - WIDTH))
        self.camera_offset.y = max(0, min(self.camera_offset.y, MAP_HEIGHT - HEIGHT))

        # Update champions
        # for champion in self.game_objects:
        #     champion.update()
        self.game_objects.update(self.camera_offset)

        # super().update()

    def draw(self):
        """
        Draw the frame.
        """
        self.map.fill(pygame.Color(255, 255, 255))
        for champion in self.game_objects:
            champion.draw()
        # self.game_objects.draw(self.screen)
            
        # Draw enemies
        pygame.draw.rect(self.map, RED, (100, 100, 50, 50))
        pygame.draw.rect(self.map, RED, (1000, 100, 50, 50))
        pygame.draw.rect(self.map, RED, (100, 1000, 50, 50))
        pygame.draw.rect(self.map, RED, (500, 500, 50, 50))
        pygame.draw.rect(self.map, RED, (2000, 1000, 50, 50))
        pygame.draw.rect(self.map, RED, (2100, 1300, 50, 50))

        self.screen.blit(self.map, (0, 0), pygame.Rect(self.camera_offset, (WIDTH, HEIGHT)))
        # super().draw()