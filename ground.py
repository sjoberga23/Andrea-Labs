"""
# ground.py - manages the ground includinig drawing and updating the scroll position 
# Author: Andrea Stevens
"""

class Ground:
    def __init__(self, y_position):
        self.y_position = y_position
        self.scroll_position = 0

    def draw(self):
        Log.i(f"Drawing ground at y position {self.y_position}")

    def update(self):
        self.scroll_position -= 1
        if self.scroll_position < -self.get_width():
            self.scroll_position = 0

    def get_width(self):
        return 800  # Example width, adjust as needed
