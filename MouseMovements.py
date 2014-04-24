from Tkinter import *
import time
root = Tk()
oldx = 0
oldy = 0

def key(event):
    s = "pressed " + repr(event.char)
    root.title(s)

def callback(event):
    # frame.focus_set()
    canvas.focus_set()
    s = "clicked at " + str(event.x) + " " + str(event.y)
    move(event.x, event.y)
    root.title(s)
    
def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    root.title(str1)
    #move(xm, ym)
    # switch color to red if mouse enters a set location range
#     x,y, delta = 100, 100, 10
#     frame.config(bg='red'
#                  if abs(xm - x) < delta and abs(ym - y) < delta
#                  else 'yellow')

def drag(event):
    showxy(event)
    callback(event)

def move(x, y):
    global oldx, oldy
    dx = x - oldx         
    dy = y - oldy
    canvas.move(cir, dx, dy)
    oldx = x
    oldy = y

canvas = Canvas(root, width=450, height=450, bg='gray')
canvas.pack(fill='both', expand=True)
cir = canvas.create_oval(-25, -25, 25, 25, outline='white', fill='red')
top = canvas.create_line(10, 10, 400, 10, fill='blue')
bot = canvas.create_line(10, 400, 400, 400, fill='blue')
left = canvas.create_line(10, 10, 10, 400, fill='blue')
right = canvas.create_line(400, 10, 400, 400, fill='blue')
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.bind("<Motion>", showxy)
canvas.bind("<B1-Motion>", drag)


# frame = Frame(root, width=300, height=300, bg="white")
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.bind("<Motion>", showxy)
# frame.pack()
 
root.mainloop()
