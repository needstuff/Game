import math
class Vec3D:
	TOL = .001
	
	def __init__(self, x, y, z):
		self.x = self.y = self.z = 0
		if(x):
			self.x = x
		if(y):
			self.y = y
		if(z):
			self.z = z
		
		
	def __add__(self, rhs):
		return Vec3D(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)
	
	
	def __iadd__(self, rhs):
		self.x += rhs
		self.y +=rhs
		self.z +=rhs
			
	def __isub__(self, rhs):
		self.x -= rhs
		self.y -=rhs
		self.z -=rhs
			
	def __imul__(self, rhs):
		self.x *= rhs
		self.y *=rhs
		self.z *=rhs
			
	def __idiv__(self, rhs):
		self.x /= rhs
		self.y /=rhs
		self.z /=rhs
			
	def __sub__(self, rhs):
		return Vec3D(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)
	
	def __div__(self, scalar):
		return Vec3D(self.x / scalar, self.y / scalar, self.z / scalar)
	
	def __mul__(self, scalar):
		return Vec3D(self.x * scalar, self.y * scalar, self.z * scalar)
	
	def dot(self, rhs):
		return self.x*rhs.x+self.y*rhs.y+self.z*rhs.z
	
	def len(self):
		return math.sqrt(self.x*self.x + self.y*self.y, self.z*self.z)
	
	def lenSqrd(self):
		return (self.x*self.x+self.y*self.y+self.z*self.z)
	
	def getRotatedAboutZ(self, angle):
		cs = math.cos(angle)
		sn = math.sin(angle)
		return Vec3D(self.x*cs - self.y*sn, self.x*sn + self.y*cs, self.z)
	
	
		
	
	