class Settings:
    def __init__(self):
        # Player settings
        self.life_limit = 3

        # Speeding up the game
        self.speedup_scale = 1.1
        # Increasing point values
        self.score_scale = 1.5

    def initialize_easy_dynamic_settings(self):
        self.bullet_speed = 5
        self.enemy_speed = 1
        self.enemy_points = 50

    def initialize_medium_dynamic_settings(self):
        self.bullet_speed = 5.5
        self.enemy_speed = 1.5
        self.enemy_points = 60

    def initialize_hard_dynamic_settings(self):
        self.bullet_speed = 6
        self.enemy_speed = 2
        self.enemy_points = 70

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)