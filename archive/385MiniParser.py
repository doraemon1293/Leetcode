# coding=utf-8
'''
Created on 2017å¹?8æœ?16æ—?

@author: Administrator
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        import re
        if re.match(r"^-?[0-9]+$", s):
            nest = NestedInteger()
            nest.setInteger(int(s))
            return nest
        s = [x for x in re.split(r"([-0-9]+)", s) if x != ""]
        print s
        arr = []
        for x in s:
            if re.match(r"-?[0-9]+", x):
                arr.append(int(x))
            else:
                arr.extend(list(x))
        arr = [x for x in arr if x != ","]
        print arr

        stack = []
        nest = None
        num = None
        for ch in arr:
            if ch == "[":
                if nest != None:
                    stack.append(nest)
                nest = NestedInteger()
            if type(ch) == int:
                nest.add(ch)
            if ch == ",":
                pass
            if ch == "]":
                if stack:
                    last_nest = stack.pop()
                    last_nest.add(nest)
                    nest = last_nest
        return nest


s = "[-123,[456,[789]]]"
s = "-3"
print Solution().deserialize(s)
