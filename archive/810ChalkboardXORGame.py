class Solution:
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = 0
        for num in nums: temp ^=num
        return temp == 0 or len(nums) % 2 == 0