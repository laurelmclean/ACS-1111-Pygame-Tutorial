# Example 2

# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Make a Game Object class that draws a rectangle.
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))


# Make an instance of image
apple = GameObject(120, 300, 'apple.png')

# strawberry
strawberry = GameObject(400, 100, 'strawberry.png')

# Create a new instance of Surface
# Using a surface we display more than just rectangles and circles. A surface can also display image files.
# surf = pygame.Surface((50, 50))
# surf.fill((255, 111, 33))

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill((255, 255, 255))
  # Draw the surface
#   Blitting is the process of copying a block of pixels onto another block of pixels. In this case, you're copying the pixels in the surface onto the pixels of the pygame window.
  # screen.blit(surf, (100, 120))
  # Clear screen
  screen.fill((255, 255, 255))
  # add image
  apple.render(screen)
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()

  
