class Ball():
    def __init__(self, canvas):
        self.radius = 15
        self.start = 225
        center = [-self.radius + self.start, -self.radius + self.start, self.radius + self.start, self.radius + self.start]
        self.cir = canvas.create_oval(center, outline='white', fill='red')
        self.canvas = canvas
        self.currentXY = (0, 0)
        
    def move(self, x , y):
        self.canvas.move(self.cir, x, y)
        self.currentXY = (x, y)
        
