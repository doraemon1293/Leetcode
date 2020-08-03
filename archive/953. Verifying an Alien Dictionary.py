class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for i, ch in enumerate(order):
            d[ch] = i

        def is_lte(w1, w2):
            length = min(len(w1), len(w2))
            for i in range(length):
                if d[w1][i] < d[w2][i]:
                    return True
                elif d[w1][i] > d[w2][i]:
                    return False
            return len(w1) <= len(w2)

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not is_lte(words[i].words[j]):
                    return False
        return True


