import pygame
import sys
import random
import time

pygame.init()

# --------------- Setup ---------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Clicker Challenge")

FONT = pygame.font.SysFont("Arial", 24)
BIG_FONT = pygame.font.SysFont("Arial", 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --------------- ColorBox Class ---------------

class ColorBox:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.move_random()

    def move_random(self):
        self.rect.x = random.randint(0, WIDTH - 100)
        self.rect.y = random.randint(50, HEIGHT - 120)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# --------------- Create Boxes ---------------
colors = [
    ((255, 0, 0), "Red"),
    ((0, 255, 0), "Green"),
    ((0, 0, 255), "Blue"),
]
boxes = [ColorBox(color, name) for color, name in colors]

# --------------- Game Variables ---------------
score = 0
start_time = time.time()
game_duration = 30  # seconds
last_move_time = 0
move_interval = 3  # seconds

# --------------- Main Game Loop ---------------
clock = pygame.time.Clock()
running = True
message = ""

while running:
    screen.fill(WHITE)
    current_time = time.time()
    elapsed = int(current_time - start_time)
    remaining_time = game_duration - elapsed

    # Quit check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Click check
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for box in boxes:
                if box.is_clicked(pos):
                    score += 1
                    message = f"You clicked: {box.name}!"
                    box.move_random()

    # Random movement every few seconds
    if current_time - last_move_time > move_interval:
        for box in boxes:
            box.move_random()
        last_move_time = current_time

    # Draw boxes
    for box in boxes:
        box.draw()

    # Show score and timer
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    timer_text = FONT.render(f"Time Left: {remaining_time}s", True, BLACK)
    screen.blit(score_text, (20, 10))
    screen.blit(timer_text, (WIDTH - 180, 10))

    # Message
    if message:
        msg = FONT.render(message, True, BLACK)
        screen.blit(msg, (WIDTH//2 - 100, HEIGHT - 40))

    # Game over
    if remaining_time <= 0:
        screen.fill(WHITE)
        end_msg = BIG_FONT.render("Time's Up!", True, BLACK)
        score_msg = FONT.render(f"Your Score: {score}", True, BLACK)
        screen.blit(end_msg, (WIDTH//2 - 80, HEIGHT//2 - 40))
        screen.blit(score_msg, (WIDTH//2 - 80, HEIGHT//2 + 10))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
