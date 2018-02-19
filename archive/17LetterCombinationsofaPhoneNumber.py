# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''


# recursive
class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        num_alpha = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        res = [None] * len(digits)
        ans = []

        def rec(res, i, n):
            if i == n:
                ans.append("".join(res))
            else:
                for c in num_alpha[int(digits[i])]:
                    res[i] = c
                    rec(res, i + 1, n)

        rec(res, 0, n)
        return ans


digits = "1023"
print Solution().letterCombinations(digits)

# Using reduce
# class Solution:
#     # @return a list of strings, [s1, s2]
#     def letterCombinations(self, digits):
#         if '' == digits: return []
#         kvmaps = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#         return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

# BFS
# class Solution:
#     # @return a list of strings, [s1, s2]
#     def letterCombinations(self, digits):
#         if '' == digits: return []
#         kvmaps = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#         ret = ['']
#         for c in digits:
#             tmp = []
#             for y in ret:
#                 for x in kvmaps[c]:
#                     tmp.append(y + x)
#             ret = tmp
#
#         return ret
digits = "23"
print Solution().letterCombinations(digits)
