from collections import defaultdict
import heapq
class Solution:
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        graph=defaultdict(dict)
        used=defaultdict(int)
        q=[(0,0)]
        d=defaultdict(lambda :M)
        d[0]=0
        visited=set()
        ans=0
        for u,v,w in edges:
            graph[u][v]=graph[v][u]=w
        while q:
            dis,u=heapq.heappop(q)
            if u not in visited:
                ans+=1
                visited.add(u)
                for v,w in graph[u].items():
                    used[u,v]=max(used[u,v],min(w,M-dis))
                    dis2=dis+w+1
                    if dis2<=d[v]:
                        heapq.heappush(q,(dis2,v))
                        d[v]=dis2
        for u,v,w in edges:
            ans+=min(w,used[u,v]+used[v,u])