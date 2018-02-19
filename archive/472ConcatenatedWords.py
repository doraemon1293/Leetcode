# coding=utf-8
'''
Created on 2017å¹?10æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if words == []: return []
        words.sort(key = len)
        ans = []
        s = set()
        ind = 0
        for x in xrange(ind, len(words)):
            word = words[x]
            if word:
                f = [False] * len(word)
                for i in xrange(len(word)):
                    for j in xrange(-1, i + 1):
                        if (f[j] or j == -1) and word[j + 1:i + 1] in s:
                            f[i] = True
                            break
                if f[-1]:
                    ans.append(word)
                s.add(word)
        return ans


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print Solution().findAllConcatenatedWordsInADict(words)
