class Solution:

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = sum([S.count(ch) for ch in J])
        return ans


J = "aA"
S = "aAAbbbb"
print(Solution().numJewelsInStones(J, S))
