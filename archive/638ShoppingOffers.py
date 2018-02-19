# coding=utf-8
'''
Created on 2017å¹?7æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        ind = 0
        while ind < len(special):
            p = 0
            for i, x in enumerate(special[ind][:-1]):
                p += price[i] * x
            if p <= special[ind][-1]:
                del special[ind]
            else:
                ind += 1

        def sub(a, b):
            return [a[i] - b[i] for i in xrange(len(a))]

        def dfs(price, special, needs):
            if all(x == 0 for x in needs):
                return 0
            elif any(x < 0 for x in needs):
                return float("inf")
            else:
                return min([sum([needs[i] * price[i] for i in xrange(len(needs))])] + [spe[-1] + dfs(price, special, [needs[i] - spe[i] for i in xrange(len(needs))]) for spe in special])

        return dfs(price, special, needs)


price = [2, 5]
special = [[3, 0, 5], [1, 2, 10]]
needs = [3, 2]
print Solution().shoppingOffers(price, special, needs)

