import pygame
def loadimage(path):
    pygame.image.load(path)
    pygame.transform.scale(path,(250,250))
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("diegos dum game") 
standing = pygame.image.load("idk/x.png")
standing=pygame.transform.scale(standing,(250,250))
enme=[loadimage("idk/b1.png"),loadimage("idk/b2.png"),loadimage("idk/b3.png"),loadimage("idk/b3.png")]
#attack=
#X is left and right
x = 0
#y is up and down
y= 0
width = 50
height = 50
speed = 5
run = True
while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys =pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -=speed 
    if keys[pygame.K_UP]:
        y -=speed
    if keys[pygame.K_DOWN]:
        y +=speed
    window.fill((0,0,0))
    #pygame.draw.rect(window, (0, 255,0), (x, y, width, height))
    window.blit(standing,(x,y))
    pygame.display.update()
pygame.quit()
