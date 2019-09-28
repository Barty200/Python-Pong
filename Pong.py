import pygame
from random import randint
from time import sleep

running = True
(width, height) = (1000, 700)

class Player:
    def __init__(self, xconstrain):
        self.xconstrain = xconstrain
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.xconstrain, pygame.mouse.get_pos()[1], 10, 50))

class Ball:
    def __init__(self):
        self.x = 500
        self.y = 350
        self.velx = randint(-10, 10)
        self.vely = randint(-10, 10)
        while True:
            if self.velx < 5 and self.velx > -5:
                self.velx = randint(-10, 10)
            elif self.vely < 5 and self.vely > -5:
                self.velx = randint(-10, 10)
            else:
                break
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (round(self.x), round(self.y)), 5)
    def update(self):
        if self.y > height or self.y < 0:
            self.vely *= -1
        if self.y > (pygame.mouse.get_pos()[1] - 25) and self.y < (pygame.mouse.get_pos()[1] + 25) and self.x > player.xconstrain:
            self.velx *= -1
        if self.x < 0:
            self.velx *= -1
        if self.x > width:
            print("You lost")
            pygame.display.quit()
            running = False
        self.x += self.velx
        self.y += self.vely
        self.velx *= 1.001
        self.vely *= 1.001

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
player = Player(970)
ball = Ball()

while running:
    try:
        clock.tick(50)
        screen.fill((0, 0, 0))
        player.draw()
        ball.draw()
        ball.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False
    except:
        pass
        
