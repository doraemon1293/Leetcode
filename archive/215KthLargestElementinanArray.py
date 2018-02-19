class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(s, e, k):
            x = nums[s]
            i, j = s, e
            while i < j:
                while i < j and nums[j] <= x:
                    j -= 1
                if i < j: nums[i] = nums[j]
                while i < j and nums[i] > x:
                    i += 1
                if i < j: nums[j] = nums[i]
            nums[i] = x
            print nums
            if i - s + 1 == k:
                return nums[i]
            elif i - s + 1 > k:
                return helper(s, i - 1, k)
            else:
                return helper(i + 1, e, k - (i - s + 1))

        from random import shuffle
        shuffle(nums)
        return helper(0, len(nums) - 1, k)


nums = [3, 2, 1, 5, 6, 4, 7, 8, 9, 10, 11, 12]
k = 6
print Solution().findKthLargest(nums, k)
print nums

