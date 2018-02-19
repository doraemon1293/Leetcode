# coding=utf-8
'''
Created on 2017å¹?7æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict

        def get_abbr(words, preLen):
            abbrs = defaultdict(set)
            for word in words:
                l = len(word)
                if l < preLen + 3:
                    abbr_word = word
                else:
                    abbr_word = word[:preLen] + str(l - preLen - 1) + word[-1]
                abbrs[abbr_word].add(word)
            temp = list(abbrs.items())
            for abbr_word, words in temp:
                if len(words) > 1:
                    new_abbr = get_abbr(words, preLen + 1)
                    del abbrs[abbr_word]
                    abbrs.update(new_abbr)
            return abbrs

        abbrs = get_abbr(words, 1)
        rev_abbrs = dict([(v.pop(), k) for k, v in abbrs.items()])
        ans = []
        for word in words:
            ans.append(rev_abbrs[word])
        return ans


words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
print Solution().wordsAbbreviation(words)

