import math
import functools
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd_nums=functools.reduce(gcd,numsDivide)
        nums.sort()
        for i,num in enumerate(nums):
            if gcd_nums%num==0:
                return i
        return -1


