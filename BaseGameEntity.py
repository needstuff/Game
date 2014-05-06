from Vec2D import Vec2D

class BaseGameEntity():
    def __init__(self, vertices, pos = Vec2D(), velocity=Vec2D(), orientation = 0, angularVelocity = 0, mass = 1, inverseMass = 1):
        self.vertices = vertices
        self.pos = pos
        self.velocity = velocity
        self.orientation = orientation
        self.angularVelocity = angularVelocity
        self.mass = mass
        self.inverseMass = inverseMass
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
        count = len(self.vertices)
        for i in range(0, count):
            self.worldVertices[i] = self.vertices[i].getRotated(self.orientation)+self.pos
        
        prev = self.worldVertices[0]
        self.worldNormals[0] = (prev-self.worldVertices[count-1]).getLeftPerpendicular().getNormalized()
        for i in range(1, count):
            curr = self.worldVertices[i]     
            self.worldNormals[i] = (curr-prev).getLeftPerpendicular().getNormalized()
            curr = prev
        for i in range(0, count):
            j = 2*i
            v = self.worldVertices[i]
            self.worldVerticesList[j] = v.x
            self.worldVerticesList[j+1] = v.y
         
            
        
    def update(self, deltaTime):
        self.orientation+=self.angularVelocity*deltaTime
        self.updateWorldVertices()
        self.pos+= (self.velocity*deltaTime)