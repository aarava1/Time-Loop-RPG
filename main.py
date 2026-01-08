import pygame
from game import Game

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Loop RPG")

clock = pygame.time.Clock()
game = Game(screen)

running = True
while running:
    dt = clock.tick(60) / 1000  # delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update(dt)
    game.draw()

    pygame.display.flip()

pygame.quit()
