import collections
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        st=rounds[0]
        ans=collections.defaultdict(int)
        ans[st]+=1
        for i in range(1,len(rounds)):
            end=rounds[i]
            x=st+1
            while x!=end+1:
                if x>n:
                    x-=n
                ans[x]+=1
                x+=1
            st=end
        return sorted([k for k in ans if ans[k]==max(ans.values())])

