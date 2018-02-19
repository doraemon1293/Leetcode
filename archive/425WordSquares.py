# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if words == []: return []
        from collections import defaultdict
        pre = defaultdict(set)
        ans = []
        n = len(words[0])
        for word in words:
            s = ""
            for ch in word:
                s += ch
                pre[s].add(word)

        def search(matrix):
            if len(matrix) == n:
                ans.append(matrix)
            else:
                cur_pre = "".join(zip(*matrix)[len(matrix)])
                # print matrix, cur_pre
                for word in pre[cur_pre]:
                    search(matrix + [word])

        for word in words:
            search([word])
        return ans


words = ["abat", "baba", "atan", "atal"]

print Solution().wordSquares(words)

