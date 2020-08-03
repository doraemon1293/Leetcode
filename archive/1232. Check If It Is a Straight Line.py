class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        dx,dy=coordinates[1][0]-coordinates[0][0],coordinates[1][1]-coordinates[0][1]
        dx,dy=dx/dy,1
        for i in range(1,len(coordinates)-1):
            tdx,tdy=coordinates[i+1][0]-coordinates[i][0],coordinates[i+1][1]-coordinates[i][1]
            if tdx*dy!=tdy*dx:
                return False

        return True