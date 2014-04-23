from Tkinter import *
import asyncore

# master = Tk()
# 
# master.mainloop()

class MainClass(asyncore.dispatcher):
    def __init__(self, conn):
        asyncore.dispatcher.__init__(self, conn)
        self.master = Tk()
        self.master.mainloop()