from Vec2D import Vec2D

class BaseGameEntity():
    def __init__(self, vertices, pos = Vec2D(), velocity=Vec2D(), orientation = 0, angularVelocity = 0):
        self.vertices = vertices
        self.pos = pos
        self.velocity = velocity
        self.orientation = orientation
        self.angularVelocity = angularVelocity
        self.__initWorldVertices__()
        
    def __initWorldVertices__(self):
        self.worldVertices = []
        for i in range(0, len(self.vertices)):
            rotated = self.vertices[i].getRotated(self.orientation)
            self.worldVertices.append(rotated + self.pos)
               
    
        
    def updateWorldVertices(self):
        for i in range(0, len(self.vertices)):
            rotated = self.vertices[i].getRotated(self.orientation)
            self.worldVertices[i] = rotated + self.pos
            
    
    def update(self, deltaTime):
        self.updateWorldVertices()
        self.pos+= self.velocity*deltaTime
        
    def listVertices(self):
        list = []
        for v in self.vertices:
            list.append(v.x)
            list.append(v.y)
        return list