import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PALETTE_COLORS = [
    (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (255, 192, 203), (128, 0, 128)
]

# Initial settings
drawing = False
last_pos = None
color = (0, 0, 255)
radius = 5
mode = "free"

# Fill background
screen.fill(WHITE)

# Font
font = pygame.font.SysFont("Verdana", 18)

# Palette setup
palette_rects = []
for i, c in enumerate(PALETTE_COLORS):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    palette_rects.append((rect, c))

# Button setup
buttons = []
button_names = ["free", "eraser", "rect", "circle", "r_triangle", "e_triangle", "rhombus"]
for i, name in enumerate(button_names):
    rect = pygame.Rect(10 + i * 50, HEIGHT - 50, 40, 40)
    buttons.append({"name": name, "rect": rect})

# Draw all buttons and palette
def draw_ui():
    # Clear UI area
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - 90, WIDTH, 90))
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 50))

    # Draw palette
    for rect, c in palette_rects:
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw shape buttons
    for b in buttons:
        pygame.draw.rect(screen, (200, 200, 200), b["rect"])
        pygame.draw.rect(screen, BLACK, b["rect"], 2)
        cx, cy = b["rect"].center
        if b["name"] == "free":
            pygame.draw.line(screen, BLACK, (cx - 10, cy - 5), (cx, cy + 5), 2)
            pygame.draw.line(screen, BLACK, (cx, cy + 5), (cx + 10, cy - 5), 2)
        elif b["name"] == "eraser":
            pygame.draw.rect(screen, BLACK, (cx - 10, cy - 10, 20, 20))
        elif b["name"] == "rect":
            pygame.draw.rect(screen, BLACK, (cx - 10, cy - 10, 20, 20), 2)
        elif b["name"] == "circle":
            pygame.draw.circle(screen, BLACK, (cx, cy), 10, 2)
        elif b["name"] == "r_triangle":
            pygame.draw.polygon(screen, BLACK, [(cx - 10, cy + 10), (cx - 10, cy - 10), (cx + 10, cy + 10)], 2)
        elif b["name"] == "e_triangle":
            pygame.draw.polygon(screen, BLACK, [(cx, cy - 10), (cx - 10, cy + 10), (cx + 10, cy + 10)], 2)
        elif b["name"] == "rhombus":
            pygame.draw.polygon(screen, BLACK, [(cx, cy - 10), (cx - 10, cy), (cx, cy + 10), (cx + 10, cy)], 2)

    # Draw mode and brush size
    info_text = f"Mode: {mode.upper()} | Brush: {radius}px"
    text_surface = font.render(info_text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 80))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for rect, c in palette_rects:
                if rect.collidepoint(pos):
                    color = c
                    if mode == "eraser":
                        mode = "free"
            for b in buttons:
                if b["rect"].collidepoint(pos):
                    mode = b["name"]
            if pos[1] > 50 and pos[1] < HEIGHT - 60:
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
                draw_color = WHITE if mode == "eraser" else color
                if mode == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    top_left = (min(x1, x2), min(y1, y2))
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    pygame.draw.rect(screen, draw_color, (top_left, (width, height)))
                elif mode == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    radius_circ = max(abs(x2 - x1) // 2, abs(y2 - y1) // 2)
                    pygame.draw.circle(screen, draw_color, center, radius_circ)
                elif mode == "r_triangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    points = [(x1, y2), (x1, y1), (x2, y2)]
                    pygame.draw.polygon(screen, draw_color, points)
                elif mode == "e_triangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    top = ((x1 + x2) // 2, min(y1, y2))
                    left = (min(x1, x2), max(y1, y2))
                    right = (max(x1, x2), max(y1, y2))
                    points = [top, left, right]
                    pygame.draw.polygon(screen, draw_color, points)
                elif mode == "rhombus":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    points = [(cx, y1), (x1, cy), (cx, y2), (x2, cy)]
                    pygame.draw.polygon(screen, draw_color, points)
                drawing = False
                last_pos = None

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "free" or mode == "eraser":
                draw_color = WHITE if mode == "eraser" else color
                pygame.draw.line(screen, draw_color, last_pos, event.pos, radius)
                last_pos = event.pos

    draw_ui()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
