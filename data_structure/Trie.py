# coding=utf-8
'''
Created on 2017å¹?7æœ?24æ—?

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

    def find(self, word):  # find whether a word in Trie
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node

    def find_prefix(self, word):  # find the shortest prefix of the word in Trie, if cannot find return word itself
        node = self.root
        res = []
        i = 0
        while i < len(word) and node != None:
            node = node.get(word[i], None)
            if node != None:
                res.append(word[i])
                if self.END in node:
                    return "".join(res)
            i += 1
        return word

