class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        summ=[0]
        for x in A:
            summ.append(summ[-1]+x)
        from collections import deque
        q=deque()
        ans=float("inf")
        for y in range(len(summ)):
            while q and summ[q[-1]]>=summ[y]:
                q.pop()
            while q and summ[q[0]]<=summ[y]-K:
                x=q.popleft()
                ans=min(ans,y-x)
            q.append(y)
        return -1 if ans==float("inf") else ans
