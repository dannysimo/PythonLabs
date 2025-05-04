import pygame
import random
import sys


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat's Hate Water")
clock = pygame.time.Clock()

# Sounds
pygame.mixer.init()
pygame.mixer.music.load("Sounds/background_music.mp3")
pygame.mixer.music.play(-1, 0.0)

cat_collision_sound = pygame.mixer.Sound("Sounds/catsound.mp3")
drop_collision_sound = pygame.mixer.Sound("Sounds/watterdrop.mp3")
win_sound = pygame.mixer.Sound("Sounds/win.mp3")
lose_sound = pygame.mixer.Sound("Sounds/lose.mp3")

# Sprites , Texts
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
sprite_sheet = pygame.image.load("Sprites/cat_spritesheet.png").convert_alpha()
background = pygame.image.load("Sprites/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
font = pygame.font.Font("Fonts/8-bit.ttf", 30)

GROUND_Y = HEIGHT - 85
IDLE_ROW = 1
WALK_ROW = 4
ANIMATION_FRAMES = {"idle": 4, "walk": 6}

def load_animation_row(sheet, row, frame_count):
    frames = []
    for col in range(frame_count):
        frame = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT), pygame.SRCALPHA)
        frame.blit(sheet, (0, 0), (col * SPRITE_WIDTH, row * SPRITE_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT))
        frame = pygame.transform.scale(frame, (128, 128))
        frames.append(frame)
    return frames

idle_frames = load_animation_row(sprite_sheet, IDLE_ROW, ANIMATION_FRAMES["idle"])
walk_frames = load_animation_row(sprite_sheet, WALK_ROW, ANIMATION_FRAMES["walk"])

player_pos = [WIDTH // 2, GROUND_Y - 96]
player_speed = 5

frame_index = 0
frame_timer = 0
animation_speed = 6
state = "idle"
previous_state = None
flip_sprite = False

invincible = False
invincible_start_time = 0
invincibility_duration = 2000

# WatterDrops
drop_size = 50
drop_list = []
drop_speed = 5
drop_image = pygame.image.load("Sprites/wdrop.png").convert_alpha()
drop_image = pygame.transform.scale(drop_image, (drop_size, drop_size))

score = 0
lives = 3
start_ticks = pygame.time.get_ticks()
game_duration = 60

def drop_water():
    if len(drop_list) < 10 and random.random() < 0.05:
        x_pos = random.randint(0, WIDTH - drop_size)
        drop_list.append([x_pos, 0])

def draw_drops():
    for drop in drop_list:
        screen.blit(drop_image, (drop[0], drop[1]))

def update_drops():
    global score
    for idx, drop in enumerate(drop_list[:]):
        if drop[1] >= GROUND_Y - drop_size + 30:
            drop_list.remove(drop)
            score += 1
            drop_collision_sound.play()
        else:
            drop[1] += drop_speed

def detect_collision(p1, p2):
    if invincible:
        return False
    player_rect = pygame.Rect(p1[0] + 44, p1[1] + 40, 40, 60)
    drop_rect = pygame.Rect(p2[0], p2[1], drop_size, drop_size)
    return player_rect.colliderect(drop_rect)

# Start Screen
screen.fill((0, 0, 0))
start_text = font.render("Press any key to start", True, (255, 255, 255))
text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(start_text, text_rect)
pygame.display.flip()

waiting_to_start = True
while waiting_to_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            waiting_to_start = False

# Loop 
running = True
game_over = False
start_ticks = pygame.time.get_ticks()

while running:
    screen.blit(background, (0, 0))
    dt = clock.tick(60) / 1000

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, int(game_duration - seconds))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx = 0

    if keys[pygame.K_LEFT]:
        dx = -player_speed
        state = "walk"
        flip_sprite = True
    elif keys[pygame.K_RIGHT]:
        dx = player_speed
        state = "walk"
        flip_sprite = False
    else:
        state = "idle"

    player_pos[0] += dx
    player_pos[0] = max(0, min(WIDTH - 96, player_pos[0]))

    if state != previous_state:
        frame_index = 0
        frame_timer = 0
        previous_state = state

    current_frames = idle_frames if state == "idle" else walk_frames

    frame_timer += animation_speed * dt
    if frame_timer >= 1:
        frame_timer = 0
        frame_index = (frame_index + 1) % len(current_frames)

    current_frame = current_frames[frame_index]
    if flip_sprite:
        current_frame = pygame.transform.flip(current_frame, True, False)

    # IFrames
    if invincible and (pygame.time.get_ticks() // 200) % 2 == 0:
        tinted = current_frame.copy()
        width, height = tinted.get_size()
        for x in range(width):
            for y in range(height):
                r, g, b, a = tinted.get_at((x, y))
                if a > 0:
                    tinted.set_at((x, y), (255, 0, 0, a))
        current_frame = tinted

    drop_water()
    update_drops()
    draw_drops()

    for drop in drop_list[:]:
        if detect_collision(player_pos, drop) and not invincible:
            drop_list.remove(drop)
            lives -= 1
            invincible = True
            invincible_start_time = pygame.time.get_ticks()
            cat_collision_sound.play()
            if lives <= 0:
                game_over = True
                running = False

    if invincible and pygame.time.get_ticks() - invincible_start_time >= invincibility_duration:
        invincible = False

    screen.blit(current_frame, player_pos)
    text = font.render(f"Score: {score}  Lives: {lives}  Time: {time_left}s", True, (255, 255, 255))
    screen.blit(text, (20, HEIGHT - 40))

    if time_left <= 0:
        game_over = True
        running = False

    pygame.display.flip()

# Final
pygame.mixer.music.stop()
pygame.mixer.stop()

if lives > 0:
    win_sound.play()
else:
    lose_sound.play()

screen.fill((0, 0, 0))
end_msg = "You Win!" if lives > 0 else "You Lose!"
label = font.render(end_msg, True, (255, 255, 255))
screen.blit(label, (WIDTH // 2 - 100, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
