class Solution(object):
    def shortestPathLength(self, graph):
        from collections import deque
        N=len(graph)
        q=deque([(1<<x,x) for x in range(N)])
        d={}
        for x in range(N):
            d[1<<x,x]=0
        while q:
            cover,cur_node=q.popleft()
            dis=d[cover,cur_node]
            for node in graph[cur_node]:
                new_cover=cover|(1<<node)
                if new_cover==2**N-1:
                    return dis+1
                if (new_cover,node) not in d or dis+1<d[new_cover,node]:
                    d[new_cover,node]=dis+1
                    q.append((new_cover,node))
        return 0

graph=[[1,2,3],[0],[0],[0]]
graph=[[1],[0,2,4],[1,3,4],[2],[1,2]]
graph=[[]]
print(Solution().shortestPathLength(graph))














