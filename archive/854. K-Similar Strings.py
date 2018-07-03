class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        from collections import deque
        def neighbour(s):
            i = 0
            while s[i] == B[i]:
                i += 1
            arr = list(s)
            ret = []
            for j in range(i + 1, len(A)):
                if s[j] == B[i]:
                    arr[i], arr[j] = arr[j], arr[i]
                    ret.append("".join(arr))
                    arr[i], arr[j] = arr[j], arr[i]
            return ret
        if A==B: return 0
        visited = {A: 0}
        q = deque([A])
        while q:
            s = q.popleft()
            step = visited[s]
            for s1 in neighbour(s):
                if s1 == B:
                    return step + 1
                if s1 not in visited:
                    visited[s1] = step + 1
                    q.append(s1)
        return -1