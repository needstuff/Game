from Tkinter import *
from math import sqrt
import time
from BaseGameEntity import *
from Renderer import *
from GamePhysics import CollisionDetection

def drag(event):
    pad.pos = Vec2D(event.x, event.y)



root = Tk()
cd = CollisionDetection.CollisionTests()
can = Canvas(root, bg="white", width=600, height=600)
renderer = Renderer(can)

circle = [Vec2D(10 * sqrt(3) / 2, 10 * .5), Vec2D(10 * sqrt(2) / 2, 10 * sqrt(2) / 2), Vec2D(10 * .5, 10 * sqrt(3) / 2), Vec2D(0, 10),
                Vec2D(10 * -.5, 10 * sqrt(3) / 2), Vec2D(10 * -sqrt(2) / 2, 10 * sqrt(2) / 2), Vec2D(10 * -sqrt(3) / 2, 10 * .5), Vec2D(-10, 0),
                 Vec2D(10 * -sqrt(3) / 2, 10 * -.5), Vec2D(10 * -sqrt(2) / 2, 10 * -sqrt(2) / 2), Vec2D(10 * -.5, 10 * -sqrt(3) / 2), Vec2D(0, -10),
                  Vec2D(10 * .5, 10 * -sqrt(3) / 2), Vec2D(10 * sqrt(2) / 2, 10 * -sqrt(2) / 2), Vec2D(10 * sqrt(3) / 2, 10 * -.5), Vec2D(10, 0)]
rect_vertices = [Vec2D(-10, -10), Vec2D(-10, 10), Vec2D(10, 10), Vec2D(10, -10)]
cir = BaseGameEntity(circle, pos=Vec2D(150, 100), velocity=Vec2D(230, 150), angularVelocity=3)
rect = BaseGameEntity(rect_vertices, pos=Vec2D(300, 100), velocity=Vec2D(-200, -200), angularVelocity=3)

pad_v = [Vec2D(-30, -10), Vec2D(-30, 10), Vec2D(30,10), Vec2D(30,-10)]
pad = BaseGameEntity(pad_v, pos=Vec2D(300, 500))
renderer.addEntity(cir)
renderer.addEntity(rect)
renderer.addEntity(pad)

horizontal = [Vec2D(-5, -5), Vec2D(-5, 5), Vec2D(495, 5), Vec2D(495, -5)]
vertical = [Vec2D(-5, -5), Vec2D(-5, 505), Vec2D(5, 505), Vec2D(5, -5)]

top = BaseGameEntity(horizontal, pos=Vec2D(50, 50))
bot = BaseGameEntity(horizontal, pos=Vec2D(50, 550))
left = BaseGameEntity(vertical, pos=Vec2D(50, 50))
right = BaseGameEntity(vertical, pos=Vec2D(550, 50))

renderer.addEntity(top)
renderer.addEntity(bot)
renderer.addEntity(left)
renderer.addEntity(right)

entities = [rect, cir, top, bot, left, right, pad]
can.pack()


root.bind("<B1-Motion>", drag)


while True:
    deltaTime = .025
    time.sleep(deltaTime)
    for e in entities:
        e.update(deltaTime)
        
    m = cd.testCollisionSAT(cir, pad)
    if m:
        cir.pos += m
        if cir.velocity == Vec2D(230, 150) or cir.velocity == Vec2D(-230, 150):
            cir.velocity = -cir.velocity.getReflection(Vec2D(0, -1))
  
    mtv = cd.testCollisionSAT(cir, rect)
    if(mtv):
        cir.pos += mtv
        rect.pos += -mtv
        cir.velocity *= -1
        rect.velocity *= -1
        
    mtv1 = cd.testCollisionSAT(cir, top)
    if(mtv1):
        cir.pos += mtv1
        if cir.velocity == Vec2D(-230, -150) or cir.velocity == Vec2D(230, -150): 
            cir.velocity = -cir.velocity.getReflection(Vec2D(0, 1))

    mtv2 = cd.testCollisionSAT(cir, bot)
    if(mtv2):
        cir.pos += mtv2
        if cir.velocity == Vec2D(230, 150) or cir.velocity == Vec2D(-230, 150):
            cir.velocity = -cir.velocity.getReflection(Vec2D(0, -1))

    mtv3 = cd.testCollisionSAT(cir, left)
    if(mtv3):
        cir.pos += mtv3
        if cir.velocity == Vec2D(-230, 150) or cir.velocity == Vec2D(-230, -150):
            cir.velocity = -cir.velocity.getReflection(Vec2D(1, 0))

    mtv4 = cd.testCollisionSAT(cir, right)
    if(mtv4):
        cir.pos += mtv4
        if cir.velocity == Vec2D(230, 150) or cir.velocity == Vec2D(230, -150):
            cir.velocity = -cir.velocity.getReflection(Vec2D(-1, 0))    
        
    mtv5 = cd.testCollisionSAT(rect, top)
    if(mtv5):
        rect.pos += mtv5
        if rect.velocity == Vec2D(-200, -200) or rect.velocity == Vec2D(200, -200): 
            rect.velocity = -rect.velocity.getReflection(Vec2D(0, 1))
    mtv6 = cd.testCollisionSAT(rect, bot)
    if(mtv6):
        rect.pos += mtv6
        if rect.velocity == Vec2D(200, 200) or rect.velocity == Vec2D(-200, 200): 
            rect.velocity = -rect.velocity.getReflection(Vec2D(0, -1))
    mtv7 = cd.testCollisionSAT(rect, left)
    if(mtv7):
        rect.pos += mtv7
        if rect.velocity == Vec2D(-200, 200) or rect.velocity == Vec2D(-200, -200): 
            rect.velocity = -rect.velocity.getReflection(Vec2D(1, 0))
    mtv8 = cd.testCollisionSAT(rect, right)
    if(mtv8):
        rect.pos += mtv8
        if rect.velocity == Vec2D(200, 200) or rect.velocity == Vec2D(200, -200): 
            rect.velocity = -rect.velocity.getReflection(Vec2D(-1, 0))
    
    
    
    renderer.renderAll()
    
    root.update()
