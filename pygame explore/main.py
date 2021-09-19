import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()  # it initialize all the pygame modules

# create a screen
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))  # must write height and width in parenthesis

# Background
background = pygame.image.load('begr.png')  # icon of the game

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Space Invader")  # title of the game
icon = pygame.image.load('ufo1.png')  # icon of the game
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("noname1.png")
# here we have set the position of the player
playerX = 550
playerY = 530
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("noname.png"))
    enemyX.append(random.randint(0, 720))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("bullet1.png")
# here we have set the position of the player
bulletX = 0
bulletY = 530
bulletX_change = 0
bulletY_change = 25
bullets_state = "ready"
# Ready - You can't see the bullet on the screen
# Fire - The bullet is directly moving

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 100)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (360, 180))


def showscore(x, y):
    score1 = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score1, (x, y))

def player(x, y):
    screen.blit(playerImg, (y, x))  # blit means to draw image on screen


def enemy(x, y, i):
    screen.blit(enemyImg[i], (y, x))

def bulletfire (x, y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bulletImg, (x + 76, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow((enemyY - bulletY), 2))
    if distance < 27:
        return True
    else:
        return False



# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))  # Here these are the values of RGB i.e., Red, Green and Blue between 0 - 256
    # now here it not showing after running because we have not updated so after do anything we have to
    # apply pygame.display.update()
    # now you game window update at last we have update it
# background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # this is to close window that is to quite game
            running = False

        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # print("A keystroke pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -10
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullets_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # get the current x coordinate of the spaceship
                    bulletX = playerX
                    bulletfire(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0


 #   player boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1080:
        playerX = 1080

#   enemy boundaries
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 1200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 7
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1080:
            enemyX_change[i] = -7
            enemyY[i] += enemyY_change[i]

            #   collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 530
            bullets_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 1280)
            enemyY[i] = random.randint(10, 200)
        enemy(enemyY[i], enemyX[i], i)

#   bullet movement
    if bulletY <= 0:
        bulletY = 530
        bullets_state = "ready"

    if bullets_state == "fire":
            bulletfire(bulletX, bulletY)
            bulletY -= bulletY_change

    showscore(textX, textY)
    player(playerY, playerX)
    pygame.display.update()
