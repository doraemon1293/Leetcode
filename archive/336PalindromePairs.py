# coding=utf-8
'''
Created on 2017å¹?10æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def isPalindrome(word):
            i, j = (len(word) - 1) / 2, len(word) / 2
            while i >= 0 and j < len(word) and word[i] == word[j]:
                i -= 1
                j += 1
            return i == -1

        word_ind = dict([(word, i) for i, word in enumerate(words)])
        print word_ind
        ans = set()
        for i, word in enumerate(words):
            if "" in word_ind and isPalindrome(word):
                if i != word_ind[""]:
                    ans.add((word_ind[""], i))
                    ans.add((i, word_ind[""]))
            if word[::-1] in word_ind:
                if i != word_ind[word[::-1]]:
                    ans.add((i, word_ind[word[::-1]]))
                    ans.add((word_ind[word[::-1]], i))
            for k in xrange(1, len(word)):
                left = word[:k]
                right = word[k:]
                if right[::-1] in word_ind and isPalindrome(left):
                    if i != word_ind[right[::-1]]:
                        ans.add((word_ind[right[::-1]], i))
                if left[::-1] in word_ind and isPalindrome(right):
                    if i != word_ind[left[::-1]]:
                        ans.add((i, word_ind[left[::-1]]))
        ans = [list(x) for x in ans]
        return ans


words = ["abcd", "dcba", "lls", "s", "sssll"]
print Solution().palindromePairs(words)
