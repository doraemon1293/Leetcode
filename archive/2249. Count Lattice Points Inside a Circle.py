from typing import List
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans=set()
        for x,y,r in circles:
            for x0 in range(x-r,x+r+1):
                for y0 in range(y-r,y+r+1):
                    if (x0-x)**2+(y0-y)**2<=r**2:
                        ans.add((x0,y0))


        return len(ans)

circles=[[8,9,6],[9,8,4],[4,1,1],[8,5,1],[7,1,1],[6,7,5],[7,1,1],[7,1,1],[5,5,3]]
# circles=[[8,9,6]]
print(Solution().countLatticePoints(circles))