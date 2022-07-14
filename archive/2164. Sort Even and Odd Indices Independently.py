class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_arr = sorted([nums[i] for i in range(0, len(nums), 2)])
        odd_arr = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even_arr[i // 2]
            else:
                nums[i] = odd_arr[i // 2]
        return nums

