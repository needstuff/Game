class Renderer():
    
    def __init__(self, canvas):
        self.entities = []
        self.map = {}
        self.canvas = canvas
        
    def addEntity(self, e):
        self.map[e] = self.canvas.create_polygon(e.listVertices())
        self.entities.append(e)
        
    def render(self):
        for entity in self.entities:
            self.canvas.move(self.map[entity], entity.pos.x, entity.pos.y)