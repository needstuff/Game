
class CollisionTests():
    
    def testCollisionSAT(self, e1, e2): #Seperating Axis Theorem Test, returns minimum translation vector to separate 2d convex polygon
        normals = e1.worldNormals + e2.worldNormals #normals are unit vectors perpendicular to shape edges
        minOverlap = 999999999
        minOverlapAxis = None
        
        for norm in normals: 
            e1Dots, e2Dots = [v.dot(norm) for v in e1.worldVertices], [v.dot(norm) for v in e2.worldVertices]
            e1Min, e1Max, e2Min, e2Max = min(e1Dots), max(e1Dots), min(e2Dots), max(e2Dots)
            
            diff1 = e1Max - e2Min
            overlap = min(diff1, e2Max - e1Min)
                   
            if(overlap <= 0): #Exit if there is an axis with space between shapes
                return None
            
            if(overlap < minOverlap):
                minOverlap = overlap
                minOverlapAxis = -norm
                if(overlap != diff1): #enforce that returned mtv points toward e2
                    minOverlapAxis = norm
                
        return minOverlapAxis * minOverlap
    
    def getAdj(self, alist, i, count): #get adjacent list elements or loop around
        return alist[max((i-1) * -(count-1), i-1)], alist[((i+1) % count)]
  
    def calcCollisionEdge(self, vertices, shape, axis):
        sMax, vi = -99999999, 0
        count = len(vertices)
        
        for i in xrange(count):
            dp = vertices[i].dot(axis)
            if(dp > sMax):
                sMax, vi = dp, i
        
        adj = self.getAdj(vertices, vi, count)
        v1, v2, v3 = vertices[vi], adj[0], adj[1]
        e1, e2 = (v1,v2),(v1, v3)
        d1, d2 = v1- v2, v1 - v3
        
        if(abs(d1.dot(axis)) < abs(d2.dot(axis))):
            return e1
        return e2
    
    def clip(self, v1, v2, offset, n):
        d1 = v1.dot(n) - offset
        d2 = v2.dot(n) - offset
        ret = []
        if(d1 >= 0):
            ret.append(v1)
        if(d2 >= 0):
            ret.append(v2)
        
        if(d1*d2 < 0):
            inc = v2-v1
            p = d1 / (d1 - d2)
            inc*=p
            ret.append(v1+inc)
        return ret  
        
    def calcCollisionManifold(self, s1, s2, mtv):
        n = mtv
        #Assume mtv point to s2
        ref, inc = self.calcCollisionEdge(s1.worldVertices, s1, -n), self.calcCollisionEdge(s2.worldVertices, s2, n)
       
        vecRef, vecInc = ref[0]- ref[1], inc[0] - inc[1]
        if abs(vecInc.dot(n)) < abs(vecRef.dot(n)):
            ref,inc = inc, ref
            n = -n
         
        refAxis = (ref[1] - ref[0]).getNormalized()
        offset = refAxis.dot(ref[0])
            
        manifold = self.clip(inc[0], inc[1], offset, refAxis)
        offset = refAxis.dot(ref[1])
        if(len(manifold) < 2):
            return manifold
        manifold = self.clip(manifold[0], manifold[1], -offset, -refAxis)
        
        if(len(manifold) < 2):
            return manifold
        nNorm = refAxis.getLeftPerpendicular()
        maxV = nNorm.dot(ref[0])
        ret = []
        if(nNorm.dot(manifold[0]) - maxV >= 0):
            ret.append(manifold[0])
        if(nNorm.dot(manifold[1]) - maxV  >= 0):
            ret.append(manifold[1])
            
        return ret
         
    def calcImpulse(self, s1, s2, mtv, manifold):
        e = 1
        cp = manifold[0]
        r1 = cp-s1.pos
        r2 = cp-s2.pos
        relVel = s2.velocity-s1.velocity
        n = mtv.getNormalized()
        s1Angular = pow((r1.getLeftPerpendicular()*s1.angularVelocity).dot(n),2)
        s2Angular = pow((r2.getLeftPerpendicular()*s2.angularVelocity).dot(n),2)
        denom = n.dot(n * (s1.inverseMass + s2.inverseMass)) + s1Angular + s2Angular
        j = relVel.dot(n) * -(1+e) / denom
        
        s1.velocity -= n * j * s1.inverseMass
        s2.velocity += n * j * s2.inverseMass
        
        