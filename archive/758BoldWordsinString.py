# coding=utf-8
'''
Created on 17 Jan 2018

@author: Administrator
'''


class Solution:

    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        import re
        intervals = []
        for word in words:
            p = '(?=(%s))' % word
            print(p)
            intervals.extend((m.start(1), m.end(1) - 1) for m in re.finditer(p, S))
        intervals.sort()
        print(intervals)
        temp = []
        for interval in intervals:
            if len(temp) == 0:
                temp.append(interval)
            else:
                if interval[0] <= temp[-1][1] + 1:
                    temp[-1] = (temp[-1][0], max(temp[-1][1], interval[1]))
                else:
                    temp.append(interval)
        intervals = temp
        ans = ""
        st = 0
        for interval in intervals:
            ans += S[st:interval[0]]
            ans += "<b>"
            ans += S[interval[0]:interval[1] + 1]
            ans += ("</b>")
            st = interval[1] + 1
        ans += S[st:]
        print(intervals)
        print(ans)
        return ans


        # re.findall(pattern, string, flags)
words = ["ab", "bc"]
S = "aabcd"
print(Solution().boldWords(words, S))
