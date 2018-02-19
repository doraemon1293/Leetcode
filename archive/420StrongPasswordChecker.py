# coding=utf-8
'''
Created on 2017å¹?9æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        import heapq
        miss = 3
        if any("0" <= c <= "9" for c in s): miss -= 1
        if any("a" <= c <= "z" for c in s): miss -= 1
        if any("A" <= c <= "Z" for c in s): miss -= 1
        repeats = []
        last = ""
        length = 0
        for i in xrange(len(s) + 1):
            if i == len(s) or s[i] != last:
                if length >= 3:
                    repeats.append(length)
                if i != len(s):
                    last = s[i]
                    length = 1
            else:
                length += 1

        if len(s) < 6:
            if max(repeats + [0]) == 5:
                return max(2, miss)
            else:
                return max(6 - len(s), miss)
        else:
            toDelete = max(len(s) - 20, 0)
            q = [(x % 3 , x) for x in repeats]
            heapq.heapify(q)
            while q and toDelete > 0:
                m, x = heapq.heappop(q)
                delete = min(m + 1, toDelete)
                toDelete -= delete
                if x - delete >= 3:
                    heapq.heappush(q, ((x - delete) % 3, x - delete))
            change = sum([x[1] / 3 for x in q])
            return max(len(s) - 20, 0) + max(change, miss)


s = "aaa123"
s = "aA123"
s = "1111111111"
s = "aaaaaaaAAAAAA6666bbbbaaaaaaABBC"
print Solution().strongPasswordChecker(s)

