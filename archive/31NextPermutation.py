# coding=utf-8
'''
Created on 2017�?2�?27�?

@author: Administrator
'''

# 考虑排列1237654，它的下�?个排列是1243567，找子集的方法其实就是：从头到尾找到�?后一个满�? num[i+1] > num[i] 的一�?(实现时可以从尾到头遍历，找到第一个num[i+1] > num[i] 的一�?)，需要重排的子集就是 num[i~size-1] 这个子集。这个子集num[i~size-1] 满足�?个条件：前两个元素�?�增，后面都是�?�减或�?�后面已经没有元素�?�特殊情况是：如果找不到这样的存在�?�增关系�? num[i] �? num[i+1]，说明整个序列都是降序，也就是没有更大的排列了，根据题目要求，直接将序列逆序即可�?
# 重新排列的方式就是从num[i+1 ~ size-1]中�?�一个比num[i] 大的�?小元素，将其和num[i] 交换，然后将num[+1 ~ size-1]逆序�?


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(a, st, en):
            i, j = st, en
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i + 1, len(nums) - 1)

