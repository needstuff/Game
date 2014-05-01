
class CollisionTests():
    
    def testCollisionSAT(self, e1, e2): #Seperating Axis Theorem Test
        normals = e1.worldNormals + e2.worldNormals #normals are unit vectors perpendicular to shape edges
        minOverlap = 999999999
        minOverlapAxis = None
        
        bounds1 = e1.worldVertices
        bounds2 = e2.worldVertices
        
        
        for norm in normals:
            e1Max = e1Min = bounds1[0].dot(norm) #dot product is position along the normal 
            e2Max = e2Min = bounds2[1].dot(norm)
            
            for b in bounds1:
                e1Max = max(e1Max, b.dot(norm))
                e1Min = min(e1Min, b.dot(norm))
            for b in bounds2:
                e2Max = max(e2Max, b.dot(norm))
                e2Min = min(e2Min, b.dot(norm))
        
            overlap = min(e1Max - e2Min, e2Max - e1Min)
                   
            if(overlap < 0): #Exit if there is an axis with space between shapes
                return None
            
            needFlip = overlap == e1Max - e2Min
            if(overlap < minOverlap):
                minOverlap = overlap
                minOverlapAxis = norm
                if(needFlip):
                    minOverlapAxis = -norm
                
        return minOverlapAxis * minOverlap
    
    
    def testCollisionSATExtended(self, e1, e2): #Seperating Axis Theorem Test
        normals = e1.worldNormals + e2.worldNormals #normals are unit vectors perpendicular to shape edges
        minOverlap = 999999999
        minOverlapAxis = None
        
        bounds1 = e1.worldVertices
        bounds2 = e2.worldVertices
        
        
        for norm in normals:
            e1Max = bounds1[0].dot(norm) #dot product is position along the normal 
            e1NextMax = bounds1[1].dot(norm)
            e1MaxI = 0
            e1NextMaxI = 1
            
            if(e1Max > e1NextMax):
                e1Max, e1NextMax = e1NextMax, e1Max
                e1MaxI, e1NextMaxI = e1NextMaxI, e1MaxI
            
            e1Min = min(e1Max, e1NextMax)
                
            for i in range(0, len(bounds1)):
                projLen = bounds1[i].dot(norm)
                currMax = max(e1Max, projLen)
                e1Min = min(e1Min, projLen)
                
                if(currMax > e1Max):
                    e1Max, e1NextMax = currMax, e1Max
                    e1MaxI, e1NextMaxI = i, e1MaxI
                    
            e2Max = bounds2[0].dot(norm)
            e2NextMax = bounds2[1].dot(norm)
            e2MaxI = 0
            e2NextMaxI = 1
            
            if(e2Max > e2NextMax):
                e2Max, e2NextMax = e2NextMax, e2Max
                e2MaxI, e2NextMaxI = e2NextMaxI, e2MaxI
                
            e2Min = min(e2Max, e2NextMax)
                
            for i in range(0, len(bounds2)):
                projLen = bounds2[i].dot(norm)
                currMax = max(e2Max, projLen)
                e2Min = min(e2Min, projLen)
                
                if(currMax > e2Max):
                    e2Max, e2NextMax = currMax, e2Max
                    e2MaxI, e2NextMaxI = i, e2MaxI
                    
                
        
            overlap = min(e1Max - e2Min, e2Max - e1Min)
                   
            if(overlap < 0): #Exit if there is an axis with space between shapes
                return None
            
            needFlip = overlap == e1Max - e2Min
            if(overlap < minOverlap):
                minOverlap = overlap
                minOverlapAxis = norm
                if(needFlip):
                    minOverlapAxis = -norm
                
        return (minOverlapAxis * minOverlap, bounds1[e1MaxI]-bounds1[e1NextMaxI], bounds2[e2MaxI]-bounds2[e2NextMaxI])