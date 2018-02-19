# coding=utf-8
'''
Created on 2017å¹?9æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        banlance = defaultdict(int)
        for p0, p1, money in transactions:
            banlance[p0] += money
            banlance[p1] -= money
        pos = tuple(sorted([v for v in banlance.values() if v > 0]))
        neg = tuple(sorted([-v for v in banlance.values() if v < 0]))
        d = {}

        def dfs(pos, neg):
            pos_len = len(pos)
            neg_len = len(neg)
            if min(pos_len, neg_len) <= 1:
                return max(pos_len, neg_len)
            if (pos, neg) in d:
                return d[(pos, neg)]
            res = float("inf")
            money2 = neg[0]
            for i, money1 in enumerate(pos):
                if money1 == money2:
                    new_pos = pos[:i] + pos[i + 1:]
                    new_neg = neg[1:]
                    res = dfs(new_pos, new_neg) + 1
                    d[(pos, neg)] = res
                    return res
                elif money1 > money2:
                    new_pos = list(pos[:])
                    new_pos[i] = money1 - money2
                    new_pos.sort()
                    new_neg = neg[1:]
                    res = min(res, dfs(tuple(new_pos), new_neg) + 1)
                else:
                    new_pos = pos[:i] + pos[i + 1:]
                    new_neg = list(neg[:])
                    new_neg[0] = money2 - money1
                    new_neg.sort()
                    res = min(res, dfs(new_pos, tuple(new_neg)) + 1)
            d[(pos, neg)] = res
            return res

        return dfs(pos, neg)


transactions = [[0, 1, 10], [2, 0, 5]]
transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]

print Solution().minTransfers(transactions)
