from bisect import bisect_left, bisect_right


class RangeModule(object):

    def __init__(self):
        self.range = [-float('inf'), float('inf')]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        li = bisect_left(self.range, left)
        ri = bisect_right(self.range, right)
        if li % 2 == 0:
            li = li - 1
            left = self.range[li]
        if ri % 2 == 0:
            right = self.range[ri]
            ri += 1
        self.range[li:ri] = [left, right]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        li = bisect_right(self.range, left)
        ri = bisect_left(self.range, right)
        return li == ri and li % 2 == 0

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        li = bisect_left(self.range, left)
        ri = bisect_right(self.range, right)
        if li % 2 == 1:
            li = li - 1
            left = self.range[li]
        if ri % 2 == 1:
            right = self.range[ri]
            ri += 1
        self.range[li:ri] = [left, right]

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
