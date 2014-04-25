class Paddle1():
    
    def __init__(self, canvas, bounds, ls, le):
        self.canvas = canvas
        self.x0 = 200
        self.y0 = 300
        self.x1 = 250
        self.y1 = 320
        start_point = [self.x0, self.y0, self.x1, self.y1]
        self.pad = canvas.create_rectangle(start_point, fill='blue')        
        self.bounds = bounds
        self.ls = ls
        self.le = le
        
        
    def move(self, x, y):
        self.canvas.move(self.pad, x, y)
        
    def left(self, event, value=10):
        if self.x0 > self.ls + value:
            self.move(-value, 0)
            self.x0 -= value
            self.x1 -= value
            
    def right(self, event, value=10):
        if self.x0 < self.le - value - 50:
            self.move(value, 0)
            self.x0 += value
            self.x1 += value
            
    def up(self, event, value=10):
        if self.y0 > self.bounds // 2 + value:
            self.move(0, -value)
            self.y0 -= value
            self.y1 -= value
            
    def down(self, event, value=10):
        if self.y0 < self.le - value - 20:
            self.move(0, value)
            self.y0 += value
            self.y1 += value

