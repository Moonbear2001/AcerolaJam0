import pygame
import math

from game_object import GameObject
from constants import *
from my_math import *
from ability import Ability



class Champion(GameObject):
    """
    Abstract champion class. 
    """

    Q_CD = 5 * FPS
    W_CD = 5 * FPS
    E_CD = 5 * FPS
    D_CD = 5 * FPS
    AA_CD = 5 * FPS

    kit_radius = 20
    aa_cd = 3

    def __init__(self, state, screen, color, width, height):
        """
        Make a new Champion.
        """
        super().__init__(state, screen)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.move_clicks = {}
        self.attack_clicks = {}
        self.linger_time = 10
        
        self.input = {"aa": False, "a": False, "s": False, "d": False, "q": False, "w": False, "e": False}
        self.cds = {"aa": 0.0 , "d": 0.0, "q": 0.0, "w": 0.0, "e": 0.0}
        self.target_pos = (WIDTH // 2, HEIGHT // 2)

        # TODO: VARIABLE?
        self.auto_range = 100
        self.move_speed = 3

        self.camera_offset = pygame.math.Vector2()

        # Abilities
        self.abilities = pygame.sprite.Group()
        self.abilities.add(Ability(self.rect.center, Champion.kit_radius, 2, "square", RED))
        self.abilities.add(Ability(self.rect.center, Champion.kit_radius, 1, "circle", GREEN))

        self.wants_to_aa = False
        self.target = None


    def event_loop(self, events, camera_offset) -> None:
        """
        Track input.
        """
        if pygame.key.get_pressed()[pygame.K_a]:
            self.input["a"] = True

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Movement clicks
                if event.button == RIGHT_CLICK:
                    self.wants_to_aa = False
                    map_pos = (event.pos[0] + camera_offset.x, event.pos[1] + camera_offset.y)
                    self.move_clicks[map_pos] = self.linger_time
                    self.target_pos = map_pos
                
                # Auto attacks
                elif event.button == LEFT_CLICK:
                    self.input["aa"] = True
                    map_pos = (event.pos[0] + camera_offset.x, event.pos[1] + camera_offset.y)
                    self.attack_clicks[map_pos] = self.linger_time

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_a:
                #     self.input["a"] = True
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


    def update(self, camera_offset) -> None:
        """
        Update.
        """
        # Update camera offset
        self.camera_offset = camera_offset

        # Update mouse clicks
        for click_pos, time in list(self.move_clicks.items()):
            self.move_clicks[click_pos] -= 1
            if self.move_clicks[click_pos] == 0:
                del self.move_clicks[click_pos]
        for click_pos, time in list(self.attack_clicks.items()):
            self.attack_clicks[click_pos] -= 1
            if self.attack_clicks[click_pos] == 0:
                del self.attack_clicks[click_pos]

        # Update cooldowns
        for cd in self.cds:
            if self.cds[cd] > 0:
                self.cds[cd] -= 1

        # Move toward target click
        self.move_towards_target()

        # Update abilities
        self.abilities.update(self.rect.center)        

    
    def draw(self) -> None:
        """
        Draw self.
        """
        # Draw clicks
        for click_pos, time in self.move_clicks.items():
            pygame.draw.circle(self.screen, NEON, click_pos, int(10 * (time/self.linger_time)))
        for click_pos, time in self.attack_clicks.items():
            pygame.draw.circle(self.screen, RED, click_pos, int(10 * (time/self.linger_time)))

        # Draw character body
        pygame.draw.circle(self.screen, BLACK, self.rect.center, 10)
        pygame.draw.circle(self.screen, LIGHT_GRAY, self.rect.center, Champion.kit_radius, 2)


        # Draw auto range
        if self.input["a"]:
            self.a()

        # Auto attack something
        if self.input["aa"] and self.cds["aa"] == 0:
            self.aa()

        # Call abilities
        if self.input["q"] and self.cds["q"] == 0:
            self.q()
        if self.input["w"] and self.cds["w"] == 0:
            self.w()
        if self.input["e"] and self.cds["e"] == 0:
            self.e()
        if self.input["d"] and self.cds["d"] == 0:
            self.d()
        if self.input["s"]:
            self.s()

        # Draw abilities
        self.abilities.draw(self.screen)

        # Draw auto attack reload
        if self.cds["aa"] > 0:
            pygame.draw.arc(self.screen, ORANGE, self.rect, 0, 2 * PI * (self.cds["aa"] / Champion.AA_CD), width=5)

        # RESET
        self.input = {"aa": False, "a": False, "s": False, "d": False, "q": False, "w": False, "e": False}

    def aa(self) -> None:
        """
        Auto attack a target.
        """
        # Nothing targeted
        self.target = self.state.get_targeted()
        if self.target is None:
            print("nothing targeted")
            return
        
        # Targeted but not in range
        elif not self.is_in_range(self.target):
            print("targeted not in range")
            self.wants_to_aa = True
            self.target_pos = self.target.rect.center

        # Targeted and in range, actually auto
        else:
            self.cds["aa"] = Champion.AA_CD
            print("actually auto")


    def q(self) -> None:
        """
        Draw auto range.
        """
        self.cds["q"] = Champion.Q_CD
        print("q")

    def w(self) -> None:
        """
        Use w ability.
        """
        self.cds["w"] = Champion.W_CD
        print("w")

    def e(self) -> None:
        """
        Use e ability.
        """
        self.cds["e"] = Champion.E_CD
        print("e")

    def a(self) -> None:
        """
        Draw auto range.
        """
        pygame.draw.circle(self.screen, BLUE, self.rect.center, self.auto_range, 2)

    def s(self) -> None:
        """
        Stop movement.
        """
        self.target_pos = self.rect.center

    def d(self) -> None:
        """
        Flash.
        """
        self.cds["d"] = Champion.D_CD

        # Get mouse position and direction towards flash
        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()) + self.camera_offset
        dx = mouse_pos.x - self.rect.centerx
        dy = mouse_pos.y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        flash_unit_vector = pygame.math.Vector2(dx / distance, dy / distance)
        if distance < FLASH_DIST:
            self.rect.center = (mouse_pos.x, mouse_pos.y)
        else:
            self.rect.x += flash_unit_vector.x * FLASH_DIST
            self.rect.y += flash_unit_vector.y * FLASH_DIST

        # Reset movement if flash is away from previously desired direction
        target_vector = vector_between_points(self.rect.center, self.target_pos)
        if angle_between(target_vector, (flash_unit_vector.x, flash_unit_vector.y)) > 90:
            self.target_pos = self.rect.center

    def is_in_range(self, minion) -> bool:
        """
        Check if a game objects center coordinate is in this champions auto attack range.
        """
        # Calculate the distance between the center points of the champion and minion
        distance = math.sqrt((self.rect.centerx - minion.rect.centerx)**2 + (self.rect.centery - minion.rect.centery)**2 )

        # Check if the distance is less than or equal to the champion's attack range
        return distance <= self.auto_range
    
    def move_towards_target(self):
        """
        Move the champion toward the desired pos.
        """

        # TESTING
        if self.wants_to_aa:
            if self.is_in_range(self.target):
                print('in range! stop')
                self.target_pos = self.rect.center
                self.wants_to_aa = False


        distance = math.sqrt((self.target_pos[0] - self.rect.centerx)**2 + (self.target_pos[1] - self.rect.centery)**2)
        if distance >= self.move_speed:
            direction_x = (self.target_pos[0] - self.rect.centerx) / distance
            direction_y = (self.target_pos[1] - self.rect.centery) / distance
            self.rect.x += direction_x * self.move_speed
            self.rect.y += direction_y * self.move_speed
        else:
            self.rect.center = self.target_pos


            
    