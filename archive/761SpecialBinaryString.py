# coding=utf-8
'''
Created on 16 Jan 2018

@author: Administrator
'''


# solution: https://discuss.leetcode.com/topic/116280/easy-and-concise-solution-with-explanation-c-java-python/2
class Solution:

    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """

        def solve(s):
            count = i = 0
            strings = []
            for j, ch in enumerate(s):
                if ch == "0":
                    count -= 1
                else:
                    count += 1
                if count == 0:
                    strings.append("1" + solve(s[i + 1:j]) + "0")
                    i = j + 1
            strings.sort(reverse = True)
            return "".join(strings)

        return solve(S)


S = "11011000"
print(Solution().makeLargestSpecial(S))
