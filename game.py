from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(400, 300)
        self.day_length = 60
        self.time_elapsed = 0
        self.loop_count = 1

    def update(self, dt):
        self.player.update(dt)
        self.time_elapsed += dt
        if self.time_elapsed >= self.day_length:
            self.reset_loop()

    def reset_loop(self):
        self.loop_count += 1
        self.time_elapsed = 0
        self.player.rect.topleft = (400, 300)

    def draw(self):
        self.screen.fill((20, 20, 30))
        self.player.draw(self.screen)
