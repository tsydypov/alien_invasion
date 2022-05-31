import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Initialize the game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Last screen image
        pygame.display.flip()


run_game()
