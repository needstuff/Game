class Paddle2():
    
    def __init__(self, canvas, bounds, ls, le):
        self.canvas = canvas
        self.currentX = 200
        self.currentY = 130
        start_point = [self.currentX, self.currentY, self.currentX + 50, self.currentY + 20]
        self.pad = canvas.create_rectangle(start_point, fill='green')        
        self.bounds = bounds
        self.ls = ls
        self.le = le
        
        
    def move(self, x, y):
        self.canvas.move(self.pad, x, y)
        
    def left(self, event, value=10):
        if self.currentX > self.ls + value:
            self.move(-value, 0)
            self.currentX -= value
    def right(self, event, value=10):
        if self.currentX < self.le - value - 50:
            self.move(value, 0)
            self.currentX += value
    def up(self, event, value=10):
        if self.currentY > self.ls + value:
            self.move(0, -value)
            self.currentY -= value
    def down(self, event, value=10):
        if self.currentY < self.bounds // 2 - 30:
            self.move(0, value)
            self.currentY += value

