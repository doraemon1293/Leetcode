class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            while maxq and maxq[-1][0] < num:
                maxq.pop()
            maxq.append((num, right))
            while minq and minq[-1][0] > num:
                minq.pop()
            minq.append((num, right))
            while (maxq[0][0] - minq[0][0]) > limit:
                while maxq[0][1] <= left:
                    maxq.popleft()
                while minq[0][1] <= left:
                    minq.popleft()
                left += 1
            # print(maxq,minq,right,left)
            ans = max(ans, right - left + 1)
        return ans
