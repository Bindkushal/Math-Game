import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fill the Box")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Box dimensions
BOX_WIDTH = 100
BOX_HEIGHT = 50
MARGIN = 20

# Create a list to store the boxes and their states (filled or not)
boxes = []
for i in range(10):
    x = MARGIN + (i % 5) * (BOX_WIDTH + MARGIN)
    y = MARGIN + (i // 5) * (BOX_HEIGHT + MARGIN)
    rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
    boxes.append((rect, False))  # (rect, filled)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a box is clicked
            mouse_pos = pygame.mouse.get_pos()
            for i, (rect, filled) in enumerate(boxes):
                if rect.collidepoint(mouse_pos):
                    # Toggle the filled state
                    boxes[i] = (rect, not filled)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the boxes
    for rect, filled in boxes:
        color = RED if filled else BLACK
        pygame.draw.rect(screen, color, rect, 2 if not filled else 0)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()