# coding=utf-8
'''
Created on 2017å¹?9æœ?10æ—?

@author: Administrator
'''
from collections import defaultdict


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fuzzy_dict = defaultdict(int)
        self.dict = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.dict.add(word)
            for i in xrange(len(word)):
                self.fuzzy_dict[word[:i] + "_" + word[i + 1:]] += 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(word)):
            if word[:i] + "_" + word[i + 1:] in self.fuzzy_dict:
                if self.fuzzy_dict[word[:i] + "_" + word[i + 1:]] == 1:
                    if word in self.dict:
                        continue
                    else:
                        return True
                else:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
d = MagicDictionary()
d.buildDict(["hello", "hallo", "leetcode"])
print d.search("hello")

