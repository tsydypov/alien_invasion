import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        """Create bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet at the position (0,0) and set right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet's position keeps in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update bullet's position in float
        self.y -= self.speed_factor

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
