import pygame, sys, random, psycopg2
from config import load_config

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

# PostgreSQL functions
def get_or_create_user(username):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
            user_id = cur.fetchone()[0]
            conn.commit()
            return user_id

def get_user_progress(user_id):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1;", (user_id,))
            result = cur.fetchone()
            return result if result else (0, 1)

def save_score(user_id, score, level):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s);", (user_id, score, level))
            conn.commit()

# Wall generator
def generate_walls(level):
    walls = []
    for x in range(GRID_WIDTH):
        walls.append((x, 0))
        walls.append((x, GRID_HEIGHT - 1))
    for y in range(GRID_HEIGHT):
        walls.append((0, y))
        walls.append((GRID_WIDTH - 1, y))
    if level >= 2:
        for x in range(5, 15):
            walls.append((x, 10))
    if level >= 3:
        for y in range(5, 15):
            walls.append((10, y))
    return walls

# Generate food
def generate_food(snake, walls):
    while True:
        pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
        if pos not in snake and pos not in walls:
            weight = random.choice([1, 2, 3])
            timer = random.randint(3000, 7000)
            return {"position": pos, "weight": weight, "timer": timer, "spawn_time": pygame.time.get_ticks()}

# Draw all game objects
def draw_game(snake, food, score, level, walls):
    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0] * CELL_SIZE, block[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    color = RED if food["weight"] == 1 else YELLOW if food["weight"] == 2 else WHITE
    pygame.draw.rect(screen, color, (food["position"][0] * CELL_SIZE, food["position"][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (SCREEN_WIDTH - 120, 10))
    remaining_time = max(0, (food["timer"] - (pygame.time.get_ticks() - food["spawn_time"])) // 1000)
    screen.blit(font.render(f"Food Timer: {remaining_time}s", True, WHITE), (SCREEN_WIDTH // 2 - 80, 10))
    pygame.display.update()

# Reset game state
def reset_game(level):
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)
    walls = generate_walls(level)
    food = generate_food(snake, walls)
    return snake, direction, food, 0, level, walls

# Main game loop
def game_loop():
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    score, level = get_user_progress(user_id)

    snake, direction, food, score, level, walls = reset_game(level)
    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        clock.tick(FPS_BASE + (level - 1) * 3)
        next_direction = direction
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, score, level)
                pygame.quit()
                sys.exit()
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
                    elif event.key == pygame.K_p:
                        save_score(user_id, score, level)
                        paused = True
                        # Calculate the width and height of the "Game Paused" text
                        paused_text = big_font.render("Game Paused", True, YELLOW)
                        paused_text_width, paused_text_height = big_font.size("Game Paused")
                        # Center the text
                        screen.blit(paused_text, ((SCREEN_WIDTH - paused_text_width) // 2, SCREEN_HEIGHT // 2 - paused_text_height // 2))
                        pygame.display.update()
                        while paused:
                            for e in pygame.event.get():
                                if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                                    paused = False

                else:
                    if event.key == pygame.K_r:
                        snake, direction, food, score, level, walls = reset_game(1)
                        game_over = False

        if not game_over:
            direction = next_direction
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            if new_head in walls or new_head in snake or not (0 <= new_head[0] < GRID_WIDTH) or not (0 <= new_head[1] < GRID_HEIGHT):
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food["position"]:
                    score += food["weight"]
                    if score >= level * 5:
                        level += 1
                        walls = generate_walls(level)
                    food = generate_food(snake, walls)
                else:
                    snake.pop()

                if current_time - food["spawn_time"] > food["timer"]:
                    food = generate_food(snake, walls)

        draw_game(snake, food, score, level, walls)

        if game_over:
            save_score(user_id, score, level)
            screen.blit(big_font.render("GAME OVER", True, RED), (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 - 40))
            screen.blit(font.render("Press R to Restart", True, WHITE), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 10))
            pygame.display.update()

# Run the game
if __name__ == "__main__":
    game_loop()
