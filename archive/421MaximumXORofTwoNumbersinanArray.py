# coding=utf-8
'''
Created on 2017å¹?5æœ?25æ—?

@author: Administrator
'''


class Trie(object):

    def __init__(self):
        self.children = [None, None]


class Solution(object):

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Trie()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                x = num >> i & 1
                if node.children[x] == None:
                    node.children[x] = Trie()
                node = node.children[x]

        maxi = -float("inf")
        for num in nums:
            node = root
            ans = 0
            for i in range(31, -1, -1):
                ans <<= 1
                x = (num >> i & 1) ^ 1
                if node.children[x] != None:
                    ans += 1
                    node = node.children[x]
                else:
                    node = node.children[x ^ 1]
            maxi = max(maxi, ans)

        return maxi

