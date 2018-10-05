from collections import Counter


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        uni={}
        for b in B:
            b_counter = Counter(b)
            for ch in b_counter:
                uni[ch] = max(b_counter[ch], uni.get(ch, 0))
        ans = []
        for a in A:
            a_counter = Counter(a)
            if all(a_counter[ch] >= uni[ch] for ch in uni):
                ans.append(a)
        return ans
