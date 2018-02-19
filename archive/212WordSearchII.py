# coding=utf-8
'''
Created on 2017å¹?10æœ?26æ—?

@author: Administrator
'''


class Trie(object):
    END = '/'

    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None


class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = set()
        if board == []: return []
        if words == []: return []
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)

        def dfs(x, y, trie, prefix):
            temp = board[x][y]
            board[x][y] = "*"
            if "/" in trie:
                ans.add(prefix)
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x1 = x + dx
                y1 = y + dy
                if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] in trie:
                    dfs(x1, y1, trie[board[x1][y1]], prefix + board[x1][y1])
            board[x][y] = temp

        trie = trie.root
        for x in xrange(m):
            for y in xrange(n):
                if board[x][y] in trie:
                    dfs(x, y, trie[board[x][y]], board[x][y])
        return list(ans)


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
# board = [["a"]]
# words = ["a"]
print Solution().findWords(board, words)
