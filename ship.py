import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image and get its rect
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Every new ship start from the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position, based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship in its position"""
        self.screen.blit(self.image, self.rect)
