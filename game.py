"""
# game.py - This will be the central class coordinating game elements, manages the game loop, update, draw and reset logic
# Author: Andrea Stevens
"""

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
