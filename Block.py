import pygame

black = (0,0,0)

##class Block(pygame.sprite.Sprite):
##
##    def __init__(self, color, width, height, pos):
##
##        pygame.sprite.Sprite.__init__(self)
##
##        self.image = pygame.Surface([width, height])
##        self.image.fill(color)
##
##        self.rect = pygame.Rect(pos[0], pos[1], width, height)

class Block(object):

    def __init__(self, pos):
        
        obstacles.append(self)
        self.rect = pygame.Rect(pos[0],pos[1], 16, 16)
