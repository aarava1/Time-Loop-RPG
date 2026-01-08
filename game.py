import pygame
from player import Player
from time_loop import TimeLoopMemory


class Game:
    def __init__(self, screen):
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 32)
        self.screen = screen
        self.player = Player(400, 300)
        self.day_length = 5
        self.time_elapsed = 0
        self.loop_count = 1
        self.memory = TimeLoopMemory()
        self.memory_rect = pygame.Rect(200, 200, 40, 40)
        self.door_rect = pygame.Rect(600, 250, 40, 80)
        self.door_locked = True
        

    def update(self, dt):
        self.player.update(dt)
        if self.door_locked and self.player.rect.colliderect(self.door_rect):
            if self.player.rect.centerx < self.door_rect.centerx:
                self.player.rect.right = self.door_rect.left
            else:
                self.player.rect.left = self.door_rect.right

        self.time_elapsed += dt
        if self.time_elapsed >= self.day_length:
            self.reset_loop()

        keys = pygame.key.get_pressed()

        if self.player.rect.colliderect(self.memory_rect):
            if keys[pygame.K_e]:
                self.memory.remember("learned_secret")

        if keys[pygame.K_e]:
            if self.memory.knows("learned_secret"):
                self.door_locked = False

    def reset_loop(self):
        pygame.time.delay(500)
        self.loop_count += 1
        self.time_elapsed = 0
        self.player.rect.topleft = (400, 300)
        self.door_locked = True

    def draw(self):
        self.screen.fill((20, 20, 30))
        self.player.draw(self.screen)
        self.draw_ui()

        if not self.memory.knows("learned_secret"):
            pygame.draw.rect(self.screen, (120, 200, 120), self.memory_rect)

        if self.door_locked:
            pygame.draw.rect(self.screen, (200, 80, 80), self.door_rect)
        else:
            pygame.draw.rect(self.screen, (80, 200, 120), self.door_rect)

    def get_time_remaining(self):
        return max(0, int(self.day_length - self.time_elapsed))

    def draw_ui(self):
        time_left = self.get_time_remaining()
        loop_text = f"Loop: {self.loop_count}"
        time_text = f"Time Left: {time_left}s"

        loop_surface = self.font.render(loop_text, True, (255, 255, 255))

        if time_left <= 10:
            color = (255, 80, 80)
        elif time_left <= 25:
            color = (255, 180, 80)
        else:
            color = (255, 255, 255)

        time_surface = self.font.render(time_text, True, color)

        if self.memory.knows("learned_secret"):
            mem_text = "Memory: Secret Learned"
            mem_surface = self.font.render(mem_text, True, (150, 220, 150))
            self.screen.blit(mem_surface, (10, 70))

        if self.door_locked:
            text = "Door Locked"
            color = (255, 120, 120)
        else:
            text = "Door Unlocked"
            color = (120, 255, 180)

        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (10, 100))

        self.screen.blit(loop_surface, (10, 10))
        self.screen.blit(time_surface, (10, 40))


