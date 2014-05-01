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
tri_vertices = [Vec2D(-10,10), Vec2D(10,10), Vec2D(30,-50)]
rect_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
tri = BaseGameEntity(tri_vertices,pos=Vec2D(100,100),velocity=Vec2D(120,120), angularVelocity=-1)
rect = BaseGameEntity(rect_vertices, pos=Vec2D(400,400), velocity=Vec2D(-120,-120), angularVelocity=1)
leftwall = BaseGameEntity(vert_vertices, pos=Vec2D(5,height/2), mass=9999999999)
rightwall = BaseGameEntity(vert_vertices, pos=Vec2D(width-5,height/2), mass=9999999999)
topwall = BaseGameEntity(hori_vertices, pos =Vec2D(width/2, 5), mass=9999999999)
bottomwall = BaseGameEntity(hori_vertices, pos=Vec2D(width/2, height-5), mass=9999999999)
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
        for j in range(1, len(entities)):
            if(j!=i):
                e1 = entities[i]
                e2 = entities[j]        
                vectors = cd.testCollisionSATExtended(e1, e2)
                if(vectors):
                    mtv = vectors[0]
                    e1Norm = (vectors[1]).getLeftPerpendicular().getNormalized()
                    e2Norm = (vectors[2]).getLeftPerpendicular().getNormalized()
                    
                    e12e2 = e2.pos - e1.pos
                    if(e1Norm.dot(e12e2) < 0):
                        e1Norm*=-1
                    if(e2Norm.dot(e12e2) > 0):
                        e2Norm*=-1
                        
                    e1.pos+=mtv / e1.mass
                    e2.pos-=mtv / e2.mass

                    e1.velocity = e2Norm # e1.velocity.getReflection(e2Norm)
                    e2.velocity = e2.velocity.getReflection(e1Norm)
    
    renderer.renderAll()
    
    root.update()
