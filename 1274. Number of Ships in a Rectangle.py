# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        if x1 > x2 or y1 > y2:
            return 0
        if sea.hasShips(topRight, bottomLeft):
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            if x1 == x2 and y1 == y2:
                return 1
            else:
                return self.countShips(sea, Point(mx, my), Point(x1, y1), ) + \
                       self.countShips(sea, Point(x2, y2), Point(mx + 1, my + 1), ) + \
                       self.countShips(sea, Point(x2, my), Point(mx + 1, y1), ) + \
                       self.countShips(sea, Point(mx, y2), Point(x1, my + 1))
        # mx,my x1,y1
        # x2,y2 mx+1,my+1
        # x2,my mx+1,y1
        # x1,my+1 mx,y2
        else:
            return 0
