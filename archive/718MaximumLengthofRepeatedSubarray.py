# coding=utf-8
'''
Created on 2017�?10�?30�?

@author: Administrator
'''


class Solution(object):

    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = [[0 for i in range(len(B) + 1)]  for j in range(len(A) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一�?
        maxi = 0  # �?长匹配的长度
        st = 0  # �?长匹配对应在A中的�?后一�?
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    m[i + 1][j + 1] = m[i][j] + 1
                    if m[i + 1][j + 1] > maxi:
                        maxi = m[i + 1][j + 1]
                        p = i + 1
        print A[p - maxi:p]
        return maxi  # 返回�?长子串及其长�?
