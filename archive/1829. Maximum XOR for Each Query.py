class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xor_all = nums[0]
        for num in nums[1:]:
            xor_all ^= num
        ans = []
        for _ in range(len(nums)):
            k = (2 ** maximumBit - 1) ^ xor_all
            xor_all ^= nums[-1]
            ans.append(k)
            nums.pop()
        return ans
