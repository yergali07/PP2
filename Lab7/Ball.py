import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Move the Red Ball')

ball_radius = 25
ball_x, ball_y = width // 2, height // 2
ball_color = (255, 0, 0)
move_step = 5

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= move_step
    if keys[pygame.K_DOWN] and ball_y + ball_radius < height:
        ball_y += move_step
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= move_step
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < width:
        ball_x += move_step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()