# coding=utf-8
'''
Created on 2017å¹?5æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        def cal(x):
            return a * (x ** 2) + b * x + c

        def bisearch(target, nums):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) / 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            return hi

        if a == 0:
            return map(cal, nums) if b > 0 else map(cal, nums)[::-1]
        else:
            middle = -(float(b) / 2 / a)
            mid_index = bisearch(middle, nums)
            print mid_index, middle
            i = mid_index
            j = mid_index + 1
            ans = []
            while i >= 0 or j < len(nums):
                if abs(nums[i] - middle) < abs(nums[j] - middle):
                    print i, nums[i]
                    ans.append(cal(nums[i]))
                    i -= 1
                else:
                    print j, nums[j]
                    ans.append(cal(nums[j]))
                    j += 1
                if i < 0:
                    ans.extend(map(cal, nums[j:]))
                    break
                if j >= len(nums):
                    ans.extend(map(cal, nums[:i + 1])[::-1])
                    break
                print ans
            if a < 0:
                ans.reverse()
            return ans


nums = [-4, -2, 2, 4]
a = -1
b = 3
c = 5
print Solution().sortTransformedArray(nums, a, b, c)
