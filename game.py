import pygame
import time

from game_object import GameObject
from champion import Champion


class Game:
    """
    Main game class, manages:
    - game loop
    - delta time
    """

    name = "tbd"
    width = 1280
    height = 720
    fps = 60

    def __init__(self) -> None:
        """
        Make new instance of Game.
        """
        pygame.init()
        self.run = True
        self.delta_time = 0.0
        self.prev_time = 0.0
        self.screen = pygame.display.set_mode((Game.width, Game.height))

        # Block irrelevant events
        # pygame.event.set_blocked()
        # pygame.event.set_allowed()

        # Grab input
        pygame.event.set_grab(False)

        self.champions = pygame.sprite.Group()
        self.champions.add(Champion((255, 255, 255), 100, 100))

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
            clock.tick(Game.fps)

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
        for event in pygame.event.get():
            
            # Quit game
            if event.type == pygame.QUIT:
                self.quit_game()

        for champion in self.champions:
            champion.event_loop()


    def update(self) -> None:
        """
        Logic per frame.
        """
        for champion in self.champions:
            champion.update()


    def draw(self) -> None:
        """
        Draw game objects to the screen.
        """
        self.screen.fill(pygame.Color(255, 255, 255))
        for champion in self.champions:
            champion.draw(self.screen)

    def quit_game(self) -> None:
        """
        Quit the game, cleanup.
        """
        pygame.quit()
        exit()

            


