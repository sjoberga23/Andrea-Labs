"""
# background.py - manages the background elements and ground rendering including drawing and updating the scroll position 
# Author: Andrea Stevens
"""

class Background:
    def __init__(self, image):
        self.image = image
        self.scroll_position = 0

    def scroll(self):
        self.scroll_position -= 1
        if self.scroll_position < -self.get_width():
            self.scroll_position = 0

    def draw(self):
        Log.i(f"Drawing background at position {self.scroll_position}")

    def get_width(self):
        return 800  # Example width, adjust as needed
