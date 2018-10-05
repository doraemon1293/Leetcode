from random import randint
import bisect


class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.interval = [0]
        self.rects = rects
        for rect in rects:
            x1, y1, x2, y2 = rect
            weight = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.interval.append(self.interval[-1] + weight)

    def pick(self):
        """
        :rtype: List[int]
        """
        temp = randint(0, self.interval[-1] - 1)
        ind = bisect.bisect_right(self.interval, temp) - 1
        x1, y1, x2, y2 = self.rects[ind]
        return [randint(x1, x2), randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# rects = [[1, 1, 5, 5]]
# obj = Solution(rects)
# print(obj.pick())
