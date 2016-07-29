#coding:utf-8
import pygame
import sys
class Ball():
    image = pygame.image.load(r"C:\Users\guoyanwen\Pictures\Camera Roll\ball1.png")
    def __init__(self):
       self.boundary = Ball.image.get_rect()
       self.speed_x , self.speed_y = 2,2
    def move(self):
        self.boundary = self.boundary.move(self.speed_x,self.speed_y)
        if self.boundary.left < 0 or self.boundary.right > SCREEN__WEIGHT:
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
if __name__ == '__main__':
    pygame.init()
    SCREEN__SIZE =1000,200
    SCREEN__WEIGHT,SCREEN_HEIGHT = SCREEN__SIZE
    BLACK = 0,0,0
    clock = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(SCREEN__SIZE)
    Ballgame().run()