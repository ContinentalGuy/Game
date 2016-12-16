import pygame

# Set display size
d_width = 512;
d_height = 256;

# Initialization
pygame.init();
gameDisplay = pygame.display.set_mode((d_width,d_height));
# Window title
pygame.display.set_caption('Action RPG');
# Needed to correctly set fps
clock = pygame.time.Clock()

# Loading images from directory
persImg = pygame.image.load('./IsometricPers.png');
mapImg = pygame.image.load('./IsometricMap.png');

# Function that shows users pers on display
def Pers(x,y):
    gameDisplay.blit(persImg, (x,y))
##    print 'Pers position: ',x,':',y

# Shows image under pers
def Map(x,y):
    gameDisplay.blit(mapImg, (x,y))

def jump():
    pass

# Flag to end running application
crashed = False

# Map image location
xMap = 0;
yMap = 0;

# Can be used as pers speed
xPers = d_width/2;
yPers = d_height/2;

# Bias for statment when key is not pressed
x_bias = 0;
y_bias = 0;

# Application runs while flag 'crashed' is set to False 
while not crashed:
    # Cycle catches all events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
    # Catches all pressed keys
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:
            x_bias = -2
            
        if event.key == pygame.K_RIGHT:
            x_bias = 2

        if event.key == pygame.K_UP:
            y_bias = -2

        if event.key == pygame.K_DOWN:
            y_bias = 2

    # Pers moves
    xPers += x_bias;
    yPers += y_bias;

    # Fill display with black color and put Map and Pers image on it
    gameDisplay.fill((0,0,0))
    Map(xMap,yMap)
    Pers(xPers,yPers)                

    if event.type == pygame.KEYUP:
        x_bias = y_bias = 0;
        #print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
