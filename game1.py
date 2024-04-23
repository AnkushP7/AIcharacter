ip install pygame
import pygame
import sys
from pygame.locals import *
from random import randint

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chase Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 5

    def move_toward(self, target):
        # Move towards the target position
        if self.rect.x < target.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > target.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < target.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > target.rect.y:
            self.rect.y -= self.speed

class Target(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH - width)
        self.rect.y = randint(0, SCREEN_HEIGHT - height)


# Create player and target
player = Player(BLUE, 50, 50)
target = Target(RED, 50, 50)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    player.move_toward(target)

    screen.fill(WHITE)
    screen.blit(player.image, player.rect)
    screen.blit(target.image, target.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
