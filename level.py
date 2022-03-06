import pygame
from player import Player
from tiles import Tile
from settings import tileSize

class Level:
    def __init__(self, levelData, surface):
        self.displaySurface = surface
        self.generate(levelData)

        self.worldShift = 0 # Represents the amount that the world needs to shift for character movement

    def generate(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for rowIndex, row in enumerate(layout): # For each row in the level map
            for columnIndex, cell in enumerate(row): # For each column in the level map
                x = columnIndex * tileSize
                y = rowIndex * tileSize
                if cell == 'X': # 'X' cell indicates a ground tile
                    tile = Tile((x,y), tileSize)
                    self.tiles.add(tile)
                
                if cell == 'P': # 'P' cell indicates player
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)
            
    def scrollX(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x

        if playerX < 200:
            self.worldShift = 8
            player.speed = 0        
        elif playerX > 1000:
            self.worldShift = -8
            player.speed = 0

    def run(self):
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)

        self.player.update()
        self.player.draw(self.displaySurface)

        self.scrollX()

        