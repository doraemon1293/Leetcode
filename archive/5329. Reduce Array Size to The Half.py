import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=collections.Counter(arr)
        remain=len(arr)
        ans=0
        for _, i in c.most_common():
            remain-=i
            ans+=1
            if remain<=len(arr)//2:
                return ans
