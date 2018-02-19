# coding=utf-8
'''
Created on 2017å¹?6æœ?11æ—?

@author: Administrator
'''
import collections
import re


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letters = collections.deque(re.split(r"\d+", compressedString)[:-1])
        self.numbers = collections.deque(map(int, re.split(r"[a-zA-Z]+", compressedString)[1:]))

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            ans = self.letters[0]
            self.numbers[0] -= 1
            if self.numbers[0] == 0:
                self.letters.popleft()
                self.numbers.popleft()
            return ans
        else:
            return " "

    def hasNext(self):
        """
        :rtype: bool
        """
        return  bool(len(self.letters))


compressedString = "L1e2t1C1o1d1e1"
# Your StringIterator object will be instantiated and called as such:
obj = StringIterator(compressedString)
print  obj.next()
print  obj.next()
