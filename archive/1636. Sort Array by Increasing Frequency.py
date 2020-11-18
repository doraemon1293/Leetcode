import collections
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=collections.Counter(nums)
        arr=[]
        for v,k in sorted([(v,-k) for k,v in c.items()]):
            arr+=[-k]*v
        return arr