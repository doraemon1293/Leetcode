# coding=utf-8
'''
Created on 2017å¹?8æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        row = col = iw = 0
        sentence = map(len, sentence)
        n = len(sentence)
        d = {}
        times = 0
        while row < rows:
            if iw not in d:
                d[iw] = (row, times)
            else:
                row0, times0 = d[iw]
                loop = (rows - row) / (row - row0)
                row += loop * (row - row0)
                times += loop * (times - times0)
            if row < rows:
                while cols - col >= sentence[iw]:  # å†™ä¸€è¡?
                    col += sentence[iw] + 1
                    iw += 1
                    if iw == n:
                        iw = 0
                        times += 1
                col = 0
                row += 1
        return times


sentence = ["hello", "world"]
sentence = ["a"]
rows = 2000
cols = 8
print Solution().wordsTyping(sentence, rows, cols)
