from typing import List
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold==0:
            return [True]*len(queries)
        uf={}
        def find(x):
            if x not in uf:
                uf[x]=x
                return x
            path=[]
            while uf[x]!=x:
                path.append(x)
                x=uf[x]
            for a in path:
                uf[a]=x
            return x


        def connect(a,b):
            uf[find(a)]=find(b)

        for div in range(threshold+1,n+1):
            for num in range(div*2,n+1,div):
                print(div,num)
                connect(div,num)
        ans = [find(i) == find(j) for i, j in queries]
        return ans

n=14
threshold=4
queries=[[4,2],[7,2],[4,3],[1,4],[4,11],[6,8],[8,12],[12,5],[3,7],[12,6],[3,6],[11,9],[6,9],[6,4],[4,9],[14,4],[10,14],[14,2],[9,8],[8,7],[13,14],[12,4],[7,4],[10,4],[1,6],[9,7],[5,13],[10,11],[14,8],[5,6],[7,12],[11,5],[8,13],[4,8],[1,9],[8,2],[1,13],[5,9],[12,1],[13,10],[1,8],[10,6],[9,13],[6,11],[3,5],[5,2]]
# print(Solution().areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]))
# print(Solution().areConnected(n=6568,threshold=4008,queries=[]))
print(Solution().areConnected(n,threshold,queries))


