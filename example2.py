# Example 2

# Import and initialize pygame
from random import randint
import pygame
pygame.init()


# Get the clock
clock = pygame.time.Clock()

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

# class extends GameObject
# generates random number for x position and always starts a y 0
class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset()  # call reset here!

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the apple
   if self.y > 500:
     self.reset()

 # add a new method
#  move an Apple back to the top of the screen after moving off the bottom and give it a new random x.
 def reset(self):
   self.x = randint(50, 400)
   self.y = -64

# Make an instance of image
apple = Apple()

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
  # update position of object each frame
  # You can control the speed of an object by how many pixels it moves in each frame.
  # Draw apple
  apple.move()
  apple.render(screen)
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()
  # tick the clock!
  # saying the next update should be applied in 1/30th of a second.
  clock.tick(60)  

  
