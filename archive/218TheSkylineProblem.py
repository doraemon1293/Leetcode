# coding=utf-8
'''
Created on 2017�?10�?25�?

@author: Administrator
'''


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


class Solution(object):

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = sorted([(building[0], building[2], i, "l") for i, building in enumerate(buildings)] + [(building[1], building[2], i, "r") for i, building in enumerate(buildings)])
        # point (x coordinate,height,index,left or right)
        criticalPoints = []

        maxHeap = hashHeap(True)
        for point in points:
            x, height, ind, leftOrRight = point
            if leftOrRight == "l":
                maxHeap.insert((height, ind))
            else:
                maxHeap.delete(ind)
            height = maxHeap.top()[0] if maxHeap.size else 0
            if len(criticalPoints) != 0 and criticalPoints[-1][0] == x:
                criticalPoints[-1][1] = height
            else:
                criticalPoints.append([x, height])
            if len(criticalPoints) > 1 and criticalPoints[-1][1] == criticalPoints[-2][1]:
                criticalPoints.pop()
        return criticalPoints


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
buildings = [[0, 2, 3], [2, 5, 20]]
print Solution().getSkyline(buildings)

