class Renderer(): #Draw Rigid Body in TK
    
    def __init__(self, canvas):
        self.map = {}
        self.canvas = canvas
        
        
    def addEntity(self, e):
        self.map[e] = self.canvas.create_polygon(e.worldVerticesList, fill=e.color)
    
    def removeEntity(self, e):
        self.canvas.delete(self.map.pop(e))
        
    def renderAll(self):
        for entity in self.map.keys():
            self.canvas.coords(self.map[entity], *entity.worldVerticesList)
            
    def setColor(self,e, c):
        self.canvas.itemconfig(self.map[e], fill=c)