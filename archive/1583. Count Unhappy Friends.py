from typing import List
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pre={}
        for i,preference in enumerate(preferences):
            pre[i]={}
            for ind,j in enumerate(preference):
                pre[i][j]=ind
        unhappy=set()
        for i in range(len(pairs)):
            for j in range(i+1,len(pairs)):
                p1=pairs[i]
                p2=pairs[j]
                for x,y in ((p1[0],p1[1]),(p1[1],p1[0])):
                    for u,v in ((p2[0],p2[1]),(p2[1],p2[0])):
                        if pre[x][u]<pre[x][y] and pre[u][x]<pre[u][v]:
                            unhappy.add(x)
                            unhappy.add(u)
        return len(unhappy)