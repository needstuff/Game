from Tkinter import *
import time, random, copy
from UI.Renderer import *
from Vec2D import Vec2D
from Core import Physics
from RigidBody2D import RigidBody2D
class Entity(RigidBody2D):
    def __init__(self, vertices, pos=Vec2D(0,0),velocity=Vec2D(0,0), angularVelocity=0,orientation=0,  health=100, inverseMass=0, inertia=1, muS=0, muK=0,color='black'):
        RigidBody2D.__init__(self, vertices=vertices, pos=pos, velocity=velocity,angularVelocity=angularVelocity, orientation=orientation, inverseMass=inverseMass, inertia=inertia, 
                             muS=muS, muK=muK)
        self.health=health
        self.color= color
    def hurt(self, amnt):
        self.health-=amnt
        
class Craft(Entity):
    def __init__(self, vertices, pos, inverseMass, inertia, muS, muK, health, color):
        self.turnRate = .4
        self.fowardThrust = 10
        self.MAX_FOWARD = 25
        self.MAX_REVERSE = -5
        self.heading=Vec2D(1,0)
        self.speed=0
        Entity.__init__(self, vertices=vertices, pos=pos, velocity=Vec2D(0,0),angularVelocity=0, orientation=0, inverseMass=inverseMass, inertia=inertia, 
                             muS=muS, muK=muK, health=health, color=color)
        
    def turnLeft(self):
        self.angularVelocity-=self.turnRate
    
    def turnRight(self):
        self.angularVelocity+=self.turnRate
    def foward(self):
        self.speed = min(self.speed+self.fowardThrust, self.MAX_FOWARD)
        heading=self.heading.getRotated(self.orientation)
        self.velocity += heading*self.speed
        
    def reverse(self):
        self.speed = max(self.speed-self.fowardThrust, self.MAX_REVERSE)
        heading=self.heading.getRotated(self.orientation)
        self.velocity += heading*self.speed
        
    def update(self, deltaTime):
        self.angularVelocity*=.97
        self.velocity*=.98
        RigidBody2D.update(self, deltaTime)
        
width = height = 800
root = Tk()
cd = Physics()
can = Canvas(root, bg="gray", width=width, height=height)
can.pack()
renderer = Renderer(can)


damMult = .01
sidewidth = 20
sqr_vertices = [Vec2D(-10,-10), Vec2D(-10,10), Vec2D(10,10), Vec2D(10,-10)]

class HealthBar(Entity):
    def __init__(self,width, height, target, offset):
        self.rightVerts = [Vec2D(width/2,height/2), Vec2D(width/2,-height/2)]
        self.leftVerts=[Vec2D(-width/2,-height/2), Vec2D(-width/2,height/2)]
        self.originalHealth=target.health
        self.vertices=self.leftVerts+self.rightVerts
        self.target=target
        self.offset=offset
        self.width = width
        self.health = target.health
        Entity.__init__(self, vertices=self.vertices, pos=target.pos+offset, velocity=Vec2D(0,0), angularVelocity=0, orientation=0, health=30, inverseMass=0, inertia=0, muS=0, muK=0, color='green')
        
    def hurt(self, amnt):
        p = amnt/self.originalHealth
        for v in self.rightVerts:
            v+=Vec2D(-1,0)*self.width*p
            
    def update(self):
        self.pos = self.target.pos+self.offset
        d = self.health-self.target.health
        self.health = self.target.health
        if(d > 0):
            self.hurt(d)
        self.updateWorldVertices()

def randVec(myMax):
    return Vec2D(random.uniform(-1,1)*myMax, random.uniform(-1,1)*myMax)
def makeTarget(scale, vertices):
    v = copy.deepcopy(vertices)
    for vert in v:
        vert*=scale
    return Entity( v, pos=Vec2D(width/2, height/2)+randVec(300), velocity=Vec2D(-2,-3), angularVelocity=5, orientation = 0, inverseMass = 1000 / scale, inertia =3 * scale,muS = .2, muK = .01, health=50*scale)

