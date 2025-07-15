import pygame
from Game import Game
from Config import Config


def main():
    # Set the game window
    display = pygame.display.set_mode(
        (Config["game"]["width"], Config["game"]["height"])
    )

    # Add game window title
    pygame.display.set_caption(Config["game"]["caption"])

    # Create game instance
    game = Game(display)
    # Run the main game loop
    game.loop()


if __name__ == "__main__":
    main()
