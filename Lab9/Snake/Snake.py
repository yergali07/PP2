import pygame, sys, random

# Initialize pygame
pygame.init()

# Game settings
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS_BASE = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)

# Walls (borders)
walls = []
for x in range(GRID_WIDTH):
    walls.append((x, 0))
    walls.append((x, GRID_HEIGHT - 1))
for y in range(GRID_HEIGHT):
    walls.append((0, y))
    walls.append((GRID_WIDTH - 1, y))

# Function to generate food at valid positions with weight and timer
def generate_food(snake):
    while True:
        pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
        if pos not in snake and pos not in walls:
            weight = random.choice([1, 2, 3])  # Food weights
            timer = random.randint(3000, 7000)  # Timer in milliseconds
            return {"position": pos, "weight": weight, "timer": timer, "spawn_time": pygame.time.get_ticks()}

# Reset game state
def reset_game():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    food = generate_food(snake)
    score = 0
    level = 1
    return snake, direction, food, score, level

# Draw everything
def draw_game(snake, food, score, level):
    screen.fill(BLACK)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0] * CELL_SIZE, block[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food (color based on weight)
    if food["weight"] == 1:
        color = RED
    elif food["weight"] == 2:
        color = YELLOW
    else:
        color = WHITE

    pygame.draw.rect(screen, color, (food["position"][0] * CELL_SIZE, food["position"][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 120, 10))

    # Draw food timer
    remaining_time = max(0, (food["timer"] - (pygame.time.get_ticks() - food["spawn_time"])) // 1000)
    timer_text = font.render(f"Food Timer: {remaining_time}s", True, WHITE)
    screen.blit(timer_text, (SCREEN_WIDTH // 2 - 80, 10))

    pygame.display.update()

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    snake, direction, food, score, level = reset_game()
    running = True
    game_over = False

    while running:
        clock.tick(FPS_BASE + (level - 1) * 3)  # Speed increases by level
        next_direction = direction
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Input handling
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0, 1):
                        next_direction = (0, -1)
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0, -1):
                        next_direction = (0, 1)
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (1, 0):
                        next_direction = (-1, 0)
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-1, 0):
                        next_direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        # Restart game
                        snake, direction, food, score, level = reset_game()
                        game_over = False

        if not game_over:
            direction = next_direction
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Check collision with wall or itself
            if new_head in walls or new_head in snake:
                game_over = True

            # Check if snake leaves grid
            if not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                # Check collision with food
                if new_head == food["position"]:
                    score += food["weight"]
                    food = generate_food(snake)
                    # Level up every 5 points
                    if score >= level * 5:
                        level += 1
                else:
                    snake.pop()

                # Remove food if timer expired
                if current_time - food["spawn_time"] > food["timer"]:
                    food = generate_food(snake)

        draw_game(snake, food, score, level)

        # Display Game Over
        if game_over:
            game_over_text = big_font.render("GAME OVER", True, RED)
            restart_text = font.render("Press R to Restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 - 40))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))
            pygame.display.update()

# Run game
game_loop()
