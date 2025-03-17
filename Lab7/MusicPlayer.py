import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "Lab7/music/"
COVERS_FOLDER = "Lab7/covers/"
playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_track = 0 if playlist else None

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)

icon_size = (50, 50)
play_img = pygame.transform.scale(pygame.image.load("Lab7/images/play.png"), icon_size)
pause_img = pygame.transform.scale(pygame.image.load("Lab7/images/pause.png"), icon_size)
stop_img = pygame.transform.scale(pygame.image.load("Lab7/images/stop.png"), icon_size)
next_img = pygame.transform.scale(pygame.image.load("Lab7/images/next.png"), icon_size)
prev_img = pygame.transform.scale(pygame.image.load("Lab7/images/prev.png"), icon_size)

button_y = HEIGHT - 100
play_rect = play_img.get_rect(center=(WIDTH // 2 - 50, button_y))
pause_rect = pause_img.get_rect(center=(WIDTH // 2 - 50, button_y))
stop_rect = stop_img.get_rect(center=(WIDTH // 2 + 50, button_y))
next_rect = next_img.get_rect(center=(WIDTH // 2 + 150, button_y))
prev_rect = prev_img.get_rect(center=(WIDTH // 2 - 150, button_y))

cover_img = None
def load_cover():
    global cover_img
    if current_track is not None:
        song_name = os.path.splitext(playlist[current_track])[0]
        cover_path = os.path.join(COVERS_FOLDER, f"{song_name}.jpg")
        if os.path.exists(cover_path):
            cover_img = pygame.transform.scale(pygame.image.load(cover_path), (200, 200))
        else:
            cover_img = None

load_cover()

def play_music():
    if current_track is not None:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
        pygame.mixer.music.play()
        load_cover()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    if current_track is not None:
        current_track = (current_track + 1) % len(playlist)
        play_music()

def prev_track():
    global current_track
    if current_track is not None:
        current_track = (current_track - 1) % len(playlist)
        play_music()

def get_progress():
    if pygame.mixer.music.get_busy():
        return pygame.mixer.music.get_pos() / 1000
    return 0

if current_track is not None:
    play_music()

running = True
paused = False
while running:
    screen.fill((255, 255, 255))

    if cover_img:
        screen.blit(cover_img, (WIDTH // 2 - 100, 125))
    
    if current_track is not None:
        song_name = playlist[current_track]
    else:
        song_name = "No songs available"
    text_surface = font.render(f"Now Playing: {song_name}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)
    
    progress = get_progress()
    progress_bar_x = WIDTH // 4
    progress_bar_width = WIDTH // 2
    pygame.draw.rect(screen, (200, 200, 200), (progress_bar_x, 400, progress_bar_width, 10))
    pygame.draw.rect(screen, (0, 255, 0), (progress_bar_x, 400, int((progress / 180) * progress_bar_width), 10))
    
    screen.blit(prev_img, prev_rect)
    if paused:
        screen.blit(play_img, play_rect)
    else:
        screen.blit(pause_img, pause_rect)
    screen.blit(stop_img, stop_rect)
    screen.blit(next_img, next_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
            elif event.key == pygame.K_s:
                stop_music()
                paused = False
            elif event.key == pygame.K_n:
                next_track()
                paused = False
            elif event.key == pygame.K_p:
                prev_track()
                paused = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if prev_rect.collidepoint(event.pos):
                prev_track()
                paused = False
            elif play_rect.collidepoint(event.pos) and paused:
                pygame.mixer.music.unpause()
                paused = False
            elif pause_rect.collidepoint(event.pos) and not paused:
                pygame.mixer.music.pause()
                paused = True
            elif stop_rect.collidepoint(event.pos):
                stop_music()
                paused = False
            elif next_rect.collidepoint(event.pos):
                next_track()
                paused = False
    
    pygame.display.update()

pygame.quit()
