# coding=utf-8
'''
Created on 2017å¹?6æœ?20æ—?

@author: Administrator
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from collections import deque


class NestedInteger(object):

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = deque(nestedList)
        while self.q and not self.q[0].isInteger():
            x = self.q.popleft()
            self.q.extendleft(x.getList()[::-1])
        if self.q:
            self.next_int = self.q.popleft().getInteger()
        else:
            self.next_int = None

    def next(self):
        """
        :rtype: int
        """
        res = self.next
        while self.q and not self.q[0].isInteger():
            x = self.q.popleft()
            self.q.extendleft(x.getList()[::-1])
        if self.q:
            self.next_int = self.q.popleft().getInteger()
        else:
            self.next_int = None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.next_int != None)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
