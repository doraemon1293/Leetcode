class Solution:

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = [arr[0]]
        for i in range(1, len(arr)):
            maxi.append(max(maxi[-1], arr[i]))
        mini = [arr[-1]]
        for i in range(len(arr) - 2, -1, -1):
            mini.append(min(mini[-1], arr[i]))
        mini = mini[::-1]
        ans = 0
        for i in range(len(arr) - 1):
            if maxi[i] <= mini[i + 1]:
                ans += 1
        return ans


arr = list(range(2000))
print(Solution().maxChunksToSorted(arr))

