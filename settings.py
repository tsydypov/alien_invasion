class Settings:
    """Class for keeping settings of game"""
    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Aliens settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
