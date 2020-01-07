import collections
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes):
        counter = collections.Counter(barcodes)
        heap=[(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        ans = []
        while len(ans) < len(barcodes):
            v, k = heapq.heappop(heap)
            if ans and ans[-1] == k:
                v, k = heapq.heapreplace(heap, (v, k))
            ans.append(k)
            heapq.heappush(heap, (v + 1, k))
        return ans


print(Solution().rearrangeBarcodes([1]))
