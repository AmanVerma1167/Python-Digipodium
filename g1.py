import pgzrun

WIDTH = 500
HEIGHT = 400

p = Actor("ironman", (200,200))

def draw(): # you are difining a function draw
    screen.fill('black')
    p.draw()

def update():
    if keyboard.A:
        p.x -= 2
        p.angle = 10
    elif keyboard.D:
        p.x += 2
        p.angle = -10
    elif keyboard.W:
        p.y -= 2
    elif keyboard.S:
        p.y += 2

pgzrun.go()