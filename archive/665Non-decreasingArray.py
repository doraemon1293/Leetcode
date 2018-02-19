class Solution(object):

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [-float("inf")] + nums + [float("inf")]
        temp = 0
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                temp += 1
                if temp > 1:
                    return False
        return True


nums = [2, 3, 3, 2, 4]
nums = [4, 3, 2]
# nums = [3, 4, 2, 3]
print Solution().checkPossibility(nums)
