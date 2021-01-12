import pygame
pygame.init()
size = (1000,700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
white = (255, 255, 255)
img2 = pygame.image.load ('3.png')
img = pygame.image.load ('2.png')  #<------------------------------


x = 350
y = 190
dx = 2
dy = 2

x2 = 290
y2 = 170

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: #PRESS KEY
            if event.key == pygame.K_RIGHT:
                dx = 2
            if event.key == pygame.K_LEFT:
                dx = -2
            if event.key == pygame.K_DOWN:
                dy = 2
            if event.key == pygame.K_UP:
                dy = -2
            if event.key == pygame.K_UP and dx == -2:
                img = pygame.transform.rotate(img, -5)
            if event.key == pygame.K_DOWN and dx == -2:
                img = pygame.transform.rotate(img, 5)

        if event.type == pygame.KEYUP: #PRESS KEY
            if event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0


    x = x + dx
    y = y + dy
    #logic:

    #the end of logic

    screen.fill(white)
    pygame.draw.rect(screen, (200,100,100),
        [500,500,1000,10],3)
    screen.blit(img2,(x2,y2))
    screen.blit(img,(x,y)) #<------------------------------
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
