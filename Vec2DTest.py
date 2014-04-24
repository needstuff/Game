import unittest
from Vec2D import Vec2D

class TestVec2D(unittest.TestCase):

	def test_const(self):
		v1 = Vec2D()
		assert(v1.x == 0 and v1.y == 0)	
		
	def test_dist(self):
		v1 = Vec2D(4,3)
		v2 = Vec2D(0,0)
		assert(v1.distance(v2) == 5)
		
		v1 = Vec2D(1.0,0.0)
		v2 = Vec2D()
		assert(v1.distance(v2) == 1)
		
	def test_equality(self):
		v2 = Vec2D(1.0, 0.0)
		v1 = Vec2D(1.0, 0.0)
		assert(v1 == v2)
		
	def test_perp(self):
		v1 = Vec2D(0,1)
		v2 = Vec2D(-1, 0)
		v3 = Vec2D(1, 0)
		assert(v1.getLeftPerpendicular() == v2)
		assert(v1.getRightPerpendicular()==v3)
		
	def test_magnitude(self):
		v1 = Vec2D(4,3)
		assert(v1.magnitude() == 5)
		assert(v1.magnitudeSquared()==25)
		v1 = Vec2D()
		assert(v1.magnitude()==0)
	
	def test_arithmetic(self):
		v1 = Vec2D(3,3)
		assert(v1 * 3 == Vec2D(9,9))
		assert(v1 / 3 == Vec2D(1,1))
		assert(v1 + Vec2D(1,2) == Vec2D(4,5))
		assert(v1 - Vec2D(2,2) == Vec2D(1,1))
		v1 *= 3
		v1 /= 3
		v1 += Vec2D(1,1)
		v1 -= Vec2D(1,1)
		assert(v1 == Vec2D(3,3))
		assert(v1.dot(Vec2D(-3,3)) == 0)
		assert(v1.dot(Vec2D(0,1)) == 3)
		assert(-v1 == Vec2D(-3,-3))
		