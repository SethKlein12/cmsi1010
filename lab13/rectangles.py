import sys
import pygame

# Always begin with initialization, sizing, and captioning
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Just a Simple Rectangle')

# Not strictly necessary, but good practice for readability
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(WHITE)  # "Clear the screen" with white
    the_rectangle = (300, 225, 200, 150)  # (x, y, width, height)
    pygame.draw.rect(screen, RED, the_rectangle)  # filled
    pygame.draw.rect(screen, BLACK, the_rectangle, 3)  # outlined
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene then wait for the QUIT event to come in, which
# happens when the user closes the window
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()