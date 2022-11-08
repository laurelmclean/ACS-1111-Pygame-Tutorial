# import and init pygame
import pygame
pygame.init()

# configure the screen and set width and height dimensions as a tuple
screen = pygame.display.set_mode([500, 500])

# Create game loop
running = True
while running:
	# Looks at events - if game quits
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Clear the screen
	screen.fill((255, 255, 255))
	# Draw a circle
    # Colors are expressed with three values representing their Red, Green, and Blue components
    # Each component can have a value of 0 to 255.
	color = (255, 0, 0)
    # top left corner is 0,0
	position = (100, 100)
    # draws a circle filled with the color, at the position, with a radius of 75 pixels.
	pygame.draw.circle(screen, color, position, 75)
	# Update the display
	pygame.display.flip()
