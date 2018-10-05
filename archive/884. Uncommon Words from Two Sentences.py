class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        return [k for k,v in Counter(A.split() + B.split()).most_common() if v==1]