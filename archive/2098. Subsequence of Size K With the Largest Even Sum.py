from typing import List


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # nums_o=sorted([num for num in nums if nums%2])
        # nums_e=sorted([num for num in nums if nums%2==0])
        nums.sort(reverse=True)
        nums_k = nums[:k]
        nums_rest = nums[k:]
        summ = sum(nums_k)
        if summ % 2 == 0:
            return summ
        else:
            last_even = last_odd = None
            for i in range(len(nums_k) - 1, -1, -1):
                if last_even == None and nums_k[i] % 2 == 0:
                    last_even = nums_k[i]
                if last_odd == None and nums_k[i] % 2 == 1:
                    last_odd = nums_k[i]
                if last_odd != None and last_even != None:
                    break

            first_even = first_odd = None
            for i in range(len(nums_rest)):
                if first_even == None and nums_rest[i] % 2 == 0:
                    first_even = nums_rest[i]
                if first_odd == None and nums_rest[i] % 2 == 1:
                    first_odd = nums_rest[i]
                if first_odd != None and first_even != None:
                    break
            summ1 = -1
            if last_even != None and first_odd != None:
                summ1 = summ - last_even + first_odd
            summ2 = -1
            if last_odd != None and first_even != None:
                summ2 = summ - last_odd + first_even
            return max(summ1, summ2)



