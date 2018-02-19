import heapq


class Solution(object):

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        nums = [x for x in nums if x]
        k = len(nums)
        pointers = [0] * k
        heap = [(nums[i][0], i) for i in xrange(k)]
        heapq.heapify(heap)
        lb = min(heap)[0]
        ub = max(heap)[0]
        ans = [lb, ub]
        while True:
            _, i = heapq.heappop(heap)
            pointers[i] += 1
            if pointers[i] == len(nums[i]):
                break
            val = nums[i][pointers[i]]
            heapq.heappush(heap, (val, i))
            lb = heap[0][0]
            ub = max(ub, val)
            if ans[1] - ans[0] > ub - lb or ans[1] - ans[0] == ub - lb and ans[0] > lb:
                ans = [lb, ub]
        return ans


nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print Solution().smallestRange(nums)
