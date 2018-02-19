# coding=utf-8
'''
Created on 2017å¹?2æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            word_ori = word
            word = word.lower()
            ch = word[0]
            for i in range(len(rows)):
                if ch in rows[i]:
                    break
            flag = True
            for ch in word[1:]:
                if ch not in rows[i]:
                    flag = False
                    break
            if flag: ans.append(word_ori)
        return ans


words = ["Hello", "Alaska", "Dad", "Peace"]
print Solution().findWords(words)
