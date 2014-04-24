from Tkinter import *
import time
from BaseGameEntity import *
from Renderer import *
root = Tk()

can = Canvas(root, bg="white", width=800, height=800)
renderer = Renderer(can)

tri_vertices = [Vec2D(0,0), Vec2D(50,0), Vec2D(25, 50)]
tri = BaseGameEntity(tri_vertices,velocity=Vec2D(1,1))
renderer.addEntity(tri)

can.pack()

while True:
    deltaTime = .025
    time.sleep(deltaTime)
    tri.update(deltaTime)
    renderer.render()
    root.update()
