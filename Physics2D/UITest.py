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
sidewidth = 20
vert_vertices = [Vec2D(-sidewidth/2,-height/2), Vec2D(-sidewidth/2,height/2), Vec2D(sidewidth/2,height/2), Vec2D(sidewidth/2,-height/2)]
hori_vertices = [Vec2D(-width/2 + 2*sidewidth, -sidewidth/2), Vec2D(-width/2+2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, -sidewidth/2)]
tri_vertices = [Vec2D(-20,10), Vec2D(20,10), Vec2D(0,-100)]
sqr_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]
rect_vertices = [Vec2D(-60,-5), Vec2D(-60, 5), Vec2D(60, 5), Vec2D(60, -5)]
avatar_vertices = [Vec2D(-10, -20), Vec2D(-10, 20), Vec2D(40, 0)]
tri = RigidBody2D(tri_vertices,pos=Vec2D(200,200),velocity=Vec2D(10,10), angularVelocity=-2, inverseMass = 500, inertia = 2, muS = .2, muK = .09)
sqr1 = RigidBody2D(sqr_vertices, pos=Vec2D(400,400), velocity=Vec2D(-160,-160), angularVelocity=5, orientation = 0, inverseMass = 2500, inertia =.05,muS = .2, muK = .01)
sqr2 = RigidBody2D(sqr_vertices, pos=Vec2D(350,300), velocity=Vec2D(60,-60), angularVelocity=5, orientation = 0, inverseMass = 2500, inertia =.05, muS = .2, muK = .01)
rect1 = RigidBody2D(rect_vertices, pos=Vec2D(90, 200), velocity=Vec2D(20,-60), angularVelocity=1, orientation = 0, inverseMass = 600, inertia =6, muS = .25, muK = .04)
leftwall = RigidBody2D(vert_vertices, pos=Vec2D(sidewidth,height/2), inverseMass = 0,  inertia = 999999)
rightwall = RigidBody2D(vert_vertices, pos=Vec2D(width-sidewidth,height/2), inverseMass = 0,  inertia = 999999)
topwall = RigidBody2D(hori_vertices, pos =Vec2D(width/2, sidewidth), inverseMass = 0,  inertia = 999999)
bottomwall = RigidBody2D(hori_vertices, pos=Vec2D(width/2, height-sidewidth-50), inverseMass = 0, inertia = 999999, orientation=-.2)
divider1 = RigidBody2D(rect_vertices, pos=Vec2D(width- 100,height/2), inverseMass=0, orientation=.2, inertia = 999999)
divider2 = RigidBody2D(tri_vertices, pos=Vec2D(width/4,height/2), inverseMass=0, orientation=1.57,inertia = 999999)
avatar = RigidBody2D(avatar_vertices, pos = Vec2D(200,100), velocity=Vec2D(0,0),inverseMass=4000, inertia=.4, muS=.3, muK=.04, angularVelocity=0)
entities = [ rect1, tri, sqr1, sqr2, leftwall,rightwall,topwall, bottomwall, divider1, divider2, avatar]



for e in entities:
    renderer.addEntity(e)
can.pack()

aeroDrag = 2
g = Vec2D(0,3)

def left(event):
    avatar.velocity+=Vec2D(-10,0)
def right(event):
    avatar.velocity+=Vec2D(10,0)
def up(event):
    avatar.velocity+=Vec2D(0, -10)
def down(event):
    avatar.velocity+=Vec2D(0,10)

root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

deltaTime = .02
while True:
    renderer.renderAll()
    time.sleep(deltaTime)
    
    for e in entities:
        if(e.inverseMass != 0):
            #e.velocity+=g
           
            e.update(deltaTime)
    
    for i in range(0, len(entities)):
        for j in range(i+1, len(entities)):
            e1 = entities[i]
            e2 = entities[j]        
            mtv = cd.testCollisionSAT(e1, e2)

            if mtv != None:         
                if e1.inverseMass==0:
                    e2.pos-=mtv
                if e2.inverseMass==0:
                    e1.pos+= mtv
                else:
                    e1.pos+=mtv*.7
                    e2.pos-=mtv*.7
                manifold = cd.calcCollisionManifold(e1, e2, mtv)      
               
                if(len(manifold) < 1): 
                    pass
                else:
                    cd.calcImpulseFriction(e1, e2, mtv, manifold)
                    #r = 2
                    #can.create_oval(manifold[0].x-r, manifold[0].y-r, manifold[0].x+r, manifold[0].y+r)
                    
                    
    
   
    
    root.update()
