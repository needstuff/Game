from Tkinter import *
import time
from UI.Renderer import *
from Vec2D import Vec2D
from Core import Physics
from RigidBody2D import RigidBody2D

width = height = 600
root = Tk()
cd = Physics()
can = Canvas(root, bg="white", width=width, height=height)
renderer = Renderer(can)
sidewidth = 10
vert_vertices = [Vec2D(-sidewidth/2,-height/2), Vec2D(-sidewidth/2,height/2), Vec2D(sidewidth/2,height/2), Vec2D(sidewidth/2,-height/2)]
hori_vertices = [Vec2D(-width/2 + 2*sidewidth, -sidewidth/2), Vec2D(-width/2+2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, -sidewidth/2)]
tri_vertices = [Vec2D(-40,10), Vec2D(40,10), Vec2D(0,-120)]
sqr_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
rect_vertices = [Vec2D(-60,-5), Vec2D(-60, 5), Vec2D(60, 5), Vec2D(60, -5)]
tri = RigidBody2D(tri_vertices,pos=Vec2D(200,200),velocity=Vec2D(10,10), angularVelocity=-2, inverseMass = 750, inertia = 50)
rect = RigidBody2D(sqr_vertices, pos=Vec2D(400,400), velocity=Vec2D(-60,-60), angularVelocity=5, orientation = 0, inverseMass = 2500, inertia =.05)
rect2 = RigidBody2D(sqr_vertices, pos=Vec2D(300,300), velocity=Vec2D(60,-60), angularVelocity=5, orientation = 0, inverseMass = 2500, inertia =.05)
rect3 = RigidBody2D(rect_vertices, pos=Vec2D(50,50), velocity=Vec2D(20,-60), angularVelocity=25, orientation = 0, inverseMass = 2000, inertia =5)
leftwall = RigidBody2D(vert_vertices, pos=Vec2D(sidewidth,height/2), inverseMass = 0,  inertia = 999999)
rightwall = RigidBody2D(vert_vertices, pos=Vec2D(width-sidewidth,height/2), inverseMass = 0,  inertia = 999999)
topwall = RigidBody2D(hori_vertices, pos =Vec2D(width/2, sidewidth), inverseMass = 0,  inertia = 999999)
bottomwall = RigidBody2D(hori_vertices, pos=Vec2D(width/2, height-sidewidth-50), inverseMass = 0, inertia = 999999, orientation=-.2)
entities = [rect, tri, rect3, rect2, leftwall,rightwall,topwall, bottomwall]


for e in entities:
    renderer.addEntity(e)
    e.update(0)
can.pack()

aeroDrag = 2
g = Vec2D(0,6)

deltaTime = .015
while True:
    renderer.renderAll()
    time.sleep(deltaTime)
    
    for e in entities:
        if(e.inverseMass != 0):
            e.velocity+=g
           
            e.update(deltaTime)
    
    for i in range(0, len(entities)):
        for j in range(i+1, len(entities)):
            e1 = entities[i]
            e2 = entities[j]        
            mtv = cd.testCollisionSAT(e1, e2)

            if(mtv != None): 
                manifold = cd.calcCollisionManifold(e1, e2, mtv)
                if(len(manifold) < 1): #bug workaround, SAT giving false positives
                    pass                    
                else:
                    e1.pos+=mtv
                    e2.pos-=mtv
                    #r = 2
                    #can.create_oval(manifold[0].x-r, manifold[0].y-r, manifold[0].x+r, manifold[0].y+r)
                    cd.calcImpulse(e1, e2, mtv, manifold)

                    
                    
    
   
    
    root.update()