vert_vertices = [Vec2D(-sidewidth/2,-height/2), Vec2D(-sidewidth/2,height/2), Vec2D(sidewidth/2,height/2), Vec2D(sidewidth/2,-height/2)]
hori_vertices = [Vec2D(-width/2 + 2*sidewidth, -sidewidth/2), Vec2D(-width/2+2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, sidewidth/2), Vec2D(width/2-2*sidewidth, -sidewidth/2)]
avatar_vertices = [Vec2D(-10, -20), Vec2D(-10, 20), Vec2D(40, 0)]
bullet_vertices=[Vec2D(-5,-5), Vec2D(-5,5), Vec2D(10,0)]
debris_vertices=[Vec2D(-6, -4), Vec2D(-5, 6), Vec2D(2,8)]
leftwall = Entity(vert_vertices, pos=Vec2D(sidewidth,height/2), inverseMass = 0,  inertia = 999999)
rightwall = Entity(vert_vertices, pos=Vec2D(width-sidewidth,height/2), inverseMass = 0,  inertia = 999999)
topwall = Entity(hori_vertices, pos =Vec2D(width/2, sidewidth), inverseMass = 0,  inertia = 999999)
bottomwall = Entity(hori_vertices, pos=Vec2D(width/2, height-sidewidth), inverseMass = 0, inertia = 999999, orientation=0)
midwall1 = Entity([v*.8 for v in hori_vertices], pos=Vec2D(width/2, height-sidewidth-300), inverseMass = 0, inertia = 999999, orientation=2)
craft = Craft(avatar_vertices, pos = Vec2D(200,100), inverseMass=4000, inertia=.5, muS=.3, muK=.04, health = 20, color='blue')
static = [leftwall,rightwall,topwall, bottomwall, midwall1]
targets = [makeTarget(random.uniform(.5,5), sqr_vertices) for i in range(0, 5)]
entities = [craft]+targets
hp=HealthBar(50, 5, craft, Vec2D(25,-25))
renderer.addEntity(hp)
debris = []

for e in entities+static:
    renderer.addEntity(e)


def left(event):
    craft.turnLeft()
def right(event):
    craft.turnRight()
def up(event):
    craft.foward()
def down(event):
    craft.reverse()
def shoot(event):
    bullet=Entity(bullet_vertices, pos=craft.worldVertices[2], velocity=Vec2D(1,0).getRotated(craft.orientation)*800, inverseMass=500, orientation=craft.orientation, inertia=1, health=20, color='red')
    entities.append(bullet)
    renderer.addEntity(bullet)
    renderer.setColor(bullet, bullet.color)
    
def randTri(scale):
    return [Vec2D(random.random() * -scale, random.random()*-scale),Vec2D(random.random() * -scale, random.random()*scale),Vec2D(random.random() * scale, random.uniform(-1,1)*scale)]

expCount = 30
debris_tris=[randTri(10) for i in range(0,expCount)]


   
def explode(e):
    entities.remove(e)
    renderer.removeEntity(e)
    for i in range(0,expCount):
        p=Vec2D(e.pos[0], e.pos[1])
        v = copy.deepcopy(debris_tris[i])
        crap=Entity(v, pos=p, velocity=randVec(300), angularVelocity=5, inverseMass=500000,color=e.color)
        debris.append(crap)
        renderer.addEntity(crap)
        renderer.setColor(crap, crap.color)
        
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<space>', shoot)

deltaTime = .015
while True:
    renderer.renderAll()
    time.sleep(deltaTime)
    
    for e in entities:
        e.update(deltaTime)
    hp.update()
    while(len(debris) > 200):
        renderer.removeEntity(debris.pop(0))
    for d in debris:
        for v in d.vertices:
            v*=.99
        d.update(deltaTime)
    for i in range(0, len(entities)):
        for j in range(i+1, len(entities)):
            e1 = entities[i]
            e2 = entities[j]        
            mtv = cd.testCollisionSAT(e1, e2)
            if mtv != None:         
                e1.pos+=mtv*.7
                e2.pos-=mtv*.7
                manifold = cd.calcCollisionManifold(e1, e2, mtv)      
                if(len(manifold) >= 1): 
                    dam=(e1.velocity-e2.velocity).magnitude()*damMult
                    cd.calcImpulseFriction(e1, e2, mtv, manifold)
                    e1.hurt(dam)
                    e2.hurt(dam)
    for e in entities:
        for s in static: 
            mtv=cd.testCollisionSAT(e, s)
            if(mtv!=None):
                e.pos+=mtv
                e.hurt(e.velocity.magnitude()*damMult)
                manifold = cd.calcCollisionManifold(e, s, mtv)
                if(len(manifold) < 1): 
                    pass
                else:
                    cd.calcImpulseFriction(e, s, mtv, manifold)   
    for e in entities:
        if(e.health <=0):
            explode(e)
    
    root.update()
