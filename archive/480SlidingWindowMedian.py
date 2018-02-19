# coding=utf-8
'''
Created on 2017�?10�?11�?

@author: Administrator
'''


# 堆中的元素是(value,key)
class hashHeap(object):

    def __init__(self, maxHeap):
        self.size = 0
        self.heapList = [0]
        self.maxHeap = maxHeap  # True�?大堆 False�?小堆
        self.key_ind = {}  # 通过插入元素的key查询在heap中的位置

    def percUp(self, i):
        while i / 2:
            if self.maxHeap:  # �?大堆
                if self.heapList[i] > self.heapList[i / 2]:
                    k1, k2 = self.heapList[i][1], self.heapList[i / 2][1]
                    self.heapList[i], self.heapList[i / 2] = self.heapList[i / 2], self.heapList[i]
                    self.key_ind[k1], self.key_ind[k2] = self.key_ind[k2], self.key_ind[k1]
                i /= 2
            else:  # �?小堆
                if self.heapList[i] < self.heapList[i / 2]:
                    k1, k2 = self.heapList[i][1], self.heapList[i / 2][1]
                    self.heapList[i], self.heapList[i / 2] = self.heapList[i / 2], self.heapList[i]
                    self.key_ind[k1], self.key_ind[k2] = self.key_ind[k2], self.key_ind[k1]
                i /= 2

    def percDown(self, i):
        while i * 2 <= self.size:
            if self.maxHeap:
                if i * 2 + 1 > self.size:
                    child = i * 2
                else:
                    if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                        child = i * 2
                    else:
                        child = i * 2 + 1
                if self.heapList[i] < self.heapList[child]:
                    k1, k2 = self.heapList[i][1], self.heapList[child][1]
                    self.heapList[i], self.heapList[child] = self.heapList[child], self.heapList[i]
                    self.key_ind[k1], self.key_ind[k2] = self.key_ind[k2], self.key_ind[k1]
                i = child
            else:
                if i * 2 + 1 > self.size:
                    child = i * 2
                else:
                    if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                        child = i * 2
                    else:
                        child = i * 2 + 1
                if self.heapList[i] > self.heapList[child]:
                    k1, k2 = self.heapList[i][1], self.heapList[child][1]
                    self.heapList[i], self.heapList[child] = self.heapList[child], self.heapList[i]
                    self.key_ind[k1], self.key_ind[k2] = self.key_ind[k2], self.key_ind[k1]
                i = child

    def insert(self, k):  # 插入
        self.heapList.append(k)
        self.size = self.size + 1
        self.key_ind[k[1]] = self.size
        self.percUp(self.size)

    def pop(self):  # 弹出堆顶元素
        res = self.heapList[1]
        self.key_ind[self.heapList[self.size][1]] = 1
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percDown(1)
        del self.key_ind[res[1]]
        return res

    def delete(self, key):  # 根据key删除�?个元�?(key�?定存�?)
        ind = self.key_ind[key]
        if self.maxHeap:
            if self.heapList[ind] > self.heapList[self.size]:
                self.key_ind[self.heapList[self.size][1]] = ind
                self.heapList[ind] = self.heapList[self.size]
                self.heapList.pop()
                self.size -= 1
                del self.key_ind[key]
                if ind <= self.size:
                    self.percDown(ind)
            else:
                self.key_ind[self.heapList[self.size][1]] = ind
                self.heapList[ind] = self.heapList[self.size]
                self.heapList.pop()
                self.size -= 1
                del self.key_ind[key]
                if ind <= self.size:
                        self.percUp(ind)
        else:
            if self.heapList[ind] > self.heapList[self.size]:
                self.key_ind[self.heapList[self.size][1]] = ind
                self.heapList[ind] = self.heapList[self.size]
                self.heapList.pop()
                self.size -= 1
                del self.key_ind[key]
                if ind <= self.size:
                    self.percUp(ind)
            else:
                self.key_ind[self.heapList[self.size][1]] = ind
                self.heapList[ind] = self.heapList[self.size]
                self.heapList.pop()
                self.size -= 1
                del self.key_ind[key]
                if ind <= self.size:
                    self.percDown(ind)

    def top(self):  # 返回栈顶元素
        return self.heapList[1]


def balance(maxHeap, minHeap):
    while maxHeap.size > minHeap.size + 1:
        minHeap.insert(maxHeap.pop())
    while minHeap.size > maxHeap.size:
        maxHeap.insert(minHeap.pop())


class Solution(object):

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if nums == []: return []
        maxHeap = hashHeap(True)
        minHeap = hashHeap(False)
        ans = []
        for i in range(k):
            maxHeap.insert((nums[i], i))
        balance(maxHeap, minHeap)
        if k % 2 == 0:
            ans.append((float(maxHeap.top()[0]) + minHeap.top()[0]) / 2)
        else:
            ans.append(float(maxHeap.top()[0]))
#         print "max", maxHeap.heapList
#         print "min", minHeap.heapList
#         print "ans", ans
        for i in range(1, len(nums) - k + 1):
            delete_ind, add_ind = i - 1, i + k - 1
            if delete_ind in maxHeap.key_ind:
                maxHeap.delete(delete_ind)
            else:
                minHeap.delete(delete_ind)
            balance(maxHeap, minHeap)
            if maxHeap.size == 0 or nums[add_ind] > maxHeap.top()[0]:
                minHeap.insert((nums[add_ind], add_ind))
            else:
                maxHeap.insert((nums[add_ind], add_ind))
            balance(maxHeap, minHeap)
#             print "max", maxHeap.heapList
#             print "min", minHeap.heapList
            if k % 2 == 0:
                ans.append((float(maxHeap.top()[0]) + minHeap.top()[0]) / 2)
            else:
                ans.append(float(maxHeap.top()[0]))
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
nums = [1, -1]
k = 1
print Solution().medianSlidingWindow(nums, k)

