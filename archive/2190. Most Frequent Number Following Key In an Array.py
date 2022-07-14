import collections
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d=collections.defaultdict(int)
        for i in range(1,len(nums)):
            if nums[i-1]==key:
                d[nums[i]]+=1
        # print(d)
        return [k for k in d if d[k]==max(d.values())][0]
