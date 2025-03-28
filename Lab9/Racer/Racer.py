import pygame, sys
from pygame.locals import *
import random, time

# Initialize
pygame.init()

# Constants
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
N = 5  # Coins needed to increase speed

# Global Variables
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Setup
FramePerSec = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("Lab9/Racer/images/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab9/Racer/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab9/Racer/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Lab9/Racer/images/Coin.png")
        size = random.randint(20, 40)
        self.weight = random.randint(1, 3)
        self.image = pygame.transform.scale(original_image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.respawn()

    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.randint(1, 3)


def draw_restart_button():
    button_rect = pygame.Rect(130, 350, 140, 50)
    pygame.draw.rect(DISPLAYSURF, (0, 200, 0), button_rect)
    text = font_small.render("Restart", True, WHITE)
    DISPLAYSURF.blit(text, (button_rect.x + 30, button_rect.y + 12))
    return button_rect


def reset_game():
    global SPEED, SCORE, COIN_SCORE, enemies, coins, all_sprites

    SPEED = 5
    SCORE = 0
    COIN_SCORE = 0

    P1 = Player()
    E1 = Enemy()
    coins = pygame.sprite.Group()

    for _ in range(3):
        coin = Coin()
        coins.add(coin)

    enemies = pygame.sprite.Group()
    enemies.add(E1)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(*coins)

    return P1, E1, coins, enemies, all_sprites


def game_loop():
    global SPEED, SCORE, COIN_SCORE

    P1, E1, coins, enemies, all_sprites = reset_game()
    running = True
    game_over_flag = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Handle Restart Button
            if game_over_flag and event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    P1, E1, coins, enemies, all_sprites = reset_game()
                    game_over_flag = False

        if not game_over_flag:
            DISPLAYSURF.blit(background, (0, 0))
            scores = font_small.render(f"Score: {SCORE}", True, BLACK)
            coin_scores = font_small.render(f"Coins: {COIN_SCORE}", True, BLACK)
            DISPLAYSURF.blit(scores, (10, 10))
            DISPLAYSURF.blit(coin_scores, (300, 10))

            # Move & Draw Sprites
            for entity in all_sprites:
                entity.move()
                DISPLAYSURF.blit(entity.image, entity.rect)

            # Collision with Enemy
            if pygame.sprite.spritecollideany(P1, enemies):
                pygame.mixer.Sound('Lab9/Racer/sounds/crash.wav').play()
                time.sleep(1)
                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(font.render("Game Over", True, BLACK), (30, 250))
                restart_button = draw_restart_button()
                pygame.display.update()
                game_over_flag = True
                continue

            # Collision with Coin
            collected = pygame.sprite.spritecollideany(P1, coins)
            if collected:
                COIN_SCORE += collected.weight
                collected.respawn()

                # Increase speed every N coins
                if COIN_SCORE % N == 0:
                    SPEED += 1

        else:
            # Draw Restart button again
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(font.render("Game Over", True, BLACK), (30, 250))
            restart_button = draw_restart_button()

        pygame.display.update()
        FramePerSec.tick(FPS)


# Start Game
game_loop()
