# coding=utf-8
'''
Created on 2017�?9�?8�?

@author: Administrator
'''
import heapq  # python 内置�?小堆


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []  # 存储小数 存储元素的个数最多比maxHeap多一�? 存储时需�?*-1
        self.minHeap = []  # 存储大数

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.maxHeap == []:
            heapq.heappush(self.maxHeap, -num)
        elif len(self.maxHeap) < len(self.minHeap) + 1:
            # 插入到小数中maxHeap
            if num <= self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                x = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -x)
                heapq.heappush(self.minHeap, num)
        else:
            # 插入到大数中
            if num >= -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                x = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, x)
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (float(-self.maxHeap[0]) + self.minHeap[0]) / 2
        else:
            return float(-self.maxHeap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
