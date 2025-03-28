import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

drawing = False
last_pos = None
color = (0, 0, 255)
radius = 5
mode = "free"
eraser = False

screen.fill((255, 255, 255))

font = pygame.font.SysFont("Verdana", 18)

palette_colors = [
    (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (255, 192, 203), (128, 0, 128)
]
palette_rects = []
for i, c in enumerate(palette_colors):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, c))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for rect, c in palette_rects:
                if rect.collidepoint(pos):
                    color = c
                    eraser = False
            if pos[1] > 50:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
            if event.button == 4:
                radius = min(100, radius + 1)
            if event.button == 5:
                radius = max(1, radius - 1)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if mode == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    top_left = (min(x1, x2), min(y1, y2))
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    rect = pygame.Rect(top_left, (width, height))
                    pygame.draw.rect(screen, (255, 255, 255) if eraser else color, rect, 0)
                elif mode == "circle":
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius_circ = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(screen, (255, 255, 255) if eraser else color, center, radius_circ, 0)
                drawing = False
                last_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                eraser = True
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_v:
                mode = "rect"
            elif event.key == pygame.K_f:
                mode = "free"

    if drawing and mode == "free":
        mouse_pos = pygame.mouse.get_pos()
        if last_pos is not None:
            pygame.draw.line(screen, (255, 255, 255) if eraser else color, last_pos, mouse_pos, radius)
        last_pos = mouse_pos

    for rect, c in palette_rects:
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    pygame.draw.rect(screen, (200, 200, 200), (0, HEIGHT - 60, WIDTH, 60))
    info_text = f"Mode: {mode.upper()} | Color: {'Eraser' if eraser else color} | Brush: {radius}px"
    controls_text = "E: Eraser  F: Freehand  C: Circle  V: Rectangle  Scroll: Brush Size"
    screen.blit(font.render(info_text, True, (0, 0, 0)), (10, HEIGHT - 55))
    screen.blit(font.render(controls_text, True, (0, 0, 0)), (10, HEIGHT - 30))

    pygame.display.update()
    clock.tick(60)
