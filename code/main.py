import pygame
import sys

# File imports
from settings import *
from tiles import Tile
from level import Level

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pygame Platformer')
clock = pygame.time.Clock()
level = Level(levelMap, screen)

# Event Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break

    screen.fill('black')
    level.run() # Run all level logic and updates (level.py)

    pygame.display.update()
    clock.tick(60) # Caps framerate at 60