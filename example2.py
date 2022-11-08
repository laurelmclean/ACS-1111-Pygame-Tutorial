# Import and initialize pygame
from random import randint, choice
import pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

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
        # Here the Apple chooses a random value from the lanes List when it needs an x position.
        self.x = choice(lanes)
        self.y = -64

# strawberry moves horizontally rather than veritcally


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice(lanes)


# Make an instance of image
apple = Apple()

# strawberry
strawberry = Strawberry()


class Player(GameObject):
    # A Player instance will inherit the x and y attributes and the render method.
  def __init__(self):
      super(Player, self).__init__(0, 0, 'player.png')
      # Player adds the dx and dy attributes.
      self.dx = 0
      self.dy = 0
      self.pos_x = 1
      self.pos_y = 1
      self.reset()

  def left(self):
      if self.pos_x > 0:
        self.pos_x -= 1
        self.update_dx_dy()


  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()


  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()


  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

# Player implements the move() method. This method updates the player's position in each frame.
# slow down player as it approaches target
  def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

# Player implements the reset() method which will move it to centre lanes
# self.pos_x is the index of the horizontal position in the lanes List! self.pos_y is the index of the vertical position in the lanes List.
  def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

  def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]


# make an instance of Player
player = Player()

# Group is a class that manages a collection of Sprites.
# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)

# Creat the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

# Clear screen
    screen.fill((255, 255, 255))
# Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)
# Update the window
    pygame.display.flip()
    # tick the clock!
    # saying the next update should be applied in 1/30th of a second.
    clock.tick(60)
