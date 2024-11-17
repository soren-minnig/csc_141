class Settings:
    def __init__(self):
        # General settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Player settings
        self.player_speed = 4
        self.life_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (227, 186, 75)
        self.bullets_allowed = 3

        # Enemy settings
        self.fleet_drop_speed = 10

        # Speeding up the game
        self.speedup_scale = 1.1
        # Increasing point values
        self.score_scale = 1.5

    def initialize_easy_dynamic_settings(self):
        self.bullet_speed = 3.5
        self.enemy_speed = 1
        self.enemy_points = 50

        self.fleet_direction = 1

    def initialize_medium_dynamic_settings(self):
        self.bullet_speed = 4
        self.enemy_speed = 1.5
        self.enemy_points = 70

        self.fleet_direction = 1

    def initialize_hard_dynamic_settings(self):
        self.bullet_speed = 4.5
        self.enemy_speed = 2
        self.enemy_points = 100

        self.fleet_direction = 1

    def increase_speed(self):
        self.player_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)