import pygame
from pygame import mixer
import random

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load("begr.png")

def backgroundimage():
    screen.blit(background, (0, 0))

# title
pygame.display.set_caption("Space Gangster")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Intro
Intro = pygame.font.Font("freesansbold.ttf", 100)
textX = 250
textY = 250
enter = pygame.font.Font("freesansbold.ttf", 50)
enterX = 250
enterY = 400

# player
player = pygame.image.load("player.png")
playerX = 600
playerY = 600
playerX_change = 0

# Enemy
no_of_enemy = 8
enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(no_of_enemy):
    enemy.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(20, 1280))
    enemyY.append(random.randint(80, 400))
    enemyX_change.append(15)
    enemyY_change.append(15)

# bullet
bullet = pygame.image.load("bullet.png")
bulletX = 616
bulletY = 600
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def bulletImage(playerX, playerY):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (playerX, playerY))


def enemyImage(enemyX, enemyY, i):
    screen.blit(enemy[i], (enemyX, enemyY))

def playerImage(playerX, playerY):
    screen.blit(player, (playerX, playerY))

def IntroText():
    Intro_text = Intro.render("Space Gangster", True, (255, 255, 255))
    enter_text = enter.render("    W to Play      Q to Quite", True, (255, 255, 255))
    screen.blit(Intro_text, (textX, textY))
    screen.blit(enter_text, (enterX, enterY))

# Gameloop
running = True
n = 0
while running:
    screen.fill((0, 0, 0))
    backgroundimage()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_LEFT:
                playerX_change = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()

                    bulletImage(bulletX, bulletY)


    # player boundaries
    playerX += playerX_change
    if playerX >= 1200:
        playerX = 1200
    if playerX <= 20:
        playerX = 20

    # Enemy Boundaries

    for i in range(no_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 20:
            enemyX_change[i] = 7
            enemyY[i] += enemyY_change[i]

        elif enemyY[i] >= 1200:
            enemyX_change[i] = -7
            enemyY[i] += enemyY_change[i]


    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bulletImage(bulletX, bulletY)
        bulletY -= bulletY_change


        enemyImage(enemyX[i], enemyY[i], i)

    playerImage(playerX, playerY)
    pygame.display.update()

