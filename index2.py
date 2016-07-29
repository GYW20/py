#coding:utf-8
import pygame
import sys
class Ball:
    image = pygame.image.load(r"C:\Users\guoyanwen\Pictures\Camera Roll\ball1.png")
    def __init__(self):
        self.boundary = Ball.image.get_rect()
        self.speed_x , self.speed_y = 2,2
    def move(self):
        self.boundary = self.boundary.move(self.speed_x,self.speed_y)
        if self.boundary.left < 0 or self.boundary.right > SCREEN_WEIGHT:
            self.speed_x *= -1
        if self.boundary.top < 0 or self.boundary.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1
    def draw(self):
        SCREEN.blit(Ball.image,self.boundary)
class Ballgame:
    def __init__(self):
        self.balls = []
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.balls.append(Ball())
            SCREEN.fill(BLACK)
            for ball in self.balls:
                ball.move()
                ball.draw()
            pygame.display.flip()
            clock.tick(60)
if __name__ == 'main':
    pygame.init()
    SCREEN_SIZE = 1000,500
    SCREEN_WEIGHT,SCREEN_HEIGHT = SCREEN_SIZE
    BLACK = 0,0,0
    clock = pygame.time.CLock()
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    Ballgame().run()