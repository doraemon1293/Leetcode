import heapq
class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        heapq.heapify(blocks)
        while len(blocks)>1:
            a=heapq.heappop(blocks)
            b=heapq.heappop(blocks)
            ab=max(a,b)+split
            heapq.heappush(blocks,ab)
        return blocks[0]
