import pygame
from tiles import Tile
from settings import tileSize

class Level:
    def __init__(self, levelData, surface):
        self.displaySurface = surface
        self.generate(levelData)

    def generate(self, layout):
        self.tiles = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for columnIndex, cell in enumerate(row):
                if cell == 'X':
                    x = columnIndex * tileSize
                    y = rowIndex * tileSize

                    tile = Tile((x,y), tileSize)
                    self.tiles.add(tile)
            

    def run(self):
        self.tiles.draw(self.displaySurface)