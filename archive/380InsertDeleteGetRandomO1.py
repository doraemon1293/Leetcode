# coding=utf-8
'''
Created on 2017�?6�?16�?

@author: Administrator
'''
from random import randint


# 删除时把要删除的移到�?后一�? 然后删除�?后一位即�?
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            self.arr.append(val)
            self.d[val] = len(self.arr) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            i = self.d[val]
            self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]
            self.d[self.arr[i]] = i
            del self.d[val]
            del self.arr[-1]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.arr[randint(0, len(self.arr) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
