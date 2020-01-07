class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        arr=[(x,y) for y in range(C) for x in range(R)]
        print(arr)
        arr.sort(key=lambda cell:abs(cell[0]-r0)+abs(cell[1]-c0))
        return arr
R=1
C=2
r0=0
c0=0
print(Solution().allCellsDistOrder(R,C,r0,c0))