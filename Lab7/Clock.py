import pygame
import time
import os

pygame.init()

width, height = 800, 600
center = (width // 2, height // 2)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mickey Clock')

bg = pygame.image.load(os.path.join('Lab7', 'images', 'clock.png'))
bg = pygame.transform.scale(bg, (width, height))
min_hand = pygame.image.load(os.path.join('Lab7', 'images', 'min_hand.png'))
min_hand = pygame.transform.scale(min_hand, (width, height))
sec_hand = pygame.image.load(os.path.join('Lab7', 'images', 'sec_hand.png'))
sec_hand = pygame.transform.scale(sec_hand, (width, height))

bg_rect = bg.get_rect(center=center)
min_hand_rect = min_hand.get_rect(center=center)
sec_hand_rect = sec_hand.get_rect(center=center)

def rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = -6 * minutes - 48
    sec_angle = -6 * seconds + 60

    min_hand_rotated, min_hand_new_rect = rotate(min_hand, min_angle, center)
    sec_hand_rotated, sec_hand_new_rect = rotate(sec_hand, sec_angle, center)

    screen.blit(min_hand_rotated, min_hand_new_rect)
    screen.blit(sec_hand_rotated, sec_hand_new_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()