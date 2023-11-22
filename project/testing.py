import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
FPS = 60
GROUND_HEIGHT = 50
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 30, 30
GRAVITY = 1
JUMP_HEIGHT = -15

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector-like Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load images
player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill(WHITE)

obstacle_image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle_image.fill(RED)

# Game variables
player_x = 50
player_y = HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
player_velocity_y = 0

obstacle_list = []

# Functions
def draw_ground():
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

def draw_player(x, y):
    screen.blit(player_image, (x, y))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)

def generate_obstacle():
    obstacle_x = WIDTH
    obstacle_y = HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT
    obstacle_list.append((obstacle_x, obstacle_y))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT:
                player_velocity_y = JUMP_HEIGHT

    # Update player position
    player_y += player_velocity_y
    player_velocity_y += GRAVITY

    # Keep the player above the ground
    if player_y > HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT:
        player_y = HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
        player_velocity_y = 0

    # Generate obstacles
    if random.randint(0, 100) < 5:
        generate_obstacle()

    # Update obstacle positions
    for i in range(len(obstacle_list)):
        obstacle_list[i] = (obstacle_list[i][0] - 5, obstacle_list[i][1])

    # Remove obstacles that are off-screen
    obstacle_list = [(x, y) for x, y in obstacle_list if x > -OBSTACLE_WIDTH]

    # Check for collisions
    for obstacle in obstacle_list:
        if (
            player_x < obstacle[0] + OBSTACLE_WIDTH
            and player_x + PLAYER_WIDTH > obstacle[0]
            and player_y < obstacle[1] + OBSTACLE_HEIGHT
            and player_y + PLAYER_HEIGHT > obstacle[1]
        ):
            # Game over
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill((0, 0, 0))
    draw_ground()
    draw_player(player_x, player_y)
    draw_obstacles(obstacle_list)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
 