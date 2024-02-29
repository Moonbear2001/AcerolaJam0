import pygame
import time


class Game:
    """
    Main game class, manages:
    - game loop
    - delta time
    """

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


    def start(self) -> None:
        """
        On startup.
        """
        pass

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
        Handle and then propogate events.
        """
        for event in pygame.event.get():
            
            # Quit game
            if event.type == pygame.QUIT:
                print("quit")

    def update(self) -> None:
        """
        Logic per frame.
        """
        pass


    def draw(self) -> None:
        """
        Draw game objects to the screen.
        """
        self.screen.fill((255, 255, 255))

    def quit_game() -> None:
        """
        Quit the game, cleanup.
        """
        pygame.quit()
        exit()

            


