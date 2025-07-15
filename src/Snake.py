import pygame
from Config import Config

"""
    Class: Snake
        - Used to keep track of player character
    Use: snake = Snake(<self>, <display/window>)
    Method:
        - get_rect(<self>): Return the snake drawing rectangle
        - eat(<self>): Increment body size on apple eatten
        - draw_body(<self>): Draw the snake
        - move(<self>, <x-axis>, <y-axis>): Increment position on movement
"""


class Snake:
    def __init__(self, display):
        self.body = []
        self.max_size = 0
        self.display = display
        self.x_pos = int((Config["game"]["width"] - 30) / 2)
        self.y_pos = int((Config["game"]["height"] - 30) / 2)

        if self.x_pos % 10 != 0:
            self.x_pos += 5
        if self.y_pos % 10 != 0:
            self.y_pos += 5

    def get_rect(self):
        return pygame.draw.rect(
            self.display,
            Config["colors"]["green"],
            [
                self.x_pos,
                self.y_pos,
                Config["snake"]["height"],
                Config["snake"]["width"],
            ],
        )

    def eat(self):
        self.max_size += 1

    def draw_body(self):
        for cell in self.body:
            pygame.draw.rect(
                self.display,
                Config["colors"]["green"],
                [cell[0], cell[1], Config["snake"]["width"], Config["snake"]["height"]],
            )

    def move(self, x_change, y_change):
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += x_change
        self.y_pos += y_change

        if len(self.body) > self.max_size:
            del self.body[0]
