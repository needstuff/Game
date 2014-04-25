import math

class Vec2D:
	DISTANCE_TOLERANCE = .001
	
	def __init__(self, x=0, y=0):
		self.x = self.y = 0
		if(x):
			self.x = x
		if(y):
			self.y = y
			
	def __add__(self, rhs):
		return Vec2D(self.x + rhs.x, self.y + rhs.y)
	
	def __sub__(self, rhs):
		return Vec2D(self.x - rhs.x, self.y - rhs.y)
	
	def __div__(self, scalar):
		return Vec2D(self.x / scalar, self.y / scalar)
	
	def __mul__(self, scalar):
		return Vec2D(self.x * scalar, self.y * scalar)
	
	def __iadd__(self, rhs):
		self.x += rhs.x
		self.y +=rhs.y
		return self
		
	def __isub__(self, rhs):
		self.x -= rhs.x
		self.y -=rhs.y
		return self
		
	def __imul__(self, scalar):
		self.x *= scalar
		self.y *=scalar
		return self
			
	def __idiv__(self, scalar):
		self.x /= scalar
		self.y /=scalar
		return self
	
	def dot(self, rhs):
		return self.x*rhs.x+self.y*rhs.y
	
	def magnitude(self):
		return math.sqrt(self.x*self.x + self.y*self.y)
	
	def magnitudeSquared(self):
		return (self.x*self.x+self.y*self.y)
	
	def distance(self, other):
		dx = (self.x - other.x)
		dy = (self.y - other.y)
		return math.sqrt(dx*dx + dy*dy)
	
	def getNormalized(self):
		mag = math.sqrt(self.x*self.x + self.y*self.y)
		return Vec2D(self.x / mag, self.y / mag)
	
	def getRotated(self, angle):
		cs = math.cos(angle)
		sn = math.sin(angle)
		return Vec2D(self.x*cs - self.y*sn, self.x*sn + self.y*cs)
	
	def getLeftPerpendicular(self):
		return Vec2D(-self.y, self.x)
		
	def getRightPerpendicular(self):
		return Vec2D(self.y, -self.x)
	
	def __neg__(self):
		return Vec2D(-self.x, -self.y)
	
	def __eq__(self, other):
		return self.distance(other) < Vec2D.DISTANCE_TOLERANCE
	
	
	def __getitem__(self, key):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		else:
			raise IndexError("Invalid subscript "+str(key)+" to Vec2d")
	def __setitem__(self, key, value):
		if key == 0:
			self.x = value
		elif key == 1:
			self.y = value
		else:
			raise IndexError("Invalid subscript "+str(key)+" to Vec2d")
	def __repr__(self):
		return 'Vec2d(%s, %s)' % (self.x, self.y)
	
		
	