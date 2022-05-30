import sys

import pygame


def run_game():
    # Initialize the game and create screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # Launch of main part of game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        # Last screen image
        pygame.display.flip()


run_game()
