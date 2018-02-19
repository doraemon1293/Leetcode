# coding=utf-8
'''
Created on 2017å¹?11æœ?20æ—?

@author: Administrator
'''


def designProbTest(functions, parameters):
    for i in xrange(len(functions)):
        f, para = functions[i], parameters[i]
        if f[0].isupper():
            cls = eval(f + "(*para)")
        else:
            print eval("cls." + f + "(*para)")


from bisect import bisect_left, bisect_right


class MyCalendarTwo(object):

    def __init__(self):
        self.x = [-float('inf'), float('inf')]
        self.y = [-float('inf'), float('inf')]

    def addRange(self, range, start, end):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        li = bisect_left(range, start)
        ri = bisect_right(range, end)
        if li % 2 == 0:
            li = li - 1
            start = range[li]
        if ri % 2 == 0:
            end = range[ri]
            ri += 1
        range[li:ri] = [start, end]

    def noOverlap(self, start, end):
        li = bisect_right(self.y, start)
        ri = bisect_left(self.y, end)
        if li == ri and li % 2 == 1:
            return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # print start, end
        overlaps = []
        i0 = bisect_left(self.x, start)
        # print i0
        if i0 % 2 == 0:
            i0 -= 1
        while self.x[i0] < end:
            if max(self.x[i0], start) < min(self.x[i0 + 1], end):
                overlaps.append([max(self.x[i0], start), min(self.x[i0 + 1], end)])
            i0 += 2
        # print overlaps
        for left, right in overlaps:
            if not self.noOverlap(left, right):
                return False
        self.addRange(self.x, start, end)
        for left, right in overlaps:
            self.addRange(self.y, left, right)
        # print self.x
        # print self.y
        return True


functions = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
parameters = [[], [36, 41], [28, 34], [40, 46], [10, 18], [4, 11], [25, 34], [36, 44], [32, 40], [34, 39], [40, 49]]
designProbTest(functions, parameters)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
