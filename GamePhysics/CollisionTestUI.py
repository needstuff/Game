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
sidewidth = 6
vert_vertices = [Vec2D(-sidewidth/2,-height/2), Vec2D(-sidewidth/2,height/2), Vec2D(sidewidth/2,height/2), Vec2D(sidewidth/2,-height/2)]
hori_vertices = [Vec2D(-width/2 + 2*sidewidth, -sidewidth/2), Vec2D(-width/2+2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, -sidewidth/2)]
tri_vertices = [Vec2D(-20,10), Vec2D(20,10), Vec2D(0,-80)]
sqr_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
rect_vertices = [Vec2D(-60,-5), Vec2D(-60, 5), Vec2D(60, 5), Vec2D(60, -5)]
tri = BaseGameEntity(tri_vertices,pos=Vec2D(200,200),velocity=Vec2D(50,50), angularVelocity=-2, inverseMass = 500, inertia = 15)
rect = BaseGameEntity(sqr_vertices, pos=Vec2D(400,400), velocity=Vec2D(-60,-60), angularVelocity=5, orientation = 0, inverseMass = 3000, inertia =2)
rect2 = BaseGameEntity(sqr_vertices, pos=Vec2D(300,300), velocity=Vec2D(60,-60), angularVelocity=5, orientation = 0, inverseMass = 3000, inertia =2)
rect3 = BaseGameEntity(rect_vertices, pos=Vec2D(50,50), velocity=Vec2D(20,-60), angularVelocity=5, orientation = 0, inverseMass = 1000, inertia =10)
leftwall = BaseGameEntity(vert_vertices, pos=Vec2D(sidewidth,height/2), inverseMass = 0,  inertia = 999999)
rightwall = BaseGameEntity(vert_vertices, pos=Vec2D(width-sidewidth,height/2), inverseMass = 0,  inertia = 999999)
topwall = BaseGameEntity(hori_vertices, pos =Vec2D(width/2, sidewidth), inverseMass = 0,  inertia = 999999)
bottomwall = BaseGameEntity(hori_vertices, pos=Vec2D(width/2, height-sidewidth), inverseMass = 0, inertia = 999999)
entities = [rect, tri, rect3, rect2, leftwall,rightwall,topwall, bottomwall]


for e in entities:
    renderer.addEntity(e)
    e.update(0)
can.pack()


deltaTime = .015
while True:
    renderer.renderAll()
    time.sleep(deltaTime)
    
    for e in entities:
        if(e.inverseMass != 0):
            e.update(deltaTime)
    for i in range(0, len(entities)):
        for j in range(i+1, len(entities)):
            e1 = entities[i]
            e2 = entities[j]        
            mtv = cd.testCollisionSAT(e1, e2)

            if(mtv != None): 
                manifold = cd.calcCollisionManifold(e1, e2, mtv)
                e1.pos+=mtv
                e2.pos-=mtv
                
                if(len(manifold) < 1):
                    manifold.append(Vec2D(0,0))
                    print("HACK")
                r = 2
                can.create_oval(manifold[0].x-r, manifold[0].y-r, manifold[0].x+r, manifold[0].y+r)
                cd.calcImpulse(e1, e2, mtv, manifold)

                    
                    
    
   
    
    root.update()
