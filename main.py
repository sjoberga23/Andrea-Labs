import time
time.sleep(0.1) # Wait for USB to become ready

from machine import Pin, ADC, I2C
from log import Log
from display import LCDDisplay
from button import Button
from sensor import DigitalSensor, AnalogSensor, TiltSensor

# Score Class
class Score:
    def __init__(self):
        self.current_score = 0

    def increment(self):
        self.current_score += 1

    def reset(self):
        self.current_score = 0

# Dino Class
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
                self.y_position = 0

# Obstacle Class
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

# Ground Class
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

# Background Class
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

# Game Class
class Game:
    def __init__(self):
        self.screen = LCDDisplay(rs=5, e=4, d4=3, d5=2, d6=1, d7=0)
        self.clock = time.time()
        self.dino = Dino()
        self.obstacles = [Obstacle(x_position=100 + i*50) for i in range(3)]
        self.ground = Ground(y_position=0)
        self.score = Score()
        self.sensors = [DigitalSensor(pin=2), AnalogSensor(pin=4, lowActive=True, threshold=500), TiltSensor(pin=6)]
        self.button = Button(pin=1, name="Jump", buttonhandler=self)
        self.background = Background(image="background.png")

    def buttonPressed(self, name):
        if name == "Jump":
            self.dino.jump()

    def buttonReleased(self, name):
        # Handle button release if necessary
        pass

    def run(self):
        while True:
            self.update()
            self.draw()
            time.sleep(0.016)  # Roughly 60 FPS

    def update(self):
        current_time = time.time()
        if current_time - self.clock >= 1:
            self.clock = current_time
            self.score.increment()

        for obstacle in self.obstacles:
            obstacle.move()
            if obstacle.check_collision(self.dino):
                Log.i("Game Over!")
                self.reset()

        if self.dino.is_jumping:
            self.dino.move()

        self.background.scroll()
        self.ground.update()

    def draw(self):
        self.screen.reset()
        self.screen.showText(f"Score: {self.score.current_score}", row=0, col=0)
        self.background.draw()
        self.ground.draw()
        # Additional draw logic for dino, obstacles, etc.

    def reset(self):
        self.score.reset()
        self.dino = Dino()
        self.obstacles = [Obstacle(x_position=100 + i*50) for i in range(3)]
        self.background = Background(image="background.png")
        self.ground = Ground(y_position=0)

# Main execution
if __name__ == "__main__":
    game = Game()
    game.run()
