import heapq
import collections
from typing import List
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        intervals=collections.deque(intervals)
        qs=[(q,i) for i,q in enumerate(queries)]
        ans=[-1]*len(qs)
        qs.sort()

        heap=[]
        for q,q_ind in qs:
            while intervals and intervals[0][0]<=q:
                heapq.heappush(heap,(intervals[0][1]-intervals[0][0]+1,intervals[0][0],intervals[0][1]))
                intervals.popleft()
            while heap and heap[0][2]<q:
                heapq.heappop(heap)
            if heap:
                ans[q_ind]=heap[0][0]
            else:
                ans[q_ind]=-1
        return ans
