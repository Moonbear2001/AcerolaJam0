import pygame
import time
import os

from constants import *
from game_object import GameObject
from champion import Champion

from states.title import Title
from states.pause import Pause


class Game:
    """
    Main game class, manages:
    - game loop
    - delta time
    """

    name = "Aberrant Evolution"
    FONT_DIR = "assets/fonts"

    def __init__(self) -> None:
        """
        Make new instance of Game.
        """
        pygame.init()
        self.run = True
        self.delta_time = 0.0
        self.prev_time = 0.0
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(Game.name)

        self.pygame_settings()

        self.state_stack = []
        self.current_state = None

        self.fonts = {}

        self.load_assets()
        self.load_states()

    def pygame_settings(self):
        """
        Pygame specific preferences.
        """
        # Block irrelevant events
        # pygame.event.set_blocked()
        # pygame.event.set_allowed()

        # Grab input
        pygame.event.set_grab(True)

        # Key repeat
        # pygame.key.set_repeat(1000)

        # Special cursor
        # pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        # pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        # pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        # pygame.mouse.set_cursor(*pygame.cursors.tri_right)
        # cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
        # pygame.mouse.set_cursor((8, 16), (0, 0), *cursor)
        
        # Not working too well
        # pygame.cursors.thickarrow_strings
        # pygame.cursors.sizer_x_strings
        # pygame.cursors.sizer_y_strings
        # pygame.cursors.sizer_xy_strings
        # pygame.cursors.textmarker_strings

    def load_assets(self):
        """
        Load in game assets.
        """
        # Fonts
        for file in os.listdir(Game.FONT_DIR):
            font_path = os.path.join(Game.FONT_DIR, file)
            font_name = os.path.splitext(file)[0]
            self.fonts[font_name] = pygame.font.Font(font_path, 36)

        # Sounds, spritesheets, etc.

    def load_states(self):
        """
        Load in starting game state.
        """
        title_state = Title(self, Game.name)
        self.current_state = title_state
        self.state_stack.append(title_state)

    def print_startup_info(self) -> None:
        """
        Prints some info on startup.
        """
        # print(f"Blocked events: {pygame.event.get_blocked(pygame.QUIT)}")
        print(f"Inputs are grabbed for this game? {pygame.event.get_grab()}")
        print(f"Default font: {pygame.font.get_default_font()}")
        print(f"Pygame display backend: {pygame.display.get_driver()}")
        print(pygame.display.Info())
        # print(f"Available fonts: ")
        # for font in pygame.font.get_fonts():
        #     print(font)

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

            # --- Change state? --- #
            self.current_state = self.state_stack[-1]

            # --- Delta time logic --- #
            self.get_delta_time()

            # --- Event Loop --- #
            self.event_loop()

            # --- Game logic --- #
            self.update()

            # --- Drawing to screen --- #
            self.draw()
            if not isinstance(self.current_state, Pause):
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
            # Esc always quits game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.run = False
                return
        
        self.current_state.event_loop(events)

    def update(self) -> None:
        """
        Handle global and state logic per frame.
        """
        self.current_state.update()

    def draw(self) -> None:
        """
        Draw global and state items per frame.
        """
        self.current_state.draw()
        self.screen.blit(self.current_state.screen, (0, 0))

    def quit_game(self) -> None:
        """
        Cleanup and quit the game.
        """
        pygame.quit()
        exit()

# Main
if __name__ == "__main__":
    game = Game()
    game.start()

