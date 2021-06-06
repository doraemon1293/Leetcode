import collections
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.d1=collections.Counter(nums1)
        self.d2=collections.Counter(nums2)
        self.nums2=nums2
    def add(self, index: int, val: int) -> None:
        self.d2[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.d2[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        res=sum([self.d2[tot-num]*self.d1[num] for num in self.d1])
        return res