from Tkinter import *
import time
from BaseGameEntity import *
from Renderer import *
from GamePhysics import CollisionDetection

width = height = 500
root = Tk()
cd = CollisionDetection.CollisionTests()
can = Canvas(root, bg="white", width=width, height=height)
renderer = Renderer(can)
sidewidth = 5
vert_vertices = [Vec2D(-sidewidth,-height/2), Vec2D(-sidewidth,height/2), Vec2D(sidewidth,height/2), Vec2D(sidewidth,-height/2)]
hori_vertices = [Vec2D(-width/2 + 2*sidewidth, -5), Vec2D(-width/2+2*sidewidth, 5), Vec2D(width/2-2*sidewidth, 5), Vec2D(width/2-2*sidewidth, -5)]
tri_vertices = [Vec2D(-10,10), Vec2D(10,10), Vec2D(0,-20)]
rect_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
tri = BaseGameEntity(tri_vertices,pos=Vec2D(100,100),velocity=Vec2D(120,120), angularVelocity=1)
rect = BaseGameEntity(rect_vertices, pos=Vec2D(400,400), velocity=Vec2D(-190,-20), angularVelocity=.5)
leftwall = BaseGameEntity(vert_vertices, pos=Vec2D(5,height/2), inverseMass = 0)
rightwall = BaseGameEntity(vert_vertices, pos=Vec2D(width-5,height/2), inverseMass = 0)
topwall = BaseGameEntity(hori_vertices, pos =Vec2D(width/2, 5), inverseMass = 0)
bottomwall = BaseGameEntity(hori_vertices, pos=Vec2D(width/2, height-5), inverseMass = 0)
entities = [rect, tri, leftwall,rightwall,topwall, bottomwall]
for e in entities:
    renderer.addEntity(e)
can.pack()


deltaTime = .015
while True:
    time.sleep(deltaTime)
    for e in entities:
        e.update(deltaTime)
   
    for i in range(0, len(entities)):
        for j in range(i+1, len(entities)):
            e1 = entities[i]
            e2 = entities[j]        
            mtv = cd.testCollisionSAT(e1, e2)
            if(mtv != None):    
                e1.pos+=  mtv * e1.inverseMass * 5
                e2.pos-=  mtv * e2.inverseMass * 5
                dur = mtv.getNormalized()    
                    
                e1.velocity = -e1.velocity.getReflection(dur)
                e2.velocity = -e2.velocity.getReflection(-dur)
                        
                    
                    
    
    renderer.renderAll()
    
    root.update()
