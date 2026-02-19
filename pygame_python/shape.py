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
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# --------------- Button Class ---------------
class Button:
    def __init__(self, text, x, y, w, h, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        label = FONT.render(self.text, True, BLACK)
        screen.blit(label, (self.rect.centerx - label.get_width()//2,
                            self.rect.centery - label.get_height()//2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

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

# --------------- Game Functions ---------------
def play_game():
    colors = [
        ((255, 0, 0), "Red"),
        ((0, 255, 0), "Green"),
        ((0, 0, 255), "Blue"),
    ]
    boxes = [ColorBox(color, name) for color, name in colors]

    score = 0
    start_time = time.time()
    game_duration = 30
    last_move_time = 0
    move_interval = 3
    clock = pygame.time.Clock()
    message = ""
    running = True

    while running:
        screen.fill(WHITE)
        current_time = time.time()
        elapsed = int(current_time - start_time)
        remaining_time = game_duration - elapsed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for box in boxes:
                    if box.is_clicked(pos):
                        score += 1
                        message = f"You clicked: {box.name}!"
                        box.move_random()

        # Move boxes automatically every interval
        if current_time - last_move_time > move_interval:
            for box in boxes:
                box.move_random()
            last_move_time = current_time

        # Draw boxes
        for box in boxes:
            box.draw()

        # Draw score and timer
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        timer_text = FONT.render(f"Time Left: {remaining_time}s", True, BLACK)
        screen.blit(score_text, (20, 10))
        screen.blit(timer_text, (WIDTH - 180, 10))

        # Show message
        if message:
            msg = FONT.render(message, True, BLACK)
            screen.blit(msg, (WIDTH//2 - 100, HEIGHT - 40))

        # Game Over Screen
        if remaining_time <= 0:
            return game_over_screen(score)

        pygame.display.flip()
        clock.tick(30)

def game_over_screen(score):
    clock = pygame.time.Clock()
    restart_button = Button("Restart", WIDTH//2 - 80, HEIGHT//2, 150, 40, "restart")
    menu_button = Button("Main Menu", WIDTH//2 - 80, HEIGHT//2 + 60, 150, 40, "menu")

    while True:
        screen.fill(WHITE)
        end_msg = BIG_FONT.render("Time's Up!", True, BLACK)
        score_msg = FONT.render(f"Your Score: {score}", True, BLACK)
        screen.blit(end_msg, (WIDTH//2 - 80, HEIGHT//2 - 80))
        screen.blit(score_msg, (WIDTH//2 - 80, HEIGHT//2 - 40))

        restart_button.draw()
        menu_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if restart_button.is_clicked(pos):
                    return "restart"
                if menu_button.is_clicked(pos):
                    return "menu"

        pygame.display.flip()
        clock.tick(30)

def main_menu():
    clock = pygame.time.Clock()
    start_button = Button("Start Game", WIDTH//2 - 80, HEIGHT//2 - 20, 150, 40, "start")
    quit_button = Button("Quit", WIDTH//2 - 80, HEIGHT//2 + 40, 150, 40, "quit")

    while True:
        screen.fill(WHITE)
        title = BIG_FONT.render("Color Clicker Challenge", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))

        start_button.draw()
        quit_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if start_button.is_clicked(pos):
                    return "start"
                if quit_button.is_clicked(pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

# --------------- Game Flow ---------------
while True:
    menu_choice = main_menu()
    if menu_choice == "start":
        result = play_game()
        if result == "restart":
            play_game()
        elif result == "menu":
            continue
