# coding=utf-8
'''
Created on 2017å¹?11æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
#                 i-2
#     case 1 : i-1â”Œâ”€â”?
#                 â””â”€â”¼â”€>i
#                  i-3
#
#                     i-2
#     case 2 : i-1 â”Œâ”€â”?â”?â”?â”?
#                  â””â”€â•â•>â”˜i-3
#                  i  i-4      (i overlapped i-4)
#
#     case 3 :    i-4
#                â”Œâ”€â”?â”?
#                â”‚i<â”¼â”€â”?
#             i-3â”? i-5â”‚i-1
#                â””â”€â”?â”?â”?â”?
#                 i-2
#
#
        for i in xrange(3, len(x)):
            if (x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]) or \
               (i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]) or \
               (i >= 5 and x[i - 1] + x[i - 5] >= x[i - 3] and x[i - 1] <= x[i - 3] and x[i - 2] >= x[i - 4] and x[i] + x[i - 4] >= x[i - 2]):
                return True
        return False
