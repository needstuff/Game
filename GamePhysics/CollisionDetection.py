
class CollisionTests():
    
    def testCollisionSAT(self, e1, e2):
        normals = e1.worldNormals + e2.worldNormals
        minOverlap = 999999999
        minOverlapAxis = None
        
        bounds1 = e1.worldVertices
        bounds2 = e2.worldVertices
        
        for norm in normals:
            e1Max = e1Min = bounds1[0].dot(norm)
            e2Max = e2Min = bounds2[1].dot(norm)
            
            for b in bounds1:
                e1Max = max(e1Max, b.dot(norm))
                e1Min = min(e1Min, b.dot(norm))
            for b in bounds2:
                e2Max = max(e2Max, b.dot(norm))
                e2Min = min(e2Min, b.dot(norm))
        
            overlap = min(e1Max - e2Min, e2Max - e1Min)
                   
            if(overlap < 0):
                return None
            
            needFlip = overlap == e1Max - e2Min
            if(overlap < minOverlap):
                minOverlap = overlap
                minOverlapAxis = norm
                if(needFlip):
                    minOverlapAxis = -norm
                
        return minOverlapAxis * minOverlap
        