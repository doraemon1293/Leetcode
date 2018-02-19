# coding=utf-8
'''
Created on 2017å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # nearly TLE
#         if k == 0 or s == "": return s
#         from collections import Counter, deque
#         counter = Counter(s)
#         q = deque()
#         ans = []
#         for _ in xrange(len(s)):
#             if len(q) == k:
#                 q.popleft()
#             flag = False
#             for ch, n in counter.most_common():
#                 if ch not in q:
#                     counter[ch] -= 1
#                     if counter[ch] == 0:
#                         del counter[ch]
#                     ans.append(ch)
#                     q.append(ch)
#                     flag = True
#                     break
#             if not flag: return ""
#         return "".join(ans)

        # heap method
        if k == 0 or s == "": return s
        from collections import Counter, deque
        import heapq
        heap = [(-freq, ch) for ch, freq in Counter(s).items()]
        heapq.heapify(heap)
        q = deque()
        ans = []
        for _ in xrange(len(s)):
            if len(q) == k:
                freq, ch = q.popleft()
                if freq != 0:
                    heapq.heappush(heap, (freq, ch))
            if heap:
                freq, ch = heapq.heappop(heap)
                ans.append(ch)
                q.append((freq + 1, ch))
            else:
                return ""
        return "".join(ans)


s = "aaabc"
k = 3
print Solution().rearrangeString(s, k)
