import pygame


class Ship:

    def __init__(self, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen

        # Load ship image and get its rect
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Every new ship start from the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship in its position"""
        self.screen.blit(self.image, self.rect)
