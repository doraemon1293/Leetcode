class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n=0
        ans=[]
        for a in A:
            n=n*2+a
            ans.append(n%5==0)
        return ans
