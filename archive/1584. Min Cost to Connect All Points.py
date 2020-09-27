from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        dis=[[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                dis[i][j]=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        visited_nodes=set()
        heap=[(0,0)]
        cost=0
        while len(visited_nodes)<N:
            c,node=heapq.heappop(heap)
            while node in visited_nodes:
                c,node=heapq.heappop(heap)
            cost+=c
            visited_nodes.add(node)
            for i in range(N):
                if i not in visited_nodes:
                    heapq.heappush(heap,(dis[node][i],i))
        return cost