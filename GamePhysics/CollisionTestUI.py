from Tkinter import *
import time
from BaseGameEntity import *
from Renderer import *
from GamePhysics import CollisionDetection

root = Tk()
cd = CollisionDetection.CollisionTests()
can = Canvas(root, bg="white", width=800, height=800)
renderer = Renderer(can)

tri_vertices = [Vec2D(-10,10), Vec2D(10,10), Vec2D(0,-20)]
rect_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
tri = BaseGameEntity(tri_vertices,velocity=Vec2D(20,20))
rect = BaseGameEntity(rect_vertices, pos=Vec2D(200,200), velocity=Vec2D(-20,-20))
renderer.addEntity(tri)
renderer.addEntity(rect)
entities = [rect, tri]
can.pack()

while True:
    deltaTime = .025
    time.sleep(deltaTime)
    for e in entities:
        e.update(deltaTime)
  
    mtv = cd.testCollisionSAT(tri, rect)
    if(mtv):
        tri.pos+=mtv
        rect.pos+=-mtv
                     
             
    
    renderer.renderAll()
    
    root.update()
