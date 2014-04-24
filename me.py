from Tkinter import *

root = Tk()

def key(event):
    s = "pressed " + repr(event.char)
    root.title(s)

def callback(event):
    frame.focus_set()
    s = "clicked at " + str(event.x) + " " + str(event.y)
    root.title(s)
    
def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    root.title(str1)
    # switch color to red if mouse enters a set location range
#     x,y, delta = 100, 100, 10
#     frame.config(bg='red'
#                  if abs(xm - x) < delta and abs(ym - y) < delta
#                  else 'yellow')

frame = Frame(root, width=300, height=300, bg="white")
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.bind("<Motion>", showxy)
frame.pack()
 
root.mainloop()
