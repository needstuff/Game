from Tkinter import *
import time
root = Tk()
oldx = 0
oldy = 0

def click(event):
    s = "clicked at " + str(event.x) + " " + str(event.y)
    if event.x > line_end - radius:
        event.x = line_end - radius
    if event.x < line_start + radius:
        event.x = line_start + radius
    if event.y > line_end - radius:
        event.y = line_end - radius
    if event.y < line_start + radius:
        event.y = line_start + radius
        
    move(event.x, event.y)
    root.title(s)
    
def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    root.title(str1)

def drag(event):
    showxy(event)
    click(event)

def move(x, y):
    global oldx, oldy
    dx = x - oldx         
    dy = y - oldy
    canvas.move(cir, dx, dy)
    oldx = x
    oldy = y

canvas = Canvas(root, width=450, height=450, bg='black')
canvas.pack()
radius = 15
center = [-radius, -radius, radius, radius]
line_start = 50
line_end = 400
cir = canvas.create_oval(center, outline='white', fill='red')
top = canvas.create_line(line_start, line_start, line_end, line_start, fill='blue')
bot = canvas.create_line(line_start, line_end, line_end, line_end, fill='blue')
left = canvas.create_line(line_start, line_start, line_start, line_end, fill='blue')
right = canvas.create_line(line_end, line_start, line_end, line_end, fill='blue')
goal_top = canvas.create_rectangle((line_end + line_start) // 3, line_start, 2 * (line_end + line_start) // 3, line_start + 10, fill='yellow')
goal_bot = canvas.create_rectangle((line_end + line_start) // 3, line_end, 2 * (line_end + line_start) // 3, line_end - 10, fill='yellow')
canvas.bind("<Button-1>", click)
canvas.bind("<Motion>", showxy)
canvas.bind("<B1-Motion>", drag)

root.mainloop()
