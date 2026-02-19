import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Polygons")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

# Polygon generator
def regular_polygon(center, radius, sides):
    cx, cy = center
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    return points

# Generate random polygons
def random_polygon():
    x = random.randint(50, WIDTH - 50)    # random x
    y = random.randint(50, HEIGHT - 50)   # random y
    radius = random.randint(20, 60)       # random size
    sides = random.randint(3, 8)          # 3=triangle up to 8=octagon
    color = [random.randint(0, 255) for _ in range(3)]  # random RGB color
    return (color, regular_polygon((x, y), radius, sides))

# Create a list of polygons
polygons = [random_polygon() for _ in range(6)]

running = True
while running:
    screen.fill(WHITE)

    # Draw all polygons
    for color, points in polygons:
        pygame.draw.polygon(screen, color, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
