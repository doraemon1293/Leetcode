# coding=utf-8
'''
Created on 2016å¹?12æœ?23æ—?

@author: Administrator
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):

    def __init__(self):
        self.buff = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read, need, temp_buff = 0, n, [None] * 4
        while need > 0:
            k = read4(temp_buff)
            self.buff.extend(temp_buff[:k])
            need = min(len(self.buff), n - read)
            buf[read:read + need] = [self.buff.pop(0) for _ in xrange(need)]
            read += need
        return read
