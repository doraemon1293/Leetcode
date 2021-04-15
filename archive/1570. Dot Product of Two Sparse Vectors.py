from typing import List
class SparseVector:
    def __init__(self, nums: List[int]):
        self.values={}
        for i,num in enumerate(nums):
            if num:
                self.values[i]=num



    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([self.values[k]*vec.values[k] for k in set(self.values)&set(vec.values)])


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)