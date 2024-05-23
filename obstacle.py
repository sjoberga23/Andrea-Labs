"""
# obstacle.py - manages obstacles including movement and collision detection 
# Author: Andrea Stevens
"""

class Obstacle:
    def __init__(self, x_position=100, y_position=0, speed=5):
        self.x_position = x_position
        self.y_position = y_position
        self.speed = speed

    def move(self):
        self.x_position -= self.speed
        if self.x_position < 0:
            self.x_position = 100  # Reset to start position

    def check_collision(self, dino):
        return self.x_position == dino.x_position and self.y_position == dino.y_position