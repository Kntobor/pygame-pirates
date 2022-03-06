import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        #Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16
        self.jumping = False

    def importAssets(self):
        characterPath = '../graphic/character/'
        self.animations = {'idle' : [], 'run' : [], 'jump' : [], 'fall' : []}

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