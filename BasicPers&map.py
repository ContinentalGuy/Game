import pygame

d_width = 512;
d_height = 256;

pygame.init();
gameDisplay = pygame.display.set_mode((d_width,d_height));
pygame.display.set_caption('Action RPG');
clock = pygame.time.Clock()

##persImg = pygame.image.load('./Pers.png');
##mapImg = pygame.image.load('./Map.png');
persImg = pygame.image.load('./IsometricPers.png');
mapImg = pygame.image.load('./IsometricMap.png');


def Pers(x,y):
    gameDisplay.blit(persImg, (x,y))
##    print 'Pers position: ',x,':',y

def Map(x,y):
    gameDisplay.blit(mapImg, (x,y))

def jump():
    pass

crashed = False

##xMap = d_width/2 - 50;
##yMap = d_height/2 - 50;
xMap = 0;
yMap = 0;

xPers = d_width/2;
yPers = d_height/2;

x_bias = 0;
y_bias = 0;

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
    
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            x_bias = -2
            
        if event.key == pygame.K_RIGHT:
            x_bias = 2

        if event.key == pygame.K_UP:
            y_bias = -2

        if event.key == pygame.K_DOWN:
            y_bias = 2


    xPers += x_bias;
    yPers += y_bias;

    gameDisplay.fill((0,0,0))
    Map(xMap,yMap)
    Pers(xPers,yPers)                

    if event.type == pygame.KEYUP:
        x_bias = y_bias = 0;
        #print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
