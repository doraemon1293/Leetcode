from typing import List
import collections
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        #create graph
        g=collections.defaultdict(set)
        for s,t in edges:
            g[s].add(t)
            g[t].add(s)

        #dfs find circle
        circle=[0]
        visited=set([0])
        def dfs(node,parent):
            for nbr in g[node]:
                if nbr!=parent:
                    if nbr in visited:
                        return True,nbr
                    circle.append(nbr)
                    visited.add(nbr)
                    find_circle,circle_head=dfs(nbr,node)
                    if find_circle:
                        return True,circle_head
                    circle.pop()
                    visited.remove(nbr)
            return False,None

        find_circle, circle_head = dfs(0,None)

        circle=circle[circle.index(circle_head):]


        #bfs find distance
        q=circle
        ans=[-1]*n
        step=0
        while q:
            new_q=[]
            for node in q:
                ans[node]=step
            for node in q:
                for nbr in g[node]:
                    if ans[nbr]==-1:
                        new_q.append(nbr)
            step+=1
            q=new_q
        return ans

n = 7
edges = [[1,2],[2,3],[3,4],[4,1],[0,1],[5,2],[6,5]]
print(Solution().distanceToCycle(n,edges))