import bisect
import collections


class MKAverage:

    def __init__(self, m: int, k: int):
        self.arr = []
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        if len(self.arr) < self.m - 1:
            self.arr.append(num)
        elif len(self.arr) == self.m - 1:
            self.arr.append(num)
            self.arr1=sorted(self.arr)
            self.arr=collections.deque(self.arr)
            self.first = collections.deque(self.arr1[:self.k])
            self.middle = collections.deque(self.arr1[self.k:self.m - self.k])
            self.last = collections.deque(self.arr1[(self.m - self.k):self.m])
            self.first_sum, self.middle_sum, self.last_sum = sum(self.first), sum(self.middle), sum(self.last)
            
        else:
            delete_num=self.arr.popleft()
            self.arr.append(num)

            if self.first[0]<=num<=self.first[-1]:
                self.first_sum=self.first_sum-self.first[-1] + num
                self.middle = self.middle - self.middle[-1] + self.first[-1]
                self.last = self.last-self.last[-1]+self.middle[-1]
                self.first.

    def calculateMKAverage(self) -> int:
        if len(self.arr) < self.m:
            return -1

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
