import pygame
from support import importFolder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importAssets()
        self.frameIndex = 0
        self.animSpeed = 0.15
        self.image = self.animations['idle'][int(self.frameIndex)]
        self.rect = self.image.get_rect(topleft = pos)

        #Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16
        self.jumping = False
        self.status = 'idle'
        self.facingRight = True
        self.onGround = False
        self.onCeiling = False
        self.onRight = False
        self.onLeft = False

    def importAssets(self):
        characterPath = '..\graphics\character'
        self.animations = {'idle' : [], 'run' : [], 'jump' : [], 'fall' : []} # Name of categories matches folders

        # Cycles through every animation type and imports the animation
        for animation in self.animations.keys():
            fullPath = characterPath + f'\{animation}'
            self.animations[animation] = importFolder(fullPath)

    def animate(self):
        animation = self.animations[self.status]

        # Loop over frame index
        self.frameIndex += self.animSpeed
        if self.frameIndex >= len(animation):
            self.frameIndex = 0

        image = animation[int(self.frameIndex)]
        flippedImage = pygame.transform.flip(image, True, False)
        if self.facingRight:
            self.image = image
        else:
            self.image = flippedImage
        
        # Rectangle Adjustments
        if self.onGround:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.onCeiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)

    def input(self):
        keys = pygame.key.get_pressed()

        # If keys are pressed than the vector self.direction is (1 or -1, 0)
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facingRight = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.jumping == False:
                self.jump()

    def checkStatus(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def jump(self):
        self.jumping = True
        self.direction.y = self.jumpSpeed

    def update(self):
        self.input()
        self.checkStatus()
        self.animate()