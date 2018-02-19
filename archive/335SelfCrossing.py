# coding=utf-8
'''
Created on 2017�?11�?3�?

@author: Administrator
'''


class Solution(object):

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
#                 i-2
#     case 1 : i-1┌─�?
#                 └─┼─>i
#                  i-3
#
#                     i-2
#     case 2 : i-1 ┌─�?�?�?�?
#                  └─══>┘i-3
#                  i  i-4      (i overlapped i-4)
#
#     case 3 :    i-4
#                ┌─�?�?
#                │i<┼─�?
#             i-3�? i-5│i-1
#                └─�?�?�?�?
#                 i-2
#
#
        for i in xrange(3, len(x)):
            if (x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]) or \
               (i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]) or \
               (i >= 5 and x[i - 1] + x[i - 5] >= x[i - 3] and x[i - 1] <= x[i - 3] and x[i - 2] >= x[i - 4] and x[i] + x[i - 4] >= x[i - 2]):
                return True
        return False
