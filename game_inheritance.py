from random import randint as ri
import pgzrun

WIDTH = 800
HEIGHT = 500

# all the class logic

class Player(Actor):
    
    # override the default constructor
    def __init__(self, image,speed = 5):
        pos = ri(0, WIDTH), ri(0, HEIGHT)  # generate the random x, y co-ordinate
        super().__init__(image, pos)  # call the parent class constructor and pass image and pos
        self.speed = speed  # add a new instance variable


    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
            self.angle = +5
        elif keyboard.D:
            self.x += self.speed
            self.angle = -5
        elif keyboard.E:
            self.x += self.speed
            self.y -= self.speed
        else:
            self.angle = 0
    
    def check_boundary(self):
        if p.x < 0: # agar player left side se ja rha hai
            p.x = WIDTH # to right side se dikhne lge
        if p.x > WIDTH: # vice versa
            p.x = 0
        if p.y < 0:
            p.y = HEIGHT
        if p.y > HEIGHT:
            p.y = 0


# main game code

p = Player('ironman')
print(dir(p))

def draw():
    screen.fill('black')
    screen.blit('wall', (0, 0))
    p.draw()

def update():
    p.move()
    p.check_boundary()

pgzrun.go()