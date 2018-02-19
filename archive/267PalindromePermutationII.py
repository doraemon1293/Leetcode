# coding=utf-8
'''
Created on 2017å¹?8æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import Counter
        import itertools

        def permutation(counter):
            s = reduce(lambda x, y:[] + x + y, [[k] * v for k, v in counter.items()], [])
            ans = [[]]
            for ch in s:
                new_ans = []
                for arr in ans:
                    for i in xrange(len(arr) + 1):
                        new_ans.append(arr[:i] + [ch] + arr[i:])
                        if i < len(arr) and arr[i] == ch: break
                ans = new_ans
            return ans

        counter = Counter(s)
        ones = 0
        for k, v in counter.items():
            if v % 2 == 1:
                mid = k
                ones += 1
                if ones > 1:
                    return []
        ans = []
        if ones == 0:
            for k in counter:
                counter[k] /= 2
            for s1 in permutation(counter):
                ans.append("".join(s1 + s1[::-1]))
        else:
            counter[mid] -= 1
            if counter[mid] == 0: del counter[mid]
            for k in counter:
                counter[k] /= 2
            for s1 in permutation(counter):
                ans.append("".join(s1 + [mid] + s1[::-1]))
        return ans


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s = "a"
print Solution().generatePalindromes(s)

