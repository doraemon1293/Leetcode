from collections import deque


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        q = deque(sorted(tokens))
        ans = points = 0
        while q and (q[0] <= P or points):
            if q and q[0] <= P:
                points += 1
                P -= q.popleft()
                ans = max(ans, points)
            else:
                P += q.pop()
                points -= 1
            #print(q,P,points)
        return ans


print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], P=200))
print(Solution().bagOfTokensScore(tokens=[100, 200], P=150))
print(Solution().bagOfTokensScore(tokens=[100], P=50))
