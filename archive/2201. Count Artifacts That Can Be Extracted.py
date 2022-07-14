class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        d = {}
        for i, a in enumerate(artifacts):
            r1, c1, r2, c2 = a
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    d[x, y] = i
        for x, y in dig:
            if (x, y) in d:
                del d[x, y]

        return len(artifacts) - len(set(d.values()))
