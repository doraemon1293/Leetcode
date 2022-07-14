class Solution:
    def countElements(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        return len([1 for num in nums if num!=mini and num!=maxi])