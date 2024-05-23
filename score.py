"""
# score.py - manages the game score
# Author: Andrea Stevens
"""

class Score:
    def __init__(self):
        self.current_score = 0

    def increment(self):
        self.current_score += 1

    def reset(self):
        self.current_score = 0