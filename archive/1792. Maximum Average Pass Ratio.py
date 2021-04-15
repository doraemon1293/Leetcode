from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h=[(-(n-m)/(n*(n+1)),m,n) for m,n in classes]
        heapq.heapify(h)
        for i in range(extraStudents):
            _,m,n=heapq.heappop(h)
            heapq.heappush(h,(-(n-m)/((n+1)*(n+2)),m+1,n+1))
        # print(h)
        return sum([m/n for _,m,n in h])/len(h)



print(Solution().maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))