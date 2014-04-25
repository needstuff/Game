from Vec2D import Vec2D

class BaseGameEntity():
    def __init__(self, vertices, pos = Vec2D(), velocity=Vec2D(), orientation = 0, angularVelocity = 0, mass = 1):
        self.vertices = vertices
        self.pos = pos
        self.velocity = velocity
        self.orientation = orientation
        self.angularVelocity = angularVelocity
        self.mass = mass
        self.worldVertices = []
        self.worldNormals = []
        self.worldVerticesList = []
        self.__initWorldVertices__()
        
    def __initWorldVertices__(self):  
        for i in range(0, len(self.vertices)):
            rotated = self.vertices[i].getRotated(self.orientation)
            self.worldVertices.append(rotated + self.pos)
            self.worldNormals.append(rotated.getLeftPerpendicular().getNormalized())
            self.worldVerticesList.append(self.worldVertices[i].x)
            self.worldVerticesList.append(self.worldVertices[i].y)
        
    def updateWorldVertices(self):
        for i in range(0, len(self.vertices)):
            rotated = self.vertices[i].getRotated(self.orientation)
            nv = rotated + self.pos
            self.worldVertices[i] = nv
            self.worldNormals[i] = rotated.getLeftPerpendicular().getNormalized()
            j = 2*i
            self.worldVerticesList[j] = nv.x
            self.worldVerticesList[j+1] = nv.y
    
    def update(self, deltaTime):
        self.orientation+=self.angularVelocity*deltaTime
        self.updateWorldVertices()
        self.pos+= (self.velocity*deltaTime)