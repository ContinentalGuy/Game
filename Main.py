import pygame
import os
from Player import *
from Block import *

import pygame

class Player(object):

    def __init__(self):
        self.x = 32
        self.y = 32
        self.width = 16
        self.height = 16
        self.velocity = 0
        self.fall = True
        self.stand = False
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.rect.y += 0,5

    def jump(self, dx, dy):

        self.rect.x += 0
        self.rect.y += dy + 10

    def move(self, dx, dy):
        
        if dx != 0:
            self.moveAxis(dx,0)
        #if dy != 0:
        #    self.moveAxis(0,dy)

    def moveAxis(self, dx, dy):
        
        self.rect.x += dx
        #self.rect.y += dy

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if dx > 0:
                    self.rect.right = obstacle.rect.left
                    if self.fall == True:
                        self.fall = False
                        self.stand = True
                if dx < 0:
                    self.rect.left = obstacle.rect.right
                    if self.fall == True:
                        self.fall = False
                        self.stand = True
                if dy > 0:
                    self.rect.bottom = obstacle.rect.top
                    if self.fall == True:
                        self.fall = False
                        self.stand = True                    
                if dy < 0:
                    self.rect.top = obstacle.rect.bottom
                    if self.fall == True:
                        self.fall = False
                        self.stand = True                    

    def update(self,gravity):
        if self.velocity < 0:
            self.fall = True

        if self.stand == False:
            self.velocity += gravity
            
        self.y -= self.velocity



class Block(object):
    
    def __init__(self, pos):
        obstacles.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("I will do it!")
Display = pygame.display.set_mode((320,240))

clock = pygame.time.Clock()
obstacles = []
player = Player()

level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W                  W",
"W   WWWW       W   W",
"W   W       WWWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

gravity = -0.5
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Block((x,y))
        x += 16
    y += 16
    x = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2,0)
    if key[pygame.K_RIGHT]:
        player.move(2,0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player.jump(0,1)

    Display.fill(white)

    for obstacle in obstacles:
        pygame.draw.rect(Display, black, obstacle.rect)
    pygame.draw.rect(Display,red,player.rect)
    player.update(gravity)
    pygame.display.flip()
