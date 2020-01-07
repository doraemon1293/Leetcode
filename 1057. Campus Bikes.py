import heapq


class Solution:
    def assignBikes(self, workers, bikes):
        arr = [(abs(w[0] - b[0]) + abs(w[1] - b[1]), i, j) for i, w in enumerate(workers) for j, b in enumerate(bikes)]
        heapq.heapify(arr)
        ans = [None] * len(workers)
        removed_w = set()
        removed_b = set()
        n = 0
        while n < len(workers):
            dis, w, b = heapq.heappop(arr)
            if w not in removed_w and b not in removed_b:
                ans[w] = b
                n += 1
                removed_w.add(w)
                removed_b.add(b)
        return ans
