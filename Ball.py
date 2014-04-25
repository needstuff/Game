
class Ball():
    def __init__(self, canvas):        
        self.x0 = -15  # initial left edge
        self.x1 = 15  # initial right edge
        self.y0 = -15  # initial top edge
        self.y1 = 15  # initial bot edge
        
        
        self.dx = 2  # x movement
        self.dy = 3  # y movement
        
        center = [self.x0, self.y0, self.x1, self.y1]
        self.self = canvas.create_oval(center, outline='white', fill='red')
        self.canvas = canvas
        
    def move(self, line_start , line_end, pad1, pad2):
                
        while True:
            self.canvas.move(self.self, self.dx, self.dy)
            self.canvas.after(20)
            self.canvas.update()
            
            if self.detectPad(pad1, line_start, line_end):
                pass
            else:
                if self.x1 > line_end:
                    self.dx = -2
                if self.x0 < line_start:
                    self.dx = 2
                if self.y1 > line_end:
                    self.dy = -3
                if self.y0 < line_start:
                    self.dy = 3
                
                
            self.x0 += self.dx
            self.x1 += self.dx
            self.y0 += self.dy
            self.y1 += self.dy
            
    def detectPad(self, pad1, line_start, line_end):
        bounds = 450
        pad1Posx1 = line_end - pad1.x1
        pad1Posx2 = line_end - pad1.x0
        pad1Posy1 = line_end - pad1.y1 + bounds // 2
        pad1Posy2 = line_end - pad1.y0 + bounds // 2
        
        if self.x1 in range(pad1Posx1, pad1Posx2) and self.y1 in range(pad1Posy1, pad1Posy2):
            self.dx = -2
            self.dy = -3
            return True
        elif self.x0 in range(pad1Posx1, pad1Posx2) and self.y0 in range(pad1Posy1, pad1Posy2):
            self.dx = 2
            self.dy = 3
            return True
        return False
        
        
