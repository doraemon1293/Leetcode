import collections


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(s, a):
            res = []
            for i, ch in enumerate(s):
                if i % 2 == 0:
                    res.append(ch)
                else:
                    res.append(str((int(ch) + a) % 10))
            return "".join(res)

        def rotate(s, b):
            return s[-b:] + s[:-b]

        visited = set([s])
        q = collections.deque()
        q.append(s)
        while q:
            s = q.popleft()
            s1 = add(s, a)
            s2 = rotate(s, b)
            for s in (s1, s2):
                if s not in visited:
                    visited.add(s)
                    q.append(s)
        return min(visited)


print(Solution().findLexSmallestString(s="5525", a=9, b=2))
