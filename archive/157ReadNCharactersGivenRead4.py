# coding=utf-8
'''
Created on 2016å¹?12æœ?5æ—?

@author: Administrator
'''


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass


class Solution(object):

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        readed = 0
        temp = 4
        temp_buf = [None] * 4

        while readed < n and temp == 4:
            temp = read4(temp_buf)
            for i in range(temp):
                buf[readed + i] = temp_buf[i]
            readed += temp
        return min(readed, n)
