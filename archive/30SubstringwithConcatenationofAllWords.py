# coding=utf-8
'''
Created on 2017�?8�?4�?

@author: Administrator
'''


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if words == []:
            return []
        counter = Counter(words)
        total = len(words)

        def solve(st_ind, length, s, counter, total):
            temp_words = {}
            temp_total = 0
            st = end = st_ind
            res = []
            while end < len(s):
                # 如果end指向的单词不在words�?
                if s[end:end + length] not in counter:
                    st = end = end + length
                    temp_words = {}
                    temp_total = 0
                # 如果end指向的单词在words�? 而且可以继续消�??
                elif temp_words.get(s[end:end + length], 0) < counter[s[end:end + length]]:
                    temp_words.setdefault(s[end:end + length], 0)
                    temp_words[s[end:end + length]] += 1
                    temp_total += 1
                    if temp_total == total:
                        res.append(st)
                    end += length
                # 如果end指向的单词在words�? 但是已经消�?�光�?
                else:
                    temp_words[s[st:st + length]] -= 1
                    temp_total -= 1
                    st += length
            return res

        ans = []
        for st_ind in xrange(len(words[0])):
            ans += solve(st_ind, len(words[0]), s, counter, total)
        return ans


s = "foofoofoo"
words = ["foo", "foo"]
s = "barfooothefoobarman"
words = ["o", "o"]
print Solution().findSubstring(s, words)

