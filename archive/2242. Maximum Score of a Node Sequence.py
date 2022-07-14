class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        nei = {}
        for a, b in edges:
            nei.setdefault(a, [])
            nei.setdefault(b, [])

            nei[a].append(b)
            nei[b].append(a)
            if len(nei[a]) > 3:
                nei[a] = sorted(nei[a], key=lambda x: scores[x], reverse=True)[:3]
                # print(a,[(x,scores[x])for x in nei[a]])
            if len(nei[b]) > 3:
                nei[b] = sorted(nei[b], key=lambda x: scores[x], reverse=True)[:3]
                # print(b,[(x,scores[x])for x in nei[b]])

        ans = -1
        for a, b in edges:
            for x in nei[a]:
                for y in nei[b]:
                    if len(set([a, b, x, y])) == 4:
                        ans = max(ans, scores[a] + scores[b] + scores[x] + scores[y])
        return ans
