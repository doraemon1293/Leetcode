from collections import Counter


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        def gcd(a, b):
            while a % b:
                a, b = b, a % b
            return b

        counter = Counter(deck)
        arr = list(counter.values())
        x = arr[0]
        for y in arr:
            x = gcd(x, y)
        return not x == 1
