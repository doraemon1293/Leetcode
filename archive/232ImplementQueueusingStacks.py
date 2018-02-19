# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


class Queue(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        while self.q:
            x = self.q.pop()
            temp.append(x)
        temp.pop()
        while temp:
            self.q.append(temp.pop())

    def peek(self):
        """
        :rtype: int
        """
        temp = []
        while self.q:
            x = self.q.pop()
            temp.append(x)
        ans = temp.pop()
        self.q.append(ans)
        while temp:
            self.q.append(temp.pop())
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.q)


q = Queue()
print q.empty()
