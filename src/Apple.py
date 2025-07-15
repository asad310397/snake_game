import random
import pygame
from Config import Config

"""
    Class: Apple
        - Used to keep track of apple character
    Use: apple = Apple(<self>, <display/window>)
    Method:
        - randomize(<self>): generate random location for apple
        - get_rect(<self>): Return the apple drawing rectangle
"""


class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0
        self.randomize()
        self.display = display

    def randomize(self):

        max_x = (
            Config["game"]["width"]
            - Config["game"]["bumper_size"]
            - Config["snake"]["width"]
        )
        max_y = (
            Config["game"]["height"]
            - Config["game"]["bumper_size"]
            - Config["snake"]["height"]
        )

        self.x_pos = random.randrange(Config["game"]["bumper_size"] + 10, max_x, 10)
        self.y_pos = random.randrange(Config["game"]["bumper_size"] + 10, max_y, 10)

    def get_rect(self):
        return pygame.draw.rect(
            self.display,
            Config["colors"]["apple-red"],
            [
                self.x_pos,
                self.y_pos,
                Config["apple"]["height"],
                Config["apple"]["width"],
            ],
        )
