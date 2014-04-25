from Tkinter import Tk, Canvas
from Ball import Ball
from Paddle1 import Paddle1
from Paddle2 import Paddle2
    
def table():
    _top = canvas.create_line(line_start, line_start, line_end, line_start, fill='white')
    _bot = canvas.create_line(line_start, line_end, line_end, line_end, fill='white')
    _left = canvas.create_line(line_start, line_start, line_start, line_end, fill='white')
    _right = canvas.create_line(line_end, line_start, line_end, line_end, fill='white')
    _mid = canvas.create_line(line_start, bounds // 2, line_end, bounds // 2, fill='white')
    _goal_top = canvas.create_rectangle(bounds // 3, line_start, 2 * bounds // 3, line_start + 10, fill='yellow')
    _goal_bot = canvas.create_rectangle(bounds // 3, line_end, 2 * bounds // 3, line_end - 10, fill='yellow')


root = Tk()
oldx = oldy = 0
bounds = 450
line_start = 50
line_end = 400
canvas = Canvas(root, width=bounds, height=bounds, bg='black')
canvas.pack()
table()
root.title("Air Hockey")
cir = Ball(canvas)

pad1 = Paddle1(canvas, bounds, line_start, line_end)
pad2 = Paddle2(canvas, bounds, line_start, line_end)

root.bind("<Left>", pad1.left)
root.bind("<Right>", pad1.right)
root.bind("<Up>", pad1.up)
root.bind("<Down>", pad1.down)

root.bind("<a>", pad2.left)
root.bind("<d>", pad2.right)
root.bind("<w>", pad2.up)
root.bind("<s>", pad2.down)
cir.move(line_start, line_end, pad1, pad2)

root.mainloop()
