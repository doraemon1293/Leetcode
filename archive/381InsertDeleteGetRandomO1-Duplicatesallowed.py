# coding=utf-8
'''
Created on 2017å¹?6æœ?16æ—?

@author: Administrator
'''
from collections import defaultdict
from random import randint


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            self.arr.append(val)
            self.d[val].add(len(self.arr) - 1)
            return False
        else:
            self.arr.append(val)
            self.d[val].add(len(self.arr) - 1)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            # print self.d
            # print self.arr
            i = self.d[val].pop()
            # print i
            if i != len(self.arr) - 1:
                self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
                self.d[self.arr[i]].remove(len(self.arr) - 1)
                self.d[self.arr[i]].add(i)
                self.arr.pop()
            else:
                self.arr.pop()
            if len(self.d[val]) == 0 :
                del self.d[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.arr[randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
s = RandomizedCollection()
print s.insert(9)
s.insert(9)
s.insert(1)
s.insert(1)
s.insert(2)
s.insert(1)
s.remove(2)
s.remove(1)
s.remove(1)
s.insert(9)
s.remove(1)

["RandomizedCollection", "insert", "insert", "insert", "insert", "insert", "insert", "remove", "remove", "remove", "insert", "remove"]
[[], [9], [9], [1], [1], [2], [1], [2], [1], [1], [9], [1]]
