class Solution:
    def camelMatch(self, queries: list, pattern: str) -> list:
        ans = []

        def foo(q, pattern):
            p1 = p2 = 0
            while p1 < len(q) and p2 < len(pattern):
                while p1 < len(q) and q[p1] != pattern[p2]:
                    if q[p1].isupper():
                        print(q[p1])
                        return False
                    p1 += 1
                if p1 < len(q):
                    p1 += 1
                    p2 += 1
            if p2 < len(pattern):
                return False
            else:
                while p1 < len(q):
                    if q[p1].isupper():
                        return False
                    p1 += 1
                return True

        for q in queries:
            ans.append(foo(q, pattern))
        return ans


queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBaT"
print(Solution().camelMatch(queries, pattern))
