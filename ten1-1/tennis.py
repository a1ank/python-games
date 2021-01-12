import pygame
import random

balls = []


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.score = 0


class Ball:
    def __init__(self,x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)
        while self.dx == 0 or self.dy == 0:
            self.dx = random.randint(-3, 3)
            self.dy = random.randint(-3, 3)
        self.img = pygame.image.load('balls.png')
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.visible = True


size = (540, 500)

player1 = Player(5, 180, 20, 125)
player2 = Player(515, 180, 20, 125)
ball = Ball(size[0]/2 - 5, size[1]/2 - 15, 32)
balls.append(ball)
time = 0

pygame.init()
myfont = pygame.font.SysFont('Times New Roma', 75)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
true = False
c = 0

while not true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1.dy = 5
            if event.key == pygame.K_w:
                player1.dy = -5
            if event.key == pygame.K_DOWN:
                player2.dy = 5
            if event.key == pygame.K_UP:
                player2.dy = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player1.dy = 0
            if event.key == pygame.K_w:
                player1.dy = 0
            if event.key == pygame.K_DOWN:
                player2.dy = 0
            if event.key == pygame.K_UP:
                player2.dy = 0

    if player1.y < 0:  # ⭱
        player1.y = 0
    if player2.y < 0:
        player2.y = 0
    if player1.y > size[1] - player1.height:  # ⭳
        player1.y = size[1] - player1.height
    if player2.y > size[1] - player2.height:
        player2.y = size[1] - player2.height

    player1.y += player1.dy
    player2.y += player2.dy

    for ball in balls:
        if ball.visible:
            ball.x += ball.dx
            ball.y += ball.dy

    time += 1
    if time >= 100:
        ball = Ball(random.randrange(size[0]/2,size[0]/2+1,1),random.randrange(size[1]/2,size[1]/2+1,1), 32)
        balls.append(ball)
        time = 0

    for ball in balls:
        if ball.x > size[0] - ball.size - player2.width:
            if (ball.y + ball.size / 2 > player2.y) and (ball.y + ball.size / 2 < player2.y + player2.height):
                ball.dx = -abs(ball.dx) * 1.3
            else:
                balls.remove(ball)
                player1.score += 1
                c = 0

        if ball.x < player1.x + player1.width:
            if (ball.y + ball.size / 2 > player1.y) and (ball.y + ball.size / 2 < player1.y + player1.height):
                ball.dx = +abs(ball.dx) * 1.3
            else:
                balls.remove(ball)
                player2.score += 1
                c = 0

        # Departure over the upper and lower bound
        if ball.y < 1:
            ball.dy = +abs(ball.dy)
        if ball.y > size[1] - ball.size:
            ball.dy = -abs(ball.dy)

    c += 10
    if c > 255:
        c = 255
    screen.fill((255, c, c))

    pygame.draw.line(screen, (105, 105, 105), (size[0]/2 + 10, 0), (size[0]/2 +10, size[1]), 2)

    pygame.draw.rect(screen, (105, 105, 105), [
        player1.x, player1.y, player1.width, player1.height
    ], 0)
    pygame.draw.rect(screen, (105, 105, 105), [
        player2.x, player2.y, player2.width, player2.height
    ], 0)

    # Ball display and visible 
    for ball in balls:
        if ball.visible:
            screen.blit(ball.img, (ball.x, ball.y))

    text_surface = myfont.render(str(player1.score), False, (255, 0, 0))
    screen.blit(text_surface, (size[0] / 3, 10))
    text_surface = myfont.render(str(player2.score), False, (255, 0, 0))
    screen.blit(text_surface, (size[0] * 2 / 3, 10))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
