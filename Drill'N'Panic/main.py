import pygame
from pygame.locals import *
import sys
import random

FPSCLOCK = pygame.time.Clock()
pygame.init()
FPS = 60
DISPLAYSURF = pygame.display.set_mode((1500, 760))
moveLeft = False
moveRight = False
Drill_X = float(750)
vel_X = float(0)
Drill_D = 0
done_ = 0
Timer = 40
score = 20
scroll = 760
drill = pygame.image.load('graphics/drill.png').convert_alpha()
ground = pygame.image.load('graphics/ground.png').convert_alpha()
drill_rect = drill.get_rect(topleft=(Drill_X, 50))
test_font = pygame.font.Font('graphics/pixeltype.ttf', 50)
text = test_font.render('Hits left:' + str(score), False, "Black").convert()
text_rect = text.get_rect(center=(400, 50))

class Enemy:
    def __init__(self, x, y, dir, speed, enemy_rect):
        self.x = x
        self.y = y
        self.dir = dir
        self.speed = speed
        self.enemy_rect = enemy_rect
    def frame(self, x, y, dir, speed, enemy_rect, score, done_):
        self.y = self.y - (6 * self.speed)
        if random.randint(1, 40) == 1 and dir != 3:
            self.dir = random.randint(0, 2)
        if self.y <= -100:
            self.y = 760 + (self.speed * 500)
            self.x = random.randint(250, 1250)
            self.dir = random.randint(0, 2)
        if self.dir == 0:
            self.x = self.x + (1.2 * (-1 - (3 / (self.speed * self.speed))))
            self.edrill = pygame.image.load('graphics/enemyleft.png').convert_alpha()
        elif self.dir == 2:
            self.x = self.x + (1.2 * (1 + (3 / (self.speed * self.speed))))
            self.edrill = pygame.image.load('graphics/enemyright.png').convert_alpha()
        elif self.dir == 1:
            self.edrill = pygame.image.load('graphics/enemy.png').convert_alpha()
        elif self.dir == 3:
            self.edrill = pygame.image.load('graphics/skull.png').convert_alpha()
        if self.x <= -93:
            self.x = 1500
        elif self.x >= 1500:
            self.x = -93
        self.edrill_rect = drill.get_rect(topleft=(self.x, self.y))
        drill_rect = drill.get_rect(topleft=(Drill_X, 50))
        if self.dir != 3 and pygame.Rect.colliderect(self.edrill_rect, drill_rect) and done_ == 0:
            self.dir = 3
            score -= 1
        DISPLAYSURF.blit(self.edrill, self.edrill_rect)
        return score

enemy1 = Enemy(400, random.randint(200, 600), 1, 0.7, 0)
enemy2 = Enemy(600, random.randint(760, 1000), 0, 1, 0)
enemy3 = Enemy(200, random.randint(2500, 3000), 2, 1.5, 0)

def terminate():
    pygame.quit()
    sys.exit()

