# coding=utf-8
'''
Created on 2016�?11�?25�?

@author: Administrator
'''

# dfs tle or mle
# class Solution(object):
#     def lexicalOrder(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         from gc import collect
#         ans = []
#         current = 0
#         def dfs(current):
#             if current * 10 <= n:
#                 for i in range (10):
#                     next_current = current * 10 + i
#                     if next_current > n:
#                         break
#                     elif next_current != 0:
#                         ans.append(next_current)
#                         dfs(next_current)
#                         collect()
#
#         dfs(current)
#         return ans
# print Solution().lexicalOrder(34)


class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num = 1
        ans = []
        for _ in xrange(n):
            ans.append(num)
            # 能在末尾�?0先加0
            if num * 10 <= n:
                num *= 10
            # 不能�?0 在个位加1
            elif num % 10 != 9 and num + 1 <= n:
                num += 1
            # 个位�?+1也不�? 在最低位可以+1的地�?+1
            else:
                num /= 10
                while num % 10 == 9:
                    num /= 10
                num += 1
        return ans


print Solution().lexicalOrder(13)

