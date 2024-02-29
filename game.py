import pygame
import time

from constants import *
from game_object import GameObject
from champion import Champion


class Game:
    """
    Main game class, manages:
    - game loop
    - delta time
    """

    name = "tbd"

    def __init__(self) -> None:
        """
        Make new instance of Game.
        """
        pygame.init()
        self.run = True
        self.delta_time = 0.0
        self.prev_time = 0.0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Acerola Jam 0")

        # Block irrelevant events
        # pygame.event.set_blocked()
        # pygame.event.set_allowed()

        # Grab input
        pygame.event.set_grab(True)

        # Key repeat
        pygame.key.set_repeat(1000)

        self.champions = pygame.sprite.Group()
        self.champions.add(Champion((255, 255, 255), 100, 100))

        self.camera_offset = pygame.math.Vector2(0, 0)
        self.map = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.camera_speed = 5

    def print_startup_info(self) -> None:
        """
        Prints some info on startup.
        """
        # print(f"Blocked events: {pygame.event.get_blocked(pygame.QUIT)}")
        print(f"Inputs are grabbed for this game? {pygame.event.get_grab()}")

    def start(self) -> None:
        """
        On startup. Calls the game loop.
        """
        self.print_startup_info()
        self.game_loop()

    def game_loop(self) -> None:
        """
        Main game loop.
        """
        clock = pygame.time.Clock()
        self.prev_time = time.time()

        while self.run:

            # --- Delta time logic --- #
            self.get_delta_time()

            # --- Event Loop --- #
            self.event_loop()

            # --- Game logic --- #
            self.update()

            # --- Drawing to screen --- #
            self.draw()
            pygame.display.flip()

            # --- Limit frame rate --- #
            clock.tick(FPS)

        self.quit_game()


    def get_delta_time(self) -> None:
        """
        Manage delta time.
        """
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    
    def event_loop(self) -> None:
        """
        Handle global events and propogate events.
        """
        events = pygame.event.get()
        for event in events:

            # Quit game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.quit_game()
            
        for champion in self.champions:
            champion.event_loop(events, self.camera_offset)


    def update(self) -> None:
        """
        Logic per frame.
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
        # for champion in self.champions:
        #     champion.update()
        self.champions.update(self.camera_offset)


    def draw(self) -> None:
        """
        Draw game objects to the screen.
        """
        self.map.fill(pygame.Color(255, 255, 255))
        for champion in self.champions:
            champion.draw(self.map)
        # self.champions.draw(self.screen)
            
        # Draw enemies
        pygame.draw.rect(self.map, RED, (100, 100, 50, 50))
        pygame.draw.rect(self.map, RED, (1000, 100, 50, 50))
        pygame.draw.rect(self.map, RED, (100, 1000, 50, 50))
        pygame.draw.rect(self.map, RED, (500, 500, 50, 50))
        pygame.draw.rect(self.map, RED, (2000, 1000, 50, 50))
        pygame.draw.rect(self.map, RED, (2100, 1300, 50, 50))

        self.screen.blit(self.map, (0, 0), pygame.Rect(self.camera_offset, (WIDTH, HEIGHT)))


    def quit_game(self) -> None:
        """
        Quit the game, cleanup.
        """
        pygame.quit()
        exit()

            


