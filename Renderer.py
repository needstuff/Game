class Renderer():
    
    def __init__(self, canvas):
        self.entities = []
        self.map = {}
        self.canvas = canvas
        
    def addEntity(self, e):
        self.map[e] = self.canvas.create_polygon(e.worldVerticesList)
        self.entities.append(e)
        
    def renderAll(self):
        for entity in self.entities:
            #self.canvas.move(self.map[entity], entity.velocity.x, entity.velocity.y)
            self.canvas.coords(self.map[entity], *entity.worldVerticesList)