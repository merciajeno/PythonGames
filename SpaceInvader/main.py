import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
background_img = pygame.image.load("space.jpg")
background_img = pygame.transform.scale(background_img, (800, 600))

running = True # Use a variable so you can exit the loop
while running:
    # Check for events (like clicking the 'X' to close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background_img, (0, 0))

    # Refresh the screen so the drawing becomes visible
    pygame.display.update()

pygame.quit() # Cleanly close everything
