import pygame
from player import Player
from tiles import Tile
from settings import tileSize, screenWidth

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

        if playerX < screenWidth / 4 and directionX < 0:
            self.worldShift = 8
            player.speed = 0        
        elif playerX > screenWidth - (screenWidth / 4) and directionX > 0:
            self.worldShift = -8
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = 8

    def horizontalCollision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed 

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def verticalCollision(self):
        player = self.player.sprite

        player.direction.y += player.gravity
        player.rect.y += player.direction.y

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jumping = False

    def run(self):
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.scrollX()

        self.player.update()
        self.horizontalCollision()
        self.verticalCollision()
        self.player.draw(self.displaySurface)