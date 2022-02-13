import pygame
import sys

from settings import *
from tiles import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pygame Game')
clock = pygame.time.Clock()
level = Level(levelMap, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break

    level.run()

    pygame.display.update()
    clock.tick(60)