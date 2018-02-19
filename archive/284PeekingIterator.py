# coding=utf-8
'''
Created on 2017å¹?7æœ?14æ—?

@author: Administrator
'''

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object):

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        if self.iter.hasNext():
            self.nextVal = self.iter.next()
        else:
            self.nextVal = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextVal

    def next(self):
        """
        :rtype: int
        """
        res = self.nextVal
        if self.iter.hasNext():
            self.nextVal = self.iter.next()
        else:
            self.nextVal = None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextVal != None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
