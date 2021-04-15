import functools
class Solution:
    def beautySum(self, s: str) -> int:
        N=len(s)
        pre_sum_chars=[[0]*26]
        for i in range(len(s)):
            pre_sum_chars.append(pre_sum_chars[-1][:])
            pre_sum_chars[-1][ord(s[i])-ord("a")]+=1
        ans=0

        for i in range(N):
            for j in range(i+1,N):
                arr=[a-b for a,b in zip(pre_sum_chars[j+1],pre_sum_chars[i]) if a-b!=0]
                ans+=max(arr)-min(arr)

        return ans




