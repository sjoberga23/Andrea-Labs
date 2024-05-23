"""
# dino.py - Manages the Dino character, including jumping and moving
# Author: Andrea Stevens
"""
class Dino:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.jump_state = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_state = 10  # Arbitrary jump height

    def move(self):
        if self.is_jumping:
            self.y_position += self.jump_state
            self.jump_state -= 1
            if self.jump_state <= -10:  # Arbitrary fall speed
                self.is_jumping = False
                self.jump_state = 0
                self.y_position = 0class Dino:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.jump_state = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_state = 10  # Arbitrary jump height

    def move(self):
        if self.is_jumping:
            self.y_position += self.jump_state
            self.jump_state -= 1
            if self.jump_state <= -10:  # Arbitrary fall speed
                self.is_jumping = False
                self.jump_state = 0
                self.y_position = 0
