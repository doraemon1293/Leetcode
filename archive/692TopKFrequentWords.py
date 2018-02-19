# coding=utf-8
'''
Created on 2017å¹?10æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter, defaultdict
        import heapq
        count = Counter(words)
        d = defaultdict(list)
        for key, val in count.items():
            heapq.heappush(d[val], key)
        keys = [-x for x in d.keys()]
        heapq.heapify(keys)
        cur_key = -heapq.heappop(keys)

        ans = []
        while k:
            ans.append(heapq.heappop(d[cur_key]))
            k -= 1
            if k:
                if len(d[cur_key]) == 0:
                    cur_key = -heapq.heappop(keys)
        return ans


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print Solution().topKFrequent(words, k)

