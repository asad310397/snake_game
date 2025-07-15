import pygame
from Snake import Snake
from Apple import Apple
from Config import Config

"""
    Class: Game
        - The game class to run the actual game
    Use: game = Game(<self>, <display/window>)
    Methods:
        - startMenu(<self>): Create start menu for players to play, look at instructions, or quit
        - instructions(<self>): Create instructions page for players
        - loop(<self>): Run the game (more details in the function)
        - gameOver(<self>): Game end screen players can play again or quit
"""


class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        pygame.font.init()

        # set the game clock to check the updates
        clock = pygame.time.Clock()

        # add the snake and apple characters
        snake = Snake(self.display)
        apple = Apple(self.display)

        # Set change in x-axis and y-axis to 0
        x_change = 0
        y_change = 0

        # wait for input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit()

                    # if the user presses the arrow move accordingly
                    elif event.key == pygame.K_LEFT:
                        x_change = -1 * Config["snake"]["speed"]
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = 1 * Config["snake"]["speed"]
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -1 * Config["snake"]["speed"]
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = 1 * Config["snake"]["speed"]

            # Set red background, then back rectangle inside to create the background
            self.display.fill(Config["colors"]["red"])

            pygame.draw.rect(
                self.display,
                Config["colors"]["black"],
                [
                    Config["game"]["bumper_size"],
                    Config["game"]["bumper_size"],
                    Config["game"]["width"] - Config["game"]["bumper_size"] * 2,
                    Config["game"]["height"] - Config["game"]["bumper_size"] * 2,
                ],
            )

            # get the apple rectangle
            apple_rect = apple.get_rect()

            # update the snake position
            snake.move(x_change, y_change)

            # get currect snake head location
            snake_rect = snake.get_rect()

            # draw the snake at the current location
            snake.draw_body()

            # check for collition with the apple
            if apple_rect.colliderect(snake_rect):
                apple.randomize()  # create new apple
                self.score += 1  # increment score
                snake.eat()  # update the snake body

            # check snake body and head collision
            if len(snake.body) >= 1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        if self.gameOver() == 1:
                            self.score = 0
                            self.loop()

            # check collision between snake and border
            bumper_x = Config["game"]["width"] - Config["game"]["bumper_size"]
            bumper_y = Config["game"]["height"] - Config["game"]["bumper_size"]

            if (
                snake.x_pos < Config["game"]["bumper_size"]
                or snake.y_pos < Config["game"]["bumper_size"]
                or snake.x_pos + Config["snake"]["width"] > bumper_x
                or snake.y_pos + Config["snake"]["height"] > bumper_y
            ):
                if self.gameOver() == 1:
                    self.score = 0
                    self.loop()

            # create font for the game screen
            print("=" * 100, "Here", Config["game"]["font"])
            font = pygame.font.Font(Config["game"]["font"], 28)

            # create score text get the rectangle and add it to the screen
            score_text = "Score: {}".format(self.score)
            score = font.render(score_text, True, Config["colors"]["white"])

            score_rect = score.get_rect(
                center=(
                    Config["game"]["width"] / 2,
                    Config["game"]["height"] - Config["game"]["bumper_size"] / 2,
                )
            )

            self.display.blit(score, score_rect)

            # update the screen after all the change are made
            pygame.display.update()

            # set the clock to check at the specified frame rate
            clock.tick(Config["game"]["fps"])

    def gameOver(self):
        # set the game background
        self.display.fill(Config["colors"]["red"])

        pygame.draw.rect(
            self.display,
            Config["colors"]["black"],
            [
                Config["game"]["bumper_size"],
                Config["game"]["bumper_size"],
                Config["game"]["width"] - Config["game"]["bumper_size"] * 2,
                Config["game"]["height"] - Config["game"]["bumper_size"] * 2,
            ],
        )

        # create main title font and font for sub-instructions, then add them to the game screen
        font = pygame.font.Font(Config["game"]["title-font"], 38)
        instructions_font = pygame.font.Font(Config["game"]["font"], 28)

        over_text = "Game Over"
        over = font.render(over_text, True, Config["colors"]["white"])

        score_text = "Your Score: {}".format(self.score)
        score = font.render(score_text, True, Config["colors"]["white"])

        instructions_text = "Press Space to Play Again, Press Q to quit"
        instructions = instructions_font.render(
            instructions_text, True, Config["colors"]["white"]
        )

        over_rect = over.get_rect(
            center=(Config["game"]["width"] / 2, Config["game"]["height"] / 2 - 48)
        )

        score_rect = score.get_rect(
            center=(Config["game"]["width"] / 2, Config["game"]["height"] / 2)
        )

        instructions_rect = instructions.get_rect(
            center=(Config["game"]["width"] / 2, Config["game"]["height"] * (3 / 4))
        )

        self.display.blit(over, over_rect)
        self.display.blit(score, score_rect)
        self.display.blit(instructions, instructions_rect)

        # update the screen to the new end game screen
        pygame.display.update()

        # Wait for user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit()
                    elif event.key == pygame.K_SPACE:
                        return 1
