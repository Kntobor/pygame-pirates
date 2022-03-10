import pygame
from support import importFolder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importAssets()
        self.frameIndex = 0
        self.animSpeed = 0.15
        self.image = self.animations['idle'][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)

        #Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16
        self.jumping = False

    def importAssets(self):
        characterPath = '..\graphics\character'
        self.animations = {'idle' : [], 'run' : [], 'jump' : [], 'fall' : []} # Name of categories matches folders

        # Cycles through every animation type and imports the animation
        for animation in self.animations.keys():
            fullPath = characterPath + f'\{animation}'
            self.animations[animation] = importFolder(fullPath)

    def input(self):
        keys = pygame.key.get_pressed()

        # If keys are pressed than the vector self.direction is (1 or -1, 0)
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jumping == False:
                self.jump()


    def jump(self):
        self.jumping = True
        self.direction.y = self.jumpSpeed

    def update(self):
        self.input()