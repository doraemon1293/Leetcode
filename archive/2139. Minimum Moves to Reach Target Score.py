class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles==0:
            return target-1
        target=bin(target)[2:]
        ans=0
        if len(target)-1>maxDoubles:
            ans+=int(target[:-maxDoubles],2)-1
            for ch in target[-maxDoubles:]:
                if ch=="0":
                    ans+=1
                else:
                    ans+=2
        else:
            for ch in target[1:]:
                if ch=="0":
                    ans+=1
                else:
                    ans+=2
        return ans
print(Solution().minMoves(target = 10, maxDoubles = 4))