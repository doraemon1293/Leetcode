import itertools


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.generator = itertools.chain(*[x for x in itertools.izip_longest(v1, v2)])
        self.count = len(v1) + len(v2)

    def next(self):
        """
        :rtype: int
        """
        self.count -= 1
        ans = self.generator.next()
        while ans == None:
            ans = self.generator.next()
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0


v1 = []

v2 = []
# Your ZigzagIterator object will be instantiated and called as such:
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print v
