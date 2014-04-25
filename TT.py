from Tkinter import *
from math import sqrt
import time
from BaseGameEntity import *
from Renderer import *
from GamePhysics import CollisionDetection

root = Tk()
cd = CollisionDetection.CollisionTests()
can = Canvas(root, bg="white", width=600, height=600)
renderer = Renderer(can)

circle = [Vec2D(10 * sqrt(3) / 2, 10 * .5), Vec2D(10 * sqrt(2) / 2, 10 * sqrt(2) / 2), Vec2D(10 * .5, 10 * sqrt(3) / 2), Vec2D(0, 10),
                Vec2D(10 * -.5, 10 * sqrt(3) / 2), Vec2D(10 * -sqrt(2) / 2, 10 * sqrt(2) / 2), Vec2D(10 * -sqrt(3) / 2, 10 * .5), Vec2D(-10, 0),
                 Vec2D(10 * -sqrt(3) / 2, 10 * -.5), Vec2D(10 * -sqrt(2) / 2, 10 * -sqrt(2) / 2), Vec2D(10 * -.5, 10 * -sqrt(3) / 2), Vec2D(0, -10),
                  Vec2D(10 * .5, 10 * -sqrt(3) / 2), Vec2D(10 * sqrt(2) / 2, 10 * -sqrt(2) / 2), Vec2D(10 * sqrt(3) / 2, 10 * -.5), Vec2D(10, 0)]
rect_vertices = [Vec2D(-10, -10), Vec2D(-10, 10), Vec2D(10, 10), Vec2D(10, -10)]
cir = BaseGameEntity(circle, pos=Vec2D(100, 100), velocity=Vec2D(230, 150), angularVelocity=1.75)
rect = BaseGameEntity(rect_vertices, pos=Vec2D(500, 500), velocity=Vec2D(-200, -200), angularVelocity=1.75)

renderer.addEntity(cir)
renderer.addEntity(rect)

top = [Vec2D(-5, -5), Vec2D(-5, 5), Vec2D(495, 5), Vec2D(495, -5)]
bot = [Vec2D(-5, -5), Vec2D(-5, 5), Vec2D(495, 5), Vec2D(495, -5)]
left = [Vec2D(-5, -5), Vec2D(-5, 495), Vec2D(5, 495), Vec2D(5, -5)]
right = [Vec2D(-5, -5), Vec2D(-5, 505), Vec2D(5, 505), Vec2D(5, -5)]

t = BaseGameEntity(top, pos=Vec2D(50, 50))
b = BaseGameEntity(bot, pos=Vec2D(50, 550))
l = BaseGameEntity(left, pos=Vec2D(50, 50))
r = BaseGameEntity(right, pos=Vec2D(550, 50))

renderer.addEntity(t)
renderer.addEntity(b)
renderer.addEntity(l)
renderer.addEntity(r)

entities = [rect, cir, t, b, l, r]
can.pack()


while True:
    deltaTime = .025
    time.sleep(deltaTime)
    for e in entities:
        e.update(deltaTime)
  
    mtv = cd.testCollisionSAT(cir, rect)
    if(mtv):
        mtv *= 2
        cir.pos += mtv
        rect.pos += -mtv
        cir.velocity *= -1
        rect.velocity *= -1
        
    mtv1 = cd.testCollisionSAT(cir, t)
    if(mtv1):
        cir.pos += mtv1
        if(cir.velocity == Vec2D(-230, -150)):  # if velocity is going to top left (-,-)
            cir.velocity = Vec2D(-230, 150)  # make it go bot left (-,+)
        elif(cir.velocity == Vec2D(230, -150)):  # if velocity is going to top right(+,-)
            cir.velocity = Vec2D(230, 150)  # make it go bot right (+,+)
    mtv2 = cd.testCollisionSAT(cir, b)
    if(mtv2):
        cir.pos += mtv2
        if(cir.velocity == Vec2D(230, 150)):
            cir.velocity = Vec2D(230, -150)
        elif(cir.velocity == Vec2D(-230, 150)):
            cir.velocity = Vec2D(-230, -150)
    mtv3 = cd.testCollisionSAT(cir, l)
    if(mtv3):
        cir.pos += mtv3
        if(cir.velocity == Vec2D(-230, -150)):
            cir.velocity = Vec2D(230, -150)
        elif(cir.velocity == Vec2D(-230, 150)):
            cir.velocity = Vec2D(230, 150)
    mtv4 = cd.testCollisionSAT(cir, r)
    if(mtv4):
        mtv4 *= 2
        cir.pos += mtv4
        if(cir.velocity == Vec2D(230, -150)):
            cir.velocity = Vec2D(-230, -150)
        elif(cir.velocity == Vec2D(230, 150)):
            cir.velocity = Vec2D(-230, 150)
        
    mtv5 = cd.testCollisionSAT(rect, t)
    if(mtv5):
        rect.pos += mtv5
        if(rect.velocity == Vec2D(-200, -200)):
            rect.velocity = Vec2D(-200, 200)
        else:
            rect.velocity = Vec2D(200, 200)
    mtv6 = cd.testCollisionSAT(rect, b)
    if(mtv6):
        rect.pos += mtv6
        if(rect.velocity == Vec2D(200, 200)):
            rect.velocity = Vec2D(200, -200)
        else:
            rect.velocity = Vec2D(-200, -200)
    mtv7 = cd.testCollisionSAT(rect, l)
    if(mtv7):
        rect.pos += mtv7
        if(rect.velocity == Vec2D(-200, -200)):
            rect.velocity = Vec2D(200, -200)
        else:
            rect.velocity = Vec2D(200, 200)
    mtv8 = cd.testCollisionSAT(rect, r)
    if(mtv8):
        rect.pos += mtv8
        if(rect.velocity == Vec2D(200, -200)):
            rect.velocity = Vec2D(-200, -200)
        else:
            rect.velocity = Vec2D(-200, 200)
                     
             
    
    renderer.renderAll()
    
    root.update()
