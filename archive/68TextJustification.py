# coding=utf-8
'''
Created on 2017�?10�?26�?

@author: Administrator
'''


class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_len = 0
        cur_words = []
        ans = []
        ind = 0
        while ind <= len(words):
            # 当前行够空间加新�?
            if ind < len(words) and cur_len + len(words[ind]) <= maxWidth:
                cur_len += len(words[ind]) + 1
                cur_words.append(words[ind])
                ind += 1
            # 当前行不够空间加新词
            elif ind < len(words):
                if len(cur_words) > 1:
                    total_spaces = maxWidth - (cur_len - len(cur_words))
                    gaps = len(cur_words) - 1
                    spaces = [total_spaces / gaps + (1 if i < total_spaces % gaps else 0) for i in xrange(gaps)]
                    temp = []
                    for i in xrange(len(cur_words)):
                        temp.append(cur_words[i])
                        if i != len(cur_words) - 1: temp.append(" "*spaces[i])
                    ans.append("".join(temp))
                else:  # �?个单词的情况
                    ans.append(cur_words[0] + " "*(maxWidth - len(cur_words[0])))
                cur_len = 0
                cur_words = []
            else:
                # �?后一�?
                ans.append(" ".join(cur_words) + " "*(maxWidth - (cur_len - 1)))
                break
        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = [""]
maxWidth = 0
words = ["What", "must", "be", "shall", "be."]
maxWidth = 12
print Solution().fullJustify(words, maxWidth)

