# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        k = 0  # 0 top 1 right 2 bot 3 left
        ans = []
        while matrix and matrix[0]:
            # print matrix
            if k == 0:
                ans.extend(matrix[0])
                del matrix[0]
            if k == 1:
                ans.extend(zip(*matrix)[-1])
                matrix = [x[:-1] for x in matrix]
            if k == 2:
                ans.extend(matrix[-1][::-1])
                del matrix[-1]
            if k == 3:
                ans.extend(zip(*matrix)[0][::-1])
                matrix = [x[1:] for x in matrix]
            k = (k + 1) % 4
        return ans


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix = [[7], [9], [6]]
print Solution().spiralOrder(matrix)

