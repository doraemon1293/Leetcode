# coding=utf-8
'''
Created on 2017å¹?6æœ?19æ—?

@author: Administrator
'''


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1    :    'I'    ,
4    :    'IV'    ,
5    :    'V'    ,
9    :    'IX'    ,
10    :    'X'    ,
40    :    'XL'    ,
50    :    'L'    ,
90    :    'XC'    ,
100    :    'C'    ,
400    :    'CD'    ,
500    :    'D'    ,
900    :    'CM'    ,
1000    :    'M'    ,

}
        arr = sorted(d.keys(), reverse = True)

        ans = ""
        for x in arr:
            while num >= x:
                ans += d[x]
                num -= x
        return ans


print Solution().intToRoman(3999)

