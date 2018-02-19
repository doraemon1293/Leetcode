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

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        def get_depth(nestedInteger):
            if nestedInteger.isInteger():
                return 1
            if nestedInteger.getList():
                return max([get_depth(ni) for ni in nestedInteger.getList()]) + 1
            else:
                return 1

        def calc(nestedInteger, depth):
            if nestedInteger.isInteger():
                return nestedInteger.getInteger() * depth
            else:
                return sum([calc(ni, depth - 1) for ni in nestedInteger.getList()])

        if nestedList:
            depth = max(get_depth(nestedInteger) for nestedInteger in nestedList)
            return sum([calc(nestedInteger, depth) for nestedInteger in nestedList])
        else:
            return 0

        return sum[calc(x)[0] for x in nestedList.getList()]
