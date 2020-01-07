from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust) -> int:
        d1=defaultdict(set)
        d2=defaultdict(set)
        for a,b in trust:
            d1[a].add(b)
            d2[b].add(a)
        arr=[x for x in range(1,N+1) if len(d1[x])==0]
        print(arr)
        ans=[]
        for x in arr:
            if len(d2[x])==N-1:
                ans.append(x)
        if len(ans)==1:
            return ans[0]
        else:
            return -1


N=2
trust=[[1,2]]
print(Solution().findJudge(N,trust))