# coding=utf-8
'''
Created on 2017�?8�?17�?

@author: Administrator
'''
"""slow version"""
# class BinHeap:
#     def __init__(self):
#         self.heapList = [0]
#         self.currentSize = 0
#
#     def percUp(self, i):  # 向上 与父节点交换
#         while i // 2 > 0:
#             if sum(self.heapList[i]) < sum(self.heapList[i // 2]):
#                 self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
#             i = i // 2
#
#     def insert(self, k):  # 插入
#         self.heapList.append(k)
#         self.currentSize = self.currentSize + 1
#         self.percUp(self.currentSize)
#
#     def percDown(self, i):  # 向下 与较小的子节点交�?
#         while (i * 2) <= self.currentSize:
#             mc = self.minChild(i)
#             if sum(self.heapList[i]) > sum(self.heapList[mc]):
#                 self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
#             i = mc
#
#     def minChild(self, i):
#         if i * 2 + 1 > self.currentSize:
#             return i * 2
#         else:
#             if sum(self.heapList[i * 2]) < sum(self.heapList[i * 2 + 1]):
#                 return i * 2
#             else:
#                 return i * 2 + 1
#
#     def delMin(self):  # 弹出堆顶元素
#         retval = self.heapList[1]
#         self.heapList[1] = self.heapList[self.currentSize]
#         self.currentSize = self.currentSize - 1
#         self.heapList.pop()
#         self.percDown(1)
#         return retval
#
#     def buildHeap(self, alist):
#         i = len(alist) // 2
#         self.currentSize = len(alist)
#         self.heapList = [0] + alist[:]
#         while (i > 0):
#             self.percDown(i)
#             i = i - 1
#
#
#
# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         binHeap = BinHeap()
#         binHeap.buildHeap([[x, y] for x in nums1 for y in nums2])
#         ans = []
#         while k and binHeap.currentSize:
#             ans.append(binHeap.delMin())
#             k -= 1
#         return ans


class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 or n2 == 0:
            return []
        ans = 0
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while k and heap:
            temp, i, j = heapq.heappop()
            ans.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < n2:  # matrix(nums1*nums2) 如果不是矩阵�?右侧 加入右方的数
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < n1:  # matrix(nums1*nums2) 如果是矩阵最左侧 加入下方的数
                heapq.heappush(heap, (nums1[i + 1], nums2[j], i + 1, j))
        return ans


nums1 = [1, 2, 3]
nums2 = []
k = 3
print Solution().kSmallestPairs(nums1, nums2, k)
