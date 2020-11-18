from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        sum_total=0
        sum_heap=0
        for i in range(1,len(heights)):
            if heights[i]>heights[i-1]:
                delta=heights[i]-heights[i-1]
                heapq.heappush(heap,delta)
                sum_total+=delta
                sum_heap+=delta
                if len(heap)>ladders:
                    sum_heap-=heapq.heappop(heap)
                if sum_total-sum_heap>bricks:
                    return i-1
        return i


heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1
print(Solution().furthestBuilding(heights, bricks, ladders))
