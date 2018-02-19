# coding=utf-8
'''
Created on 2017�?10�?26�?

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

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = {}
        for u, v, w in times:
            edges.setdefault(u, {})
            edges[u][v] = w

        visited = set()
        heap = hashHeap(maxHeap = False)
        heap.insert((0, K))
        ans = 0
        while heap.size:
            t, u = heap.pop()
            ans = t
            visited.add(u)
            for v in edges.get(u, {}):
                if v not in visited:
                    if v not in heap.key_ind:
                        heap.insert((ans + edges[u][v], v))
                    else:
                        if heap.heapList[heap.key_ind[v]][0] > ans + edges[u][v]:
                            heap.delete(v)
                            heap.insert((ans + edges[u][v], v))
        if len(visited) == N:
            return ans
        else:
            return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]]
N = 5
K = 5
print Solution().networkDelayTime(times, N, K)

