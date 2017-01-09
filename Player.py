import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.velocity = 0
        self.fall = True
        self.stand = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def jump(self):
        
        self.rect.y += 10

    def move(self, dx, dy):
        
        if dx != 0:
            self.moveAxis(dx,0)
##        if dy != 0:
##            self.moveAxis(0,dy)

    def moveAxis(self, dx, dy):
        
        self.rect.x += dx
##        self.rect.y += dy

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if dx > 0:
                    self.rect.right = obstacle.rect.left
                if dx < 0:
                    self.rect.left = obstacle.rect.right
                if dy > 0:
                    self.rect.bottom = obstacle.rect.top
                if dy < 0:
                    self.rect.top = obstacle.rect.bottom

    def update(self,gravity):

        self.velocity += gravity
        self.dy -= self.velocity
