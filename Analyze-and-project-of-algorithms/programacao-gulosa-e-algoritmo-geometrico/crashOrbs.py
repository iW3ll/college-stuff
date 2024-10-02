# https://trinket.io/features/pygame

import pygame
import math


WIDTH, HEIGHT = 800, 600
FPS = 15

# Define general class
class Ball:
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity

    def move(self):
        self.x += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def is_colliding(ball1, ball2):
    distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    return distance <= (ball1.radius + ball2.radius)

# init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crash two orb")
clock = pygame.time.Clock()

# Create two balls
ball1 = Ball(100, HEIGHT // 2, 30, (0, 255, 0), 3)  # green orb to right
ball2 = Ball(700, HEIGHT // 2, 30, (155, 155, 255), -3)  

# Loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moving
    ball1.move()
    ball2.move()

    # Verify colision
    if is_colliding(ball1, ball2):
        # Reverse when crash
        ball1.velocity = -ball1.velocity
        ball2.velocity = -ball2.velocity
        ball1.color = (255, 0, 0)  # change color if crash green
        ball2.color = (255, 0, 255)  

    # Draw
    screen.fill((0, 0, 0))  # clean screen
    ball1.draw(screen)
    ball2.draw(screen)

    pygame.display.flip()  # refresh screen
    clock.tick(FPS)

pygame.quit()
