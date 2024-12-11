import json
from pathlib import Path

class Stats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        self.high_score = self.check_high_score()

    def reset_stats(self):
        self.lives_left = self.settings.life_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        path = Path('game_high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0