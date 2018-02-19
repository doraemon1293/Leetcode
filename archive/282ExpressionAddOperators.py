# coding=utf-8
'''
Created on 2017å¹?5æœ?18æ—?

@author: Administrator
'''

# coding=utf-8
'''
Created on 2017å¹?2æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
#         def isLeadingZeros(num):
#             return num.startswith('00') or int(num) and num.startswith('0')
#         def solve(num, target, mulExpr = '', mulVal = 1):
#             ans = []
#             # remove leading zeros
#             if isLeadingZeros(num):
#                 pass
#             elif int(num) * mulVal == target:
#                 ans += num + mulExpr,
#             for x in range(len(num) - 1):
#                 lnum, rnum = num[:x + 1], num[x + 1:]
#                 # remove leading zeros
#                 if isLeadingZeros(rnum):
#                     continue
#                 right, rightVal = rnum + mulExpr, int(rnum) * mulVal
#                 # op = '+'
#                 for left in solve(lnum, target - rightVal):
#                     ans += left + '+' + right,
#                 # op = '-'
#                 for left in solve(lnum, target + rightVal):
#                     ans += left + '-' + right,
#                 # op = '*'
#                 for left in solve(lnum, target, '*' + right, rightVal):
#                     ans += left,
#             return ans
#         if not num:
#             return []
#         return solve(num, target)

        def hasLeadingZeros(num):
            if num.startswith("00") or (num.startswith("0") and int(num) != 0):
                return True
            else:
                return False

        def divideAndConquer(num, target, mulExp = None, mulVal = None):
            ans = []
            if not hasLeadingZeros(num):
                if mulVal == None:
                    if int(num) == target:
                        ans.append(num)
                else:
                    if int(num) * mulVal == target:
                        ans.append(num + mulExp)
            for x in xrange(1, len(num)):
                left, right = num[:x], num[x:]
                if not hasLeadingZeros(right):
                    right_exp = right + (mulExp if mulExp != None else "")
                    right_val = int(right) * (mulVal if mulVal != None else 1)
                    # print right_exp, right_val
                    for left_exp in divideAndConquer(left, target - right_val):
                        ans.append(left_exp + "+" + right_exp)
                    for left_exp in divideAndConquer(left, target + right_val):
                        ans.append(left_exp + "-" + right_exp)
                    for left_exp in divideAndConquer(left, target, mulExp = "*" + right_exp, mulVal = right_val):
                        ans.append(left_exp)
            return ans

        if num == "": return []
        return divideAndConquer(num, target)


num = "123"
target = 6
print Solution().addOperators(num, target)

