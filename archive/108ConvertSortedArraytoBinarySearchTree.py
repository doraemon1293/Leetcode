# coding=utf-8
'''
Created on 2017å¹?2æœ?8æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def sortedArrayToBST(st, end, nums):
            if st > end:
                return None
            mid = (st + end) / 2
            node = TreeNode(nums[mid])
            node.left = sortedArrayToBST(st, mid - 1, nums)
            node.right = sortedArrayToBST(mid + 1, end, nums)
            return node

        if nums:
            return sortedArrayToBST(0, len(nums) - 1, nums)
        else:
            return None


nums = [0]
print Solution().sortedArrayToBST(nums)