def done():
    DISPLAYSURF.blit(pygame.image.load('graphics/Earth 1.png'), (0, 0))
    pygame.display.update()
    FPSCLOCK.tick(15)
    DISPLAYSURF.blit(pygame.image.load('graphics/Earth 2.png'), (0, 0))
    pygame.display.update()
    FPSCLOCK.tick(15)
    DISPLAYSURF.blit(pygame.image.load('graphics/Earth 3.png'), (0, 0))
    pygame.display.update()
    FPSCLOCK.tick(15)
    DISPLAYSURF.blit(pygame.image.load('graphics/Earth 4.png'), (0, 0))
    pygame.display.update()
    FPSCLOCK.tick(1)
    if score != 0:
        DISPLAYSURF.blit(pygame.image.load('graphics/Earth 5.png'), (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(1.5)
        for x in "aaaaaaaaaaaaaaaaaaaa":
            DISPLAYSURF.blit(pygame.image.load('graphics/Earth 6.png'), (0, 0))
            pygame.display.update()
            FPSCLOCK.tick(20)
            DISPLAYSURF.blit(pygame.image.load('graphics/Earth 7.png'), (0, 0))
            pygame.display.update()
            FPSCLOCK.tick(20)
    else:
        DISPLAYSURF.blit(pygame.image.load('graphics/Earth 8.png'), (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(15)
        DISPLAYSURF.blit(pygame.image.load('graphics/Earth 9.png'), (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(0.7)
    terminate()

def move(vel_X, Drill_X, moveLeft, moveRight, drill):
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key in (K_a, K_LEFT):
                moveRight = False
                moveLeft = True
            elif event.key in (K_d, K_RIGHT):
                moveLeft = False
                moveRight = True
        elif event.type == KEYUP:
            if event.key in (K_a, K_LEFT):
                moveLeft = False
            elif event.key in (K_d, K_RIGHT):
                moveRight = False
    drill = pygame.image.load('graphics/drill.png').convert_alpha()
    if moveLeft == True:
        vel_X -= 0.8
        drill = pygame.image.load('graphics/drillleft.png').convert_alpha()
    if moveRight == True:
        drill = pygame.image.load('graphics/drillright.png').convert_alpha()
        vel_X += 0.8
    vel_X = vel_X * 0.96
    Drill_X += vel_X
    if Drill_X <= 0:
        Drill_X = 0
        vel_X = 0
    elif Drill_X >= 1403:
        Drill_X = 1403
        vel_X = 0
    return(vel_X, Drill_X, moveLeft, moveRight, drill)

def main(vel_X, Drill_X, moveLeft, moveRight, scroll, drill, score):
    vel_X, Drill_X, moveLeft, moveRight, drill = move(vel_X, Drill_X, moveLeft, moveRight, drill)
    scroll += 12
    if scroll >= 0:
        scroll = scroll - 760
    drill_rect = drill.get_rect(topleft=(Drill_X, 50))
    DISPLAYSURF.blit(ground, (0, 0 - scroll))
    DISPLAYSURF.blit(ground, (0, -760 - scroll))
    score = Enemy.frame(enemy1, enemy1.x, enemy1.y, enemy1.dir, enemy1.speed, enemy1.enemy_rect, score, done_)
    score = Enemy.frame(enemy2, enemy2.x, enemy2.y, enemy2.dir, enemy2.speed, enemy2.enemy_rect, score, done_)
    score = Enemy.frame(enemy3, enemy3.x, enemy3.y, enemy3.dir, enemy3.speed, enemy3.enemy_rect, score, done_)
    DISPLAYSURF.blit(drill, drill_rect)
    return(vel_X, Drill_X, moveLeft, moveRight, scroll, drill, score)

while True:
    if __name__ == '__main__':
        (vel_X, Drill_X, moveLeft, moveRight, scroll, drill, score) = main(vel_X, Drill_X, moveLeft, moveRight, scroll, drill, score)
        Timer -= (1 / 60)
        if Timer < 0:
            done_ = 1
            done()
        if score <= 0:
            done_ = 1
            done()
        test_font = pygame.font.Font('graphics/pixeltype.ttf', 50)
        text = test_font.render('Drill Health:' + str(score), False, "black").convert()
        text_rect = text.get_rect(topleft=(8, 53))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render('Drill Health:' + str(score), False, "black").convert()
        text_rect = text.get_rect(topleft=(12, 57))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render('Drill Health:' + str(score), False, "black").convert()
        text_rect = text.get_rect(topleft=(12, 53))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render('Drill Health:' + str(score), False, "black").convert()
        text_rect = text.get_rect(topleft=(8, 57))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render('Drill Health:' + str(score), False, "white").convert()
        text_rect = text.get_rect(topleft=(10, 55))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render("Distance to the Earth's core:" + str(int(Timer * 165)) + 'KM', False,"black").convert()
        text_rect = text.get_rect(topleft=(8, 3))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render("Distance to the Earth's core:" + str(int(Timer * 165)) + 'KM', False, "black").convert()
        text_rect = text.get_rect(topleft=(12, 7))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render("Distance to the Earth's core:" + str(int(Timer * 165)) + 'KM', False, "black").convert()
        text_rect = text.get_rect(topleft=(8, 7))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render("Distance to the Earth's core:" + str(int(Timer * 165)) + 'KM', False, "black").convert()
        text_rect = text.get_rect(topleft=(12, 3))
        DISPLAYSURF.blit(text, text_rect)
        text = test_font.render("Distance to the Earth's core:" + str(int(Timer * 165)) + 'KM', False, "white").convert()
        text_rect = text.get_rect(topleft=(10, 5))
        DISPLAYSURF.blit(text, text_rect)
        if Timer >= 31:
            test_font = pygame.font.Font('graphics/pixeltype.ttf', 70)
            text = test_font.render("Destroy your drill before you reach the Earth's core", False,"black").convert()
            text_rect = text.get_rect(center=(748, 353))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("Destroy your drill before you reach the Earth's core", False, "black").convert()
            text_rect = text.get_rect(center=(752, 357))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("Destroy your drill before you reach the Earth's core", False, "black").convert()
            text_rect = text.get_rect(center=(748, 357))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("Destroy your drill before you reach the Earth's core", False, "black").convert()
            text_rect = text.get_rect(center=(752, 353))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("Destroy your drill before you reach the Earth's core", False,"white").convert()
            text_rect = text.get_rect(center=(750, 355))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("by crashing into other drills using a/d keys!", False, "black").convert()
            text_rect = text.get_rect(center=(748, 403))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("by crashing into other drills using a/d keys!", False, "black").convert()
            text_rect = text.get_rect(center=(752, 407))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("by crashing into other drills using a/d keys!", False, "black").convert()
            text_rect = text.get_rect(center=(748, 407))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("by crashing into other drills using a/d keys!", False, "black").convert()
            text_rect = text.get_rect(center=(752, 403))
            DISPLAYSURF.blit(text, text_rect)
            text = test_font.render("by crashing into other drills using a/d keys!", False,"white").convert()
            text_rect = text.get_rect(center=(750, 405))
            DISPLAYSURF.blit(text, text_rect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)