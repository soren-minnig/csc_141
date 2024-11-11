class Settings:
    def __init__(self):
        # General settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Player settings
        self.player_speed = 5
        self.life_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (227, 186, 75)
        self.bullets_allowed = 3

        # Enemy settings
        self.enemy_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1